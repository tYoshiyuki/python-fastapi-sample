from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.routers import hello, hero

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startup event")
    yield
    print("shutdown event")    

app = FastAPI(lifespan=lifespan)

app.include_router(hello.router)
app.include_router(hero.router)

@app.get("/")
async def health_check():
    return {"message": "success."}
