import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentAnalyzer:
    """
    Analyzes documents using a pre-trained model.
    Automatically logs all actions and supports session-based organization.
    """
    def __init__(self):
        pass
        # self.llm = ModelLoader().load_llm()
        # self.parser = JsonOutputParser()
        # self.fixing_parser = OutputFixingParser.from_llm(llm=self.llm, parser=self.parser)
        # self.log = CustomLogger().get_logger(__name__)

    def analyze_document(self):
        """
        Analyze the given document text using the LLM model.
        """
        pass
        # try:
        #     model = self.model_loader.load_model()
        #     # Assuming the model has a method 'analyze' to process the document
        #     analysis_result = model.analyze(document_path)
        # except Exception as e:
        #     raise DocumentPortalException("Error analyzing document", e) from e
    
