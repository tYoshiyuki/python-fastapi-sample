""" Helloエンドポイントのモジュール """
from fastapi import APIRouter

router = APIRouter()


@router.get("/hello", tags=["hello"])
async def hello():
    """ 挨拶を返却する """
    return {"message": "Hello World"}


@router.get("/hello/{name}", tags=["hello"])
async def say_hello(name: str):
    """ 名前を指定した挨拶を返却する """
    return {"message": f"Hello {name}"}
