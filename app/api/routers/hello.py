from fastapi import APIRouter

router = APIRouter()


@router.get("/hello", tags=["hello"])
async def hello():
    return {"message": "Hello World"}


@router.get("/hello/{name}", tags=["hello"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
