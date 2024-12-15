from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.routes import courses

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(courses.router, prefix="/cursos", tags=["Cursos"])

@app.get("/")
def welcome_message():
    return "Welcome to the API"