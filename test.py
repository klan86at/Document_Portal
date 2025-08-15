import os
from pathlib import Path
from src.doc_analyzer.data_ingestion import DocumentHandler
from src.doc_analyzer.data_analysis import DocumentAnalyzer

# Path to the PDF you want to test
PDF_PATH = r"D:\\LLMOPs\\Document_Portal\\data\\doc_analysis\\AppliedAI_White_Paper_Retrieval-augmented-Generation-Realized_FINAL_20240618.pdf"

# Dummy file wraper to simulate upload file (Atreamli style)
class DummyFile:
        def __init__(self, file_path):
            self.name = Path(file_path).name
            self.file_path = file_path

        def getbuffer(self):
            return open(self.file_path, "rb").read()
        
def main():
    try:
        # ------ STEP 1: Data  Ingestion ------
        print("Starting PDF ingestion...")
        dummy_pdf = DummyFile(PDF_PATH)

        handler = DocumentHandler(session_id="test_ingestion_analysis")
        saved_path = handler.save_pdf(dummy_pdf)
        print(f"PDF saved at: {saved_path}")

        text_content = handler.read_pdf(saved_path)
        print(f"Extracted text length: {len(text_content)} chars\n")

        # ------ STEP 2: Data Analysis ------
        print("Starting metadata analysis...")
        analyzer = DocumentAnalyzer()
        analysis_result = analyzer.analyze_document(text_content)

        # ------ STEP 3: Data Storage ------
        print("\n=== METADATA ANALYSIS RESULT ===")
        for key, value in analysis_result.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    main()
