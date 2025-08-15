import sys
import pandas as pd
from dotenv import load_dotenv
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from promptlib.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparatorLLM:
    """_summary_
    """

    def __init__(self):
        load_dotenv()
        self.log = CustomLogger().get_logger()
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROMPT_REGISTRY["compare_documents"]
        self.chain = self.prompt | self.llm | self.parser | self.fixing_parser

        self.log.info("DocumentComparatorLLM initialized with model and parser.")

    def compare_documents(self):
        """
        Compares two documents using a specified LLM model and returns a structured comparison.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error comparing documents, {e}")
            raise DocumentPortalException("Document comparison failed", sys)

    def _format_response(self):
        """
        Formats the response from the LLM into a structured format.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error formatting response into Dataframe, {e}")
            raise DocumentPortalException("Error formatting response", sys)