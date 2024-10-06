from fastapi import FastAPI

from app.api.routers import hello

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
async def health_check():
    return {"message": "success."}
