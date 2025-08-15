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
        pass

    def compare_documents(self):
        """
        Compares two documents using a specified LLM model and returns a structured comparison.
        """
        pass

    def _format_response(self):
        """
        Formats the response from the LLM into a structured format.
        """
        pass
