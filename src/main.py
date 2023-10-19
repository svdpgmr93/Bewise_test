from fastapi import FastAPI
from src.controller import get_tests
from src.models import Base
from src.base import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Bewice API"}


@app.post("/{questions_num}")
def find_tests(questions_num: int):
    return get_tests(questions_num)
