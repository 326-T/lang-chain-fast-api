from typing import List
from fastapi import APIRouter
from langchain_core.documents.base import Document
from pydantic import BaseModel
from src.main.persistence.milvus import vector_store


class Item(BaseModel):
    text: str


vectorStoreRouter = APIRouter()


@vectorStoreRouter.post(path="/vector")
async def read_root(item: Item) -> dict[str, str]:
    vector_store.add_texts(texts=[item.text])
    return {"text": item.text}


@vectorStoreRouter.get(path="/vector")
async def read_root(query: str) -> dict[str, str]:
    results: List[Document] = vector_store.similarity_search(query=query)
    print(results)
    return {"results": results[0].page_content}
