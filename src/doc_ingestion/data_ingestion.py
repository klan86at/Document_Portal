from __future__ import annotations

# Libraries
import os
import sys
import json
import uuid
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union, Dict, Any

import fitz  # cSpell:ignore fitz
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS  # cSpell:ignore vectorstores
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, Docx2txtLoader

from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

# from utils.file_io import _session_id, save_uploaded_files
# from utils.document_ops import load_documents, combine_documents, concat_for_analysis, concat_for_comparison



class FaissManager:  # cSpell:ignore Faiss
    def __init__(self):
        pass

    def _exists(self):
        pass
    
    @staticmethod
    def _fingerprint():
        pass
    def _save_meta(self):
        pass
    def add_documents(self):
        pass
    def _load_or_create(self):
        pass

class DocHandler:
    def __init__(self):
        pass
    def save_pdf(self):
        pass
    def read_pdf(self):
        pass


class DocumentComparator:
    def __init__(self):
        pass
    def save_uploaded_files(self):
        pass
    def read_pdf(self):
        pass
    def combine_documents(self):
        pass
    def clean_old_sessions(self):
        pass

class ChatIngestor:  # cSpell:ignore Ingestor
    def __init__(self):
        pass
    def _resolve_dir(self):
        pass
    def _split(self):
        pass
    def build_retriever(self):
        pass