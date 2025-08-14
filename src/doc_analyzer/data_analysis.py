from itertools import chain
import os
import sys
from urllib import response
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from promptlib.prompt_library import *

class DocumentAnalyzer:
    """
    Analyzes documents using a pre-trained model.
    Automatically logs all actions and supports session-based organization.
    """
    def __init__(self):
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()
            # Prepare parsers
            self.parser = JsonOutputParser(pydantic_object=Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(llm=self.llm, parser=self.parser)
        
            self.prompt = prompt

            self.log.info("DocumentAnalyzer initialized successfully.")
        
        except Exception as e:
            self.log.error(f"Error initializing DocumentAnalyzer: {e}")
            raise DocumentPortalException("Error initializing DocumentAnalyzer", sys)
        

    def analyze_document(self, document_text:str)-> dict:
        """
        Analyze the given document text using the LLM model.
        """
        try:
            chain = self.prompt | self.llm | self.fixing_parser

            self.log.info("Metadata analysis chain initialized")

            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "text": document_text
            })

            self.log.info("Metadata analysis completed", keys=list(response.keys()))

            return response
        
        except Exception as e:
            self.log.error("Error analyzing metadata", error=str(e))
            raise DocumentPortalException("Metadata extraction failed", e) from e
        
    
