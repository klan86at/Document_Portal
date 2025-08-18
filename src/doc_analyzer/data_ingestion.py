from fileinput import filename
import os
import fitz  # cSpell:ignore fitz
import uuid
from datetime import datetime

from requests import session
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from src import doc_analyzer

class DocumentHandler:
    """
    Handles PDF saving and reading operations.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self, data_dir=None, session_id=None):
        try:
            self.log=CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv(
                "DATA_STORAGE_PATH",
                os.path.join(os.getcwd(), "data", "doc_analysis")
            )
            self.session_id = session_id or f"session_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

            # Create base session directory
            self.session_path = os.path.join(self.data_dir, self.session_id)
            os.makedirs(self.session_path, exist_ok=True)

            self.log.info("PDFHandler initialized", session_id=self.session_id, session_path=self.session_path)
        except Exception as e:
            self.log.error("Error initializing DocumentHandler", {e})
            raise DocumentPortalException("Error initializing PDFHandler", e) from e
        
    def save_pdf(self, uploaded_file):
        try:
            filename = os.path.basename(uploaded_file.name)
            if not filename.lower().endswith('.pdf'):
                raise DocumentPortalException("Uploaded file is not a PDF")
            
            save_path = os.path.join(self.session_path, filename)

            with open(save_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())  # cSpell:ignore getbuffer

            self.log.info("PDF saved successfully", file=filename, save_path=save_path, session_id=self.session_id)
            return save_path
        except Exception as e:
            self.log.error(f"Error saving PDF: {e}")
            raise DocumentPortalException("Error saving PDF", e) from e

    def read_pdf(self, pdf_path:str) -> str:
        try:
            text_chunks = []
            with fitz.open(pdf_path) as doc:
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    text_chunks.append(f"\n--- Page {page_num + 1} ---\n{page.get_text()}")  # type: ignore
            text = "\n".join(text_chunks)

            self.log.info("PDF read successfully", pdf_path=pdf_path, session_id=self.session_id, pages=len(text_chunks))
            return text
        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("Error reading PDF", e) from e

if __name__ == "__main__":
    from pathlib import Path
    from io import BytesIO
    handler = DocumentHandler()

    # cSpell:ignore LLMOPs
    pdf_path =r"D:\\LLMOPs\\Document_Portal\\data\\doc_analysis\\AppliedAI_White_Paper_Retrieval-augmented-Generation-Realized_FINAL_20240618.pdf"

    class DummyFile:
        def __init__(self, file_path):
            self.name = Path(file_path).name
            self.file_path = file_path

        def getbuffer(self):
            return open(self.file_path, "rb").read()
        
    dummy_pdf = DummyFile(pdf_path)

    handler = DocumentHandler(session_id="test_session")

    try:
        saved_path = handler.save_pdf(dummy_pdf)
        print(saved_path)

        content = handler.read_pdf(saved_path)
        print(content[:100])
    except Exception as e:
        print(f"Error: {e}")
