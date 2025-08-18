# Import Libraries
import os
import sys
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS  # cSpell:ignore vectorstores

from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from promptlib.prompt_library import PROMPT_REGISTRY  # cSpell:ignore promptlib
from model.models import PromptType

class ConversationalRAG:
    def __init__(self, session_id: str, retriever=None):
        try:
            self.log = CustomLogger().get_logger(__name__)
            self.session_id = session_id
            self.llm = self._load_llm()
            self.contextualize_prompt: ChatPromptTemplate = PROMPT_REGISTRY[PromptType.CONTEXTUALIZE_QUESTION.value]
            self.qa_prompt: ChatPromptTemplate = PROMPT_REGISTRY[PromptType.CONTEXT_QA.value]
            if retriever is None:
                raise ValueError("Retriever cannot None")
            self.retriever = retriever
            self._build_lcel_chain()
            self.log.info("ConversationalRAG initialized", session_id=self.session_id)
        except Exception as e:
            self.log.error("Failed to initialize ConversationalRAG", error=str(e))
            raise DocumentPortalException("Initialization error in ConversationalRAG", sys)
        

    def load_retriever_from_faiss(self, index_path: str):  # cSpell:ignore faiss
        """
        Load a FAISS vectorstore from disk and convert to retriever
        """
        try:
            embeddings = ModelLoader().load_embeddings()
            if not os.path.isdir(index_path):
                raise FileNotFoundError(f"FAISS index directory not found: {index_path}")
            
            vectorstore = FAISS.load_local(  # cSpell:ignore vectorstore
                index_path,
                embeddings,
                allow_dangerous_deserialization=True
            )

            self.retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
            self.log.info("FAISS index loaded successfully", index_path=index_path, session_id=self.session_id)

            self._build_lcel_chain()
            return self.retriever
        except Exception as e:
            self.log.error("Failed to load FAISS index", error=str(e))
            raise DocumentPortalException("FAISS index loading error in ConversationalRAG", sys)

    def invoke(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to invoke ConversationalRAG", error=str(e))
            raise DocumentPortalException("Invocation error in ConversationalRAG", sys)

    def _load_llm(self):
        try:
            pass
        except Exception as e:
            self.log.error("Failed to load LLM", error=str(e))
            raise DocumentPortalException("LLM loading error in ConversationalRAG", sys)

    @staticmethod
    def _format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)
    
    def _build_lcel_chain(self):  # cSpell:ignore lcel
            try:

                question_rewriter = (
                    {"input": itemgetter("input"), "chat_history": itemgetter("chat_history")}
                    | self.contextualize_prompt  # type: ignore
                    | self.llm  
                    | StrOutputParser()
                )
                retrieve_docs = question_rewriter| self.retriever | self._format_docs
                self.chain = (
                    {
                        "context": retrieve_docs,
                        "input": itemgetter("input"),
                        "chat_history": itemgetter("chat_history"),
                    }
                    | self.qa_prompt  # type: ignore
                    | self.llm  # type: ignore
                    | StrOutputParser() 
                )
                self.log.info("LCEL chain built successfully", session_id=self.session_id)
            except Exception as e:
                self.log.error("Failed to build LCEL chain", error=str(e))
                raise DocumentPortalException("LCEL chain building error in ConversationalRAG", sys)