import sys
import pandas as pd
from dotenv import load_dotenv # cSpell:ignore dotenv
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from promptlib.prompt_library import PROMPT_REGISTRY  # cSpell:ignore promptlib
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
        self.prompt = PROMPT_REGISTRY["document_comparison"]
        self.chain = self.prompt | self.llm | self.parser 

        self.log.info("DocumentComparatorLLM initialized with model and parser.")

    def compare_documents(self, combined_docs: str) -> pd.DataFrame:
        """
        Compares two documents using a specified LLM model and returns a structured comparison.
        """
        try:
            inputs = {
                "combined_docs": combined_docs,
                "format_instructions": self.parser.get_format_instructions()
            }
            self.log.info("Starting document comparison", inputs=inputs)
            response = self.chain.invoke(inputs)
            self.log.info("Document comparison completed", response=response)
            return self._format_response(response)

        except Exception as e:
            self.log.error(f"Error comparing documents, {e}")
            raise DocumentPortalException("Document comparison failed", sys)

    def _format_response(self, response_parsed: list[dict]) -> pd.DataFrame: #type: ignore
        """
        Formats the response from the LLM into a structured format.
        """
        try:
            df = pd.DataFrame(response_parsed)
            self.log.info("Response formatted into Dataframe", dataframe=df)
            return df
        except Exception as e:
            self.log.error(f"Error formatting response into Dataframe, {e}")
            raise DocumentPortalException("Error formatting response", sys)