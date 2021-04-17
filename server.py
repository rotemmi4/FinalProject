import random

import uvicorn as uvicorn
from fastapi.middleware.cors import CORSMiddleware

from repositories import TextRepository, VisualizationPropertiesRepository, QuestionRepository, AnswerRepository, \
    TestTypeRepository
from pydantic import BaseModel
from repositories import TextRepository, VisualizationPropertiesRepository, StudentRepository
from pydantic import BaseModel, Field
import jwt
from algorithems import RandomAlgorithem

from typing import Optional

from fastapi import FastAPI, Header

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

class TextDelete(BaseModel):
    id: str

class TextVisu(BaseModel):
    testName: str
    textID: int
    visualizationType: str
    propName: str
    propVal: str
    propType: str
class TestType(BaseModel):
    testName:str
    testType: str
class UserLogin(BaseModel):
    username: str
    password: str

class QuestionCreate(BaseModel):
    text_id: str
    question_content: str
    answer1_isCorrect: str
    answer1_content: str
    answer2_isCorrect: str
    answer2_content: str
    answer3_isCorrect: str
    answer3_content: str
    answer4_isCorrect: str
    answer4_content: str

class AnswersCreate(BaseModel):
    option_id: int
    question_id: str
    text_id: str
    is_correct: str
    answer_content: str

class QuestionDelete(BaseModel):
    id: str


class StudentInfo(BaseModel):
    studentID: int
    studentAge: int
    studentGender: str



@app.get("/")
def read_root():
    pass


@app.get("/texts")
def get_texts():
    return TextRepository.get_texts()


@app.get("/questionId")
def get_question_id():
    return QuestionRepository.get_max_question_id()


@app.post("/uploadText")
def add_text(text : TextCreate):
    name = text.name
    content = text.content
    return TextRepository.insert_text(name, content)

@app.get("/texts/{id}")
def get_text_by_id():
    pass

@app.post("/saveVisu")
def save(visu: TextVisu):
    VisualizationPropertiesRepository.insert_visualization_properties(visu)


@app.post("/saveTest")
def saveTest(testType: TestType):
    TestTypeRepository.save_new_test(testType.testName, "\"" + testType.testType + "\"")


@app.post("/deleteText")
def delete_text(textId: TextDelete):
    return TextRepository.delete_text(textId.id)


@app.post("/deleteText")
def delete_text(textId : TextDelete):
    return TextRepository.delete_text(textId.id)

@app.post("/addQuestion")
def add_question(question : QuestionCreate):
    QuestionRepository.insert_question(question.text_id, question.question_content)
    queId= QuestionRepository.get_max_question_id()
    AnswerRepository.insert_answer(1, queId[0]['queId'], question.text_id, question.answer1_isCorrect,
                                   question.answer1_content)
    AnswerRepository.insert_answer(2, queId[0]['queId'], question.text_id, question.answer2_isCorrect,
                                   question.answer2_content)
    AnswerRepository.insert_answer(3, queId[0]['queId'], question.text_id, question.answer3_isCorrect,
                                   question.answer3_content)
    AnswerRepository.insert_answer(4, queId[0]['queId'], question.text_id, question.answer4_isCorrect,
                                   question.answer4_content)
    pass
#ddd
# @app.post("/addAnswers")
# def add_answers(answer : AnswersCreate):
#     return AnswerRepository.insert_answer(answer.option_id, answer.question_id, answer.text_id, answer.is_correct, answer.answer_content)

@app.post("/deleteQuestion")
def delete_question(que_id : QuestionDelete):
    return QuestionRepository.delete_question(que_id.id)

@app.get("/texts/{id}/weights")
def get_text_weights(id: int):
    text = TextRepository.get_text_by_id(id)
    response= {}
    if (text):
        response = RandomAlgorithem.getWeights(text[0],'random')
#         response = AlgorithemFactory.get('random').getWeight(text[0])
    arrResponse =[]
    if(response):
        arrResponse.append(response)
    return arrResponse

@app.get("/getRandom")
def get_random_texts():
    return TextRepository.get_random_text(12)
@app.get("/getRandomTextAndVisualization")
def get_random_texts_and_visualization():
    return TextRepository.get_random_text_and_visualizations(12)

@app.get("/questions/{id}")
def get_questions_by_id(id: int):
    question = QuestionRepository.get_questions_by_id(id)
    print(question)
    return question

