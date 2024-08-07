from fastapi import FastAPI
from src.main.routes.hello_router import helloRouter
from src.main.routes.document_router import documentRouter

app = FastAPI()

app.include_router(router=helloRouter)
app.include_router(router=documentRouter)
