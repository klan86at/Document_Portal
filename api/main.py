# Libraries
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.doc_ingestion.data_ingestion import (
    ChatIngestor,  # cSpell:ignore Ingestor
    DocHandler,
    DocumentComparator
)
from src.doc_analyzer.data_analysis import DocumentAnalyzer
from src.doc_compare.doc_comparator import DocumentComparatorLLM
from src.doc_chat.retrieval import ConversationalRAG
from utils.doc_ops import FastAPIFileAdapter, read_pdf_via_handler
# from logger import GLOBAL_LOGGER as log

FAISS_BASE = os.getenv("FAISS_BASE", "faiss_index")  # cSpell:ignore FAISS
UPLOAD_BASE = os.getenv("UPLOAD_BASE", "data")
FAISS_INDEX_NAME = os.getenv("FAISS_INDEX_NAME", "index")  # <--- keep consistent with save_local()

app = FastAPI(title="DevPortal API", version="1.0.0")  # object of fastapi class

BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    resp = templates.TemplateResponse("index.html", {"request": request})
    resp.headers["Cache-Control"] = "no-store"
    return resp

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "Document_Portal"}


@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)) -> Any:
    try:
        dh = DocHandler()
        save_path = dh.save_pdf(FastAPIFileAdapter(file))
        text = read_pdf_via_handler(dh, save_path)

        analyzer = DocumentAnalyzer()
        result = analyzer.analyze_document(text)
        return JSONResponse(content=result)
    except HTTPException:
        raise
    except Exception as e:
        # log.exception("Error during document analysis")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")
    
@app.post("/compare")
async def compare_documents(reference: UploadFile = File(...), actual: UploadFile = File(...)) -> Any:
    try:
        dc = DocumentComparator()
        ref_path, act_path = dc.save_uploaded_files(FastAPIFileAdapter(reference), FastAPIFileAdapter(actual))
        _ = ref_path, act_path  # Placeholder for actual comparison logic
        combined_text = dc.combine_documents()
        comp = DocumentComparatorLLM()
        df = comp.compare_documents(combined_text)
        return {"rows": df.to_dict(orient="records"), "session_id": dc.session_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {e}")
    
@app.post("/chat/index")
async def chat_build_index(
    files: List[UploadFile] = File(...),
    session_id: Optional[str] = Form(None),
    use_session_dirs: bool = Form(True),
    chunk_size: int = Form(1000),
    chunk_overlap: int = Form(200),
    k: int = Form(5),
) -> Any:
    try:
        wrapped = [FastAPIFileAdapter(f) for f in files]
        ci = ChatIngestor(
            temp_base = UPLOAD_BASE,
            faiss_base = FAISS_BASE,
            use_session_dirs = use_session_dirs,
            session_id = session_id or None,
        )
        ci.build_retriever(wrapped, chunk_size=chunk_size, chunk_overlap=chunk_overlap, k=k)
        return {"session_id": ci.session_id, "k": k, "use_session_dirs": use_session_dirs}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {e}")
    
@app.post("/chat/query")
async def chat_query(
    question: str = Form(...),
    session_id: Optional[str] = Form(None),
    k: int = Form(5),
    use_session_dirs: bool = Form(True),
) -> Any:
    try:
        if use_session_dirs and not session_id:
            raise HTTPException(status_code=400, detail="Session ID is required when using session directories.")
        
        # Prepare FAISS index path
        index_dir = os.path.join(FAISS_BASE, session_id) if use_session_dirs else FAISS_BASE #type: ignore
        if not os.path.isdir(index_dir):
            raise HTTPException(status_code=400, detail=f"FAISS index not found at: {index_dir}")
        
        # Initialize LCEL-style RAg pipeline
        rag = ConversationalRAG(session_id=session_id) # type: ignore
        rag.load_retriever_from_faiss(index_dir)

        # Optional: for now we pass empty chat history
        response = rag.invoke(question, chat_history=[])

        return {
            "answer": response,
            "session_id": session_id,
            "k": k,
            "engine": "LCEL-RAg"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {e}")
    
# How to run the app:
# 1. Save this code in a file named `main.py`.
# 2. Run the app using the command: `uvicorn main:app --reload`
# 3. Access the API at `http://

# uvicorn api.main:app --reload`