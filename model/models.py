from ctypes import Union
from annotated_types import T
from langchain_text_splitters import Language
from pydantic import BaseModel, Field, RootModel
from typing import Optional, List, Dict, Any, Union
from zmq import Enum


class Metadata(BaseModel):
    Summary: List[str] = Field(default_factory=list, description="A list of summary points extracted from the document.")
    """
    Represents the metadata associated with a document.
    """
    Title: Optional[str] = Field(None, description="The title of the document.")
    Author: Optional[str] = Field(None, description="The author of the document.")
    DateCreated: Optional[str] = Field(None, description="The creation date of the document.")
    LastModifiedDate: Optional[str] = Field(None, description="The last modification date of the document.")
    Publisher: Optional[List[str]] = Field(None, description="The publisher of the document.")
    Language: Optional[str] = Field(None, description="The language of the document.")
    PageCount: Union[int, str] = Field(..., description="The number of pages in the document.")
    SentimentTone: str = Field(..., description="The sentiment tone of the document.")

class ChangeFormat(BaseModel):
    Page: str
    Changes: str

class SummaryResponse(RootModel[list[ChangeFormat]]):
    pass

class PromptType(str, Enum):
    DOCUMENT_ANALYSIS = "doc_analysis"
    DOCUMENT_COMPARISON = "doc_comparison"
    CONTEXTUALIZE_QUESTION = "contextualize_question"
    CONTEXT_QA = "context_qa"