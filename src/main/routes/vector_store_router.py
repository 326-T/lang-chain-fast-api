from typing import List
from fastapi import APIRouter
from langchain_core.documents.base import Document
from pydantic import BaseModel
from src.main.persistence.milvus import vector_store


class Item(BaseModel):
    source: str
    title: str
    content: str


vectorStoreRouter = APIRouter()


@vectorStoreRouter.post(path="/vector")
async def read_root(item: Item) -> None:
    vector_store.add_documents(
        documents=[
            Document(
                page_content=item.content,
                metadata={"source": item.source, "title": item.title},
            )
        ]
    )


@vectorStoreRouter.get(path="/vector")
async def read_root(query: str):
    results: List[Document] = vector_store.similarity_search(query=query)
    return {
        "results": [
            {"page_content": doc.page_content, "metadata": doc.metadata}
            for doc in results
        ]
    }
