from typing import List
from fastapi import APIRouter, Depends
from langchain_core.documents.base import Document
from pydantic import BaseModel
from src.main.services.document_service import DocumentService


class DocReq(BaseModel):
    source: str
    title: str
    content: str


class DocRes(BaseModel):
    page_content: str
    metadata: dict[str, str | int]


documentRouter = APIRouter()


@documentRouter.post(path="/document")
async def post(
    doc: DocReq, service: DocumentService = Depends(dependency=DocumentService)
) -> None:
    service.add_documents(
        documents=[
            Document(
                page_content=doc.content,
                metadata={"source": doc.source, "title": doc.title},
            )
        ]
    )


@documentRouter.post(path="/document/bulk")
async def bulk(
    docs: List[DocReq], service: DocumentService = Depends(dependency=DocumentService)
) -> None:
    service.add_documents(
        documents=[
            Document(
                page_content=doc.content,
                metadata={"source": doc.source, "title": doc.title},
            )
            for doc in docs
        ]
    )


@documentRouter.get(path="/document")
async def index(
    query: str, service: DocumentService = Depends(dependency=DocumentService)
) -> List[DocRes]:
    results: List[Document] = service.similarity_search(query=query)
    return [
        DocRes(page_content=doc.page_content, metadata=doc.metadata) for doc in results
    ]