@app.post("/auth/login")
def login(user_data: UserLogin):
    if (user_data.username == admin_user and user_data.password == admin_password):
        payload = {'username': user_data.username, 'admin': True};
        encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
        response = {
                    'token': encoded_jwt,
                     'user': { 'username': user_data.username }
                     }

        return response
    pass

@app.get("/private/user/get")
def getLoginUser(x_auth_token: Optional[str] = Header(None)):
    decoded_data = jwt.decode(x_auth_token, secret, algorithms=["HS256"])
    response = {'username': decoded_data['username']}

    return response
    pass





# Roman
@app.post("/student/set_info")
def set_info_student(student_info: StudentInfo):
    studentID = student_info.studentID
    studentAge = student_info.studentAge
    studentGender = student_info.studentGender
    return StudentRepository.insert_info(studentID, studentAge, studentGender)
    # pass

@app.get("/student/get_test_id")
def get_test_id():
    all_test = StudentRepository.get_test_ids()
    d = {}
    for dict in all_test:
        for test_name in dict.values():
            d[test_name] = 0
    test_id = random.choice(list(d))
    return test_id


@app.get("/student/get_questions/{text_id}")
def get_questions_by_text_id(text_id: int):
    all_questions = StudentRepository.get_questions_by_text_id(text_id)
    for question in all_questions:
        question_id = question["question_id"]
        # question_content = question["question_content"]
        all_answers = StudentRepository.get_all_answers_by_question_id(question_id)
        # add the list of answers to the question
        question["answer_options"] = all_answers

    return all_questions


@app.post("/student/set_question_results")
def get_questions_by_text_id(results: list):
    return StudentRepository.insert_question_results(results)


@app.get("/text/get_visualization/{text_id}")
def get_visualiztion_by_id(text_id: int):
    visualization = VisualizationPropertiesRepository.get_visualiztion_by_id(text_id)
    if len(visualization) > 0:
        if (visualization[0]["type"] == "WithoutVisualization"):
            return "Without Visualization"
        elif (visualization[0]["type"] == "Highlight"):
            return "Highlight"
        elif (visualization[0]["type"] == "GradualHighlight"):
            return "Gradual Highlight"
        elif (visualization[0]["type"] == "IncreasedFont"):
            return "Increased Font"
        elif (visualization[0]["type"] == "GradualFont"):
            return "Gradual Font"
        elif (visualization[0]["type"] == "SummaryOnly"):
            return "Summary Only"
    return "Without Visualization"


@app.get("/student/get_texts_by_testid/{test_id}")
def get_texts_by_test_id(test_id: str):
    text_ids = StudentRepository.get_texts_by_test_id(test_id)
    return text_ids

@app.get("/student/get_type_by_text_id/{text_id}")
def get_texts_by_test_id(text_id: int):
    text_type_id = StudentRepository.get_type_by_text_id(text_id)
    text_type_id = text_type_id[0]["visualiztion_id"]
    visualization = VisualizationPropertiesRepository.get_visualiztion_by_id(text_type_id)
    if len(visualization) > 0:
        if (visualization[0]["type"] == "WithoutVisualization"):
            return "Without Visualization"
        elif (visualization[0]["type"] == "Highlight"):
            return "Highlight"
        elif (visualization[0]["type"] == "GradualHighlight"):
            return "Gradual Highlight"
        elif (visualization[0]["type"] == "IncreasedFont"):
            return "Increased Font"
        elif (visualization[0]["type"] == "GradualFont"):
            return "Gradual Font"
        elif (visualization[0]["type"] == "SummaryOnly"):
            return "Summary Only"
    return "Without Visualization"


@app.get("/texts/{text_id}/all_info")
def get_text_total_info(text_id: int):
    text = TextRepository.get_text_by_id(text_id)
    response = {}
    if text:
        response = RandomAlgorithem.getWeights(text[0], 'random')
#         response = AlgorithemFactory.get('random').getWeight(text[0])
    arrResponse = []
    if response:
        arrResponse.append(response)
    text_type = get_texts_by_test_id(text_id)
    arrResponse[0]["type"] = text_type
    # print("here?")
    return arrResponse

uvicorn.run(app, host="localhost", port=5000)
# @app.delete("/texts/{id}")
# def delete_text():
#     pass

# @app.put("/texts/{id}")
# def update_text():
#     pass

# uvicorn.run(app, host="localhost", port=3000)