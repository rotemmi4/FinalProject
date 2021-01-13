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
    if (text[0]):
         response = Algorithem.getWeights(text[0],'random')

    db_response = [{
        "sentences": [
            {"sentenceNum": 1, "content": """While complaints about the 'miserly' generosity of the Bush Administration have surfaced in recent days, donations and actions at the grassroots level have quietly illustrated the concern and sympathy felt by ordinary Americans.
       """, "weight": 0.5},
            {"sentenceNum": 2, "content": """On Monday of this week, Jan Egeland, the UN's chief of emergency relief said that rich nations like the U.S. were being "stingy" by making small contributions. Egeland later recanted his statement, adding that America's contributions to Asia's tsunami relief was "one of the most generous pledges so far."
       """, "weight": 0.26},
            {"sentenceNum": 3, "content": """The Bush administration has pledged $350 million in aid for the relief effort. Critics have been quick to compare this to the $177 million spent every day in Iraq to conduct war in that country. In comparison, there was a $500 million pledge made recently by the government of Japan.
       """, "weight": 0.9},
            {"sentenceNum": 4, "content": """Independently of the government, individual Americans have been directly contributing money to aid organizations. Amazon.com placed a link for the American Red Cross, collecting more than $8 million from 100,000 people as of Friday, December 31st. 12,000 donors have donated over $1.2 million to the Red Cross through Yahoo.com.
       """, "weight": 0.35},
            {"sentenceNum": 5,
             "content": """Scores of International aid organizations are accepting donations for helping victims of the earthquake and tsunami. Many major companies including Apple Computer, Microsoft, Cisco, eBay, Google, and AOL are helping enable donations through the web.""",
             "weight": 0.8},
        ],
        "name": "Some Name"
    }]
    arrResponse =[]
    arrResponse.append(response)
    return arrResponse

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