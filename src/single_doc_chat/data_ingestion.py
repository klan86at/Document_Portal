# Libraries
import uuid
import sys
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langsmith import expect  # cSpell:ignore FAISS vectorstores
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader

class SingleDocIngestor:  # cSpell:ignore Ingestor
    def __init__(self):
        try:
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Failed to initialize SingleDocIngestor", error=str(e))
            raise DocumentPortalException("Initialized error in SingleDocIngestor", sys)
        
    def ingest_files(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to ingest files", error=str(e))
            raise DocumentPortalException("Failed to ingest files", sys)
        
    def _create_retriever(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to create retriever", error=str(e))
            raise DocumentPortalException("Error occurred while creating retriever", sys)