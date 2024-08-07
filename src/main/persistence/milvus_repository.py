from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents.base import Document


class MilvusRepository:
    def __init__(self) -> None:
        self.embeddings = OpenAIEmbeddings()

        self.vector_store = Milvus(
            embedding_function=self.embeddings,
            connection_args={"host": "localhost", "port": "19530"},
            collection_name="your_collection_name",
            auto_id=True,
        )

    def add_documents(self, documents: list[Document]) -> None:
        self.vector_store.add_documents(documents=documents)

    def similarity_search(self, query: str) -> list[Document]:
        return self.vector_store.similarity_search(query=query)
