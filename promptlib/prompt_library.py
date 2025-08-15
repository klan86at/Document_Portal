
# Prepare prompt template
from langchain_core.prompts import ChatPromptTemplate


doc_analysis_prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyze and summarize documents.
Return ONLY valid JSON matching the exact schema below.
{format_instructions}
                                          
Analyze this document: {document_text}
""")

doc_comparison_prompt = ChatPromptTemplate.from_template("""
You will be provided with the content from two PDFs. Your tasks are as follows:

1. Compare the content in two PDFs.
2. Identify the difference in PDF and note down the page number.
3. The output you provide must be page wise comparison content.
4. If any page do not have any change, mention as 'NO CHANGE'

Input documents:
                                                         
{combined_docs}
                                                         
Your response should follow this format:
                                                         
{format_instructions}
""")

PROMPT_REGISTRY = {"document_analysis": doc_analysis_prompt, "document_comparison": doc_comparison_prompt}