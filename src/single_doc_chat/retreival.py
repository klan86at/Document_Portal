import sys
import os
from dotenv import load_dotenv  # cSpell:ignore dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.vectorstores import FAISS  # cSpell:ignore vectorstores FAISS
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from requests import session
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from promptlib.prompt_library import PROMPT_REGISTRY  # cSpell:ignore promptlib
from model.models import PromptType


class ConversationalRAG:
    def __init__(self) -> None:
        try:
            self.log = CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Error in initializing ConversationalRAG", error=str(e))
            raise DocumentPortalException("Initialized error in ConversationalRAG", sys)
        
    def _load_llm(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error in loading LLM", error=str(e))
            raise DocumentPortalException("Error in loading LLM", sys)
        
    def _get_session_history(self, session_id: str):
        try:
            pass
        except Exception as e:
            self.log.error("Error in getting session history", session=session_id, error=str(e))
            raise DocumentPortalException("Error in getting session history", sys)
        
    def load_retriever_from_faiss(self, faiss_db_path: str):
        try:
            pass
        except Exception as e:
            self.log.error("Error in loading retriever from FAISS", error=str(e))
            raise DocumentPortalException("Error in loading retriever from FAISS", sys)
        
    def invoke(self):
        try:
            pass
        except Exception as e:
            self.log.error("Error in invoking ConversationalRAG", error=str(e))
            raise DocumentPortalException("Failed to invoke RAG chain", sys)