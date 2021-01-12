import uvicorn as uvicorn
from fastapi import FastAPI
from repositories import TextRepository
from pydantic import BaseModel


app = FastAPI()


class TextCreate(BaseModel):
    name: str
    content: str


@app.get("/")
def read_root():
    pass


@app.get("/texts")
def get_texts():
    return TextRepository.get_texts()


@app.post("/texts")
def create_text(text: TextCreate):
    TextRepository.insert_text(text.name, text.content)
    return {}


@app.get("/texts/{id}")
def get_text_by_id():
    pass

# @app.delete("/texts/{id}")
# def delete_text():
#     pass

# @app.put("/texts/{id}")
# def update_text():
#     pass

uvicorn.run(app, host="localhost", port=3000)