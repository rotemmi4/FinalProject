import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import Algorithem
from repositories import TextRepository
from pydantic import BaseModel
import jwt
import json



admin_user = 'admin'
admin_password = 'admin'
secret = 'Mr.Awesome'

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextCreate(BaseModel):
    name: str
    content: str

class UserLogin(BaseModel):
    username: str
    password: str

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


@app.get("/texts/{id}/weights")
def get_text_weights(id: int):
    text = TextRepository.get_text_by_id(id)
    if (text):
         response = Algorithem.getWeights(text,'random')
    return response

@app.get("/auth/login")
def login(user_data: UserLogin):
    if (user_data.username == admin_user and user_data.password == admin_password):
        payload = {'username': user_data.username, 'admin': True};
        encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
        return encoded_jwt
    pass

uvicorn.run(app, host="localhost", port=5000)
# @app.delete("/texts/{id}")
# def delete_text():
#     pass

# @app.put("/texts/{id}")
# def update_text():
#     pass

uvicorn.run(app, host="localhost", port=3000)