from fastapi import APIRouter

helloRouter = APIRouter()


@helloRouter.get(path="/hello")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}
