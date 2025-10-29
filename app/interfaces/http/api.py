from fastapi import FastAPI
from app.interfaces.http.routers import book_router, member_router

app = FastAPI()

app.include_router(book_router.router, prefix="/books", tags=["Books"])
app.include_router(member_router.router, prefix="/members", tags=["Members"])

@app.get("/")
def root():
    return {"message": "📚 Library Management API is running!"}
