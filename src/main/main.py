from fastapi import FastAPI
from src.main.routes.hello_router import helloRouter
from src.main.routes.vector_store_router import vectorStoreRouter

app = FastAPI()

app.include_router(router=helloRouter)
app.include_router(router=vectorStoreRouter)
