from itertools import count
from multiprocessing import Value
import sys
from pathlib import Path
import uuid
from datetime import datetime, timezone
import fitz  # cSpell:ignore fitz
from sqlalchemy import all_
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentIngestion:
    def __init__ (self, base_dir: str="data/doc_compare", session_id=None):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S_%f')}_{uuid.uuid4().hex[:8]}"
        self.session_path = self.base_dir / self.session_id
        self.session_path.mkdir(parents=True, exist_ok=True)
    
    
    def save_uploaded_files(self, reference_file, actual_file):
        """
        Saves uploaded files to a specific directory.
        """
        try:
            ref_path= self.base_dir / reference_file.name
            act_path= self.base_dir / actual_file.name

            if not reference_file.name.lower().endswith(".pdf") or not actual_file.name.lower().endswith(".pdf"):
                raise ValueError("Only PDF files are allowed.")
            
            with open(act_path, "wb") as f:
                f.write(actual_file.getbuffer())  # cSpell:ignore getbuffer

            with open(ref_path, "wb") as f:
                f.write(reference_file.getbuffer())  # cSpell:ignore getbuffer 

            self.log.info("Files saved", reference=str(ref_path), actual=str(act_path))
            return ref_path, act_path
        
        except Exception as e:
            self.log.error(f"Error saving uploaded files, {e}")
            raise DocumentPortalException("Error saving uploaded files", sys)
    
    def read_pdf(self, pdf_path: Path)-> str:
        """
        Reads a PDF file and extracts text from each page.
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:  # Check if PDFis encrypted:
                    raise ValueError(f"PDF file is encrypted: {pdf_path.name}")
                all_text = []
                for page_num in range(doc.page_count):
                    page=doc.load_page(page_num)
                    text=page.get_text() #type: ignore
                    if text.strip():  # Check if text is not empty
                        all_text.append(f"\n --- Page {page_num + 1} --- \n{text}")
                self.log.info("PDF file read successfully", file=str(pdf_path), pages=len(all_text))
                return "\n".join(all_text)  
        except Exception as e:
            self.log.error(f"Error reading PDF file, {e}")
            raise DocumentPortalException("Error reading PDF file", sys)
        
    def combine_documents(self) -> str:
        """
        Combines text from all PDFs in the base directory.
        """
        try:
            content_dict = {}
            doc_parts = []

            for filename in sorted(self.session_path.iterdir()):
                if filename.is_file() and filename.name.endswith(".pdf"):
                    content = self.read_pdf(filename)
                    doc_parts.append(f"Document: {filename.name}\n{content}")

            combined_text = "\n\n".join(doc_parts)
            self.log.info("Documents combined successfully", count=len(doc_parts), session=self.session_id)
            return combined_text
        
        except Exception as e:
            self.log.error(f"Error combining documents, {e}")
            raise DocumentPortalException("Error combining documents", sys)
        

    def clean_old_sessions(self, keep_latest: int = 3):
        """
        Method to delete older session folders, keeping only latest int = n.
        """
        try:
            session_folders = sorted(
                [f for f in self.base_dir.iterdir() if f.is_dir()],
                reverse=True
            )
            for folder in session_folders[keep_latest:]:
                for file in folder.iterdir():
                    file.unlink()
                folder.rmdir()
                self.log.info("Old session folder deleted", path=str(folder))
                
        except Exception as e:
            self.log.error(f"Error deleting existing files, {e}")
            raise DocumentPortalException("Error occurred while deleting existing files", sys)