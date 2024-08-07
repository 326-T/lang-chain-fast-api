from typing import List
from fastapi import APIRouter
from langchain_core.documents.base import Document
from pydantic import BaseModel
from src.main.persistence.milvus import vector_store


class DocReq(BaseModel):
    source: str
    title: str
    content: str


class DocRes(BaseModel):
    page_content: str
    metadata: dict[str, str | int]


vectorStoreRouter = APIRouter()


@vectorStoreRouter.post(path="/document")
async def post(doc: DocReq) -> None:
    vector_store.add_documents(
        documents=[
            Document(
                page_content=doc.content,
                metadata={"source": doc.source, "title": doc.title},
            )
        ]
    )


@vectorStoreRouter.post(path="/document/bulk")
async def bulk(docs: List[DocReq]) -> None:
    vector_store.add_documents(
        documents=[
            Document(
                page_content=doc.content,
                metadata={"source": doc.source, "title": doc.title},
            )
            for doc in docs
        ]
    )


@vectorStoreRouter.get(path="/document")
async def index(query: str) -> List[DocRes]:
    results: List[Document] = vector_store.similarity_search(query=query)
    return [
        DocRes(page_content=doc.page_content, metadata=doc.metadata) for doc in results
    ]
