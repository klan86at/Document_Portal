# import os
# from pathlib import Path
# from src.doc_analyzer.data_ingestion import DocumentHandler
# from src.doc_analyzer.data_analysis import DocumentAnalyzer

# # Path to the PDF you want to test
# PDF_PATH = r"D:\\LLMOPs\\Document_Portal\\data\\doc_analysis\\AppliedAI_White_Paper_Retrieval-augmented-Generation-Realized_FINAL_20240618.pdf"

# # Dummy file wrapper to simulate upload file (Streamlit style)
# class DummyFile:
#         def __init__(self, file_path):
#             self.name = Path(file_path).name
#             self.file_path = file_path

#         def getbuffer(self):
#             return open(self.file_path, "rb").read()
        
# def main():
#     try:
#         # ------ STEP 1: Data  Ingestion ------
#         print("Starting PDF ingestion...")
#         dummy_pdf = DummyFile(PDF_PATH)

#         handler = DocumentHandler(session_id="test_ingestion_analysis")
#         saved_path = handler.save_pdf(dummy_pdf)
#         print(f"PDF saved at: {saved_path}")

#         text_content = handler.read_pdf(saved_path)
#         print(f"Extracted text length: {len(text_content)} chars\n")

#         # ------ STEP 2: Data Analysis ------
#         print("Starting metadata analysis...")
#         analyzer = DocumentAnalyzer()
#         analysis_result = analyzer.analyze_document(text_content)

#         # ------ STEP 3: Data Storage ------
#         print("\n=== METADATA ANALYSIS RESULT ===")
#         for key, value in analysis_result.items():
#             print(f"{key}: {value}")
#     except Exception as e:
#         print(f"Test failed: {e}")

# if __name__ == "__main__":
#     main()

import io 
from pathlib import Path
from src.doc_compare.data_ingestion import DocumentIngestion
from src.doc_compare.doc_comparator import DocumentComparatorLLM

def load_fake_uploaded_file(file_path: Path):
    return io.BytesIO(file_path.read_bytes())

# ------ Step 1: Save and combine PDFs ------
def test_compare_documents():
    # cSpell:ignore LLMOPs
    ref_path = Path(r"D:\LLMOPs\Document_Portal\data\doc_compare\Long_Report_V1.pdf")
    act_path = Path(r"D:\LLMOPs\Document_Portal\data\doc_compare\Long_Report_V2.pdf")

# Wrap them like streamlit UploadedFile- style
    class FakeUpload:
        def __init__(self, file_path: Path):
            self.name = file_path.name
            self._buffer = file_path.read_bytes()

        def getbuffer(self):  # cSpell:ignore getbuffer
            return self._buffer
        
    # Initiate
    comparator = DocumentIngestion()
    ref_upload = FakeUpload(ref_path)
    act_upload = FakeUpload(act_path)

    ref_file, act_file = comparator.save_uploaded_files(ref_upload, act_upload)
    combined_text = comparator.combine_documents()
    comparator.clean_old_sessions(keep_latest=3)

    print("\n Combine Text Preview (First 1000 chars): \n")
    print(combined_text[:1000])

    llm_comparator = DocumentComparatorLLM()
    comparison_df = llm_comparator.compare_documents(combined_text)

    print("\n=== COMPARISON RESULT ===")
    print(comparison_df.head(10))

if __name__ == "__main__":
    test_compare_documents()

    # comparator = DocumentComparator(session_id="test_compare_documents")
    # ref_path, act_path = comparator.save_uploaded_files(ref_file, act_file)
    # print(f"PDF saved at: {ref_path}, {act_path}")

    # # ------ STEP 2: Data Comparison ------
    # print("Starting document comparison...")
    # comparator_llm = DocumentComparatorLLM()
    # comparison_result = comparator_llm.compare_documents(comparator.read_pdf(ref_path))
    # print(f"Comparison result: {comparison_result}")
    # # Path to the PDF you want to test
    # PDF_PATH = r"D:\\LLMOPs\\Document_Portal\\data\\doc_compare\\reference\\AppliedAI_White_Paper_Retrieval-augmented-Generation-Realized_FINAL_20240618.pdf"
    # ACTUAL_PATH = r"D:\\LLMOPs\\Document_Portal\\data\\doc_compare\\actual\\AppliedAI_White_Paper_Retrieval-augmented-Generation-Realized_FINAL_20240618.pdf"
    # return PDF_PATH, ACTUAL_PATH