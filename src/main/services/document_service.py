from langchain_core.documents.base import Document
from src.main.persistence.milvus_repository import MilvusRepository


class DocumentService:
    def __init__(self) -> None:
        self.milvus_repository = MilvusRepository()

    def add_documents(self, documents: list[Document]) -> None:
        self.milvus_repository.add_documents(documents=documents)

    def similarity_search(self, query: str) -> list[Document]:
        return self.milvus_repository.similarity_search(query=query)
