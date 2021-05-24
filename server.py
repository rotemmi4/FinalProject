import random

import uvicorn as uvicorn
from fastapi.middleware.cors import CORSMiddleware
#from more_itertools import take

from repositories import TextRepository, VisualizationPropertiesRepository, QuestionRepository, AnswerRepository, \
    TestTypeRepository, RankRepository
from pydantic import BaseModel
from repositories import TextRepository, VisualizationPropertiesRepository, StudentRepository, StudentAnswersRepository
from pydantic import BaseModel, Field
import jwt
from algorithems import RandomAlgorithem, TextRankAlgorithem

from typing import Optional

from fastapi import FastAPI, Header

admin_user = 'admin'
admin_password = 'admin'
secret = 'Mr.Awesome'

app = FastAPI()
#dfg
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
    threshold: float
    setNum: int
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
    studentName: str

class RankCreate(BaseModel):
    student_id: int
    withoutVisualization: int
    gradualHighlight: int
    highlight: int
    increasedFont: int
    gradualFont: int
    summaryOnly: int
    textId: str

class RankUpdate(BaseModel):
    student_id: int
    WithoutVisualization_place: str
    highlight_place: str
    increasedFont_place: str
    summaryOnly_place: str
    gradualHighlight_place: str
    gradualFont_place: str

class QuestionResult(BaseModel):
    answer: bool
    question_id: int
    student_id: str
    test_name: str
    time: float

class StudentSummary(BaseModel):
    student_id: int
    text_id: str
    summary: str
    readingTime: float
    summaryTime: float


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


@app.get("/tests/getAllTests")
def get_all_tests():
    return TestTypeRepository.get_all_tests()

@app.post("/deleteText")
def delete_text(textId: TextDelete):
    return TextRepository.delete_text(textId.id)



@app.post("/tests/deleteTest/{name}")
def delete_test_by_name(name: str):
    TestTypeRepository.delete_test_by_name(name)

@app.post("/tests/deleteTestProperties/{name}")
def delete_test_by_name(name: str):

    VisualizationPropertiesRepository.delete_test_properties(name)


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

        # response1 = RandomAlgorithem.getWeights(text[0],'random')
        # print("#######################################################################")
        response = TextRankAlgorithem.textRank_algorithm(text[0])
#         response = AlgorithemFactory.get('random').getWeight(text[0])
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     arrResponse1 =[]
#     if(response1):
#         arrResponse1.append(response1)
#         print(response1)
    arrResponse =[]
    if(response):
        arrResponse.append(response)
        # print(response)
    return arrResponse

@app.get("/getRandom")
def get_random_texts():
    return TextRepository.get_random_text(18)
@app.get("/getRandomTextAndVisualization")
def get_random_texts_and_visualization():
    return TextRepository.get_random_text_and_visualizations(18)

@app.get("/questions/{id}")
def get_questions_by_id(id: int):
    question = QuestionRepository.get_questions_by_id(id)
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


@app.post("/student/set_info")
def set_info_student(student_info: StudentInfo):
    studentID = student_info.studentID
    studentAge = student_info.studentAge
    studentGender = student_info.studentGender
    studentName = student_info.studentName
    return StudentRepository.insert_info(studentID, studentAge, studentGender, studentName)
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
def get_questions_by_text_id(questionResult: QuestionResult):
    return StudentRepository.insert_question_results(questionResult)


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
    random.shuffle(text_ids)
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
    # print("text -> ", text)
    response = {}
    if text:
        # response = RandomAlgorithem.getWeights(text[0], 'random')
        response = TextRepository.get_text_weight(text_id)
        # print("response -> ",response)
#         response = AlgorithemFactory.get('random').getWeight(text[0])
    arrResponse = []
    if response:
        arrResponse.append(response)
    text_type = get_texts_by_test_id(text_id)
    # print("arrResponse -> ", arrResponse)
    arrResponse = arrResponse[0]
    # print("arrResponse -> ", arrResponse)
    # print("text_type -> ", text_type)
    arrResponse[0]["type"] = text_type
    # print(text_type)
    return arrResponse

@app.get("/sumResults/{test_name}")
def get_answer_by_test_name_SUM(test_name: str):
    res = []
    if test_name != None :
        res_set1_1 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "WithoutVisualization", 1)
        res_set1_2 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualHighlight", 1)
        res_set1_3 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "Highlight", 1)
        res_set1_4 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "IncreasedFont", 1)
        res_set1_5 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualFont", 1)
        res_set1_6 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "SummaryOnly", 1)
        res_set2_1 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "WithoutVisualization", 2)
        res_set2_2 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualHighlight", 2)
        res_set2_3 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "Highlight", 2)
        res_set2_4 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "IncreasedFont", 2)
        res_set2_5 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualFont", 2)
        res_set2_6 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "SummaryOnly", 2)
        res_set3_1 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "WithoutVisualization", 3)
        res_set3_2 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualHighlight", 3)
        res_set3_3 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "Highlight", 3)
        res_set3_4 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "IncreasedFont", 3)
        res_set3_5 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "GradualFont", 3)
        res_set3_6 = StudentAnswersRepository.get_answer_by_test_name_SUM("\'" + test_name + "\'", "SummaryOnly", 3)
        for i in range(len(res_set1_1)):
            dic={}
            dic['studentID'] = res_set1_1[i]['studentID']
            dic['studentAge'] = res_set1_1[i]['studentAge']
            dic['studentGender'] = res_set1_1[i]['studentGender']
            if len(res_set1_1) > 0:
                dic['Without Visualization_set1'] = res_set1_1[i]['SUM(time_to_answer)']
            if len(res_set2_1) > 0:
                dic['Without Visualization_set2'] = res_set2_1[i]['SUM(time_to_answer)']
            if len(res_set3_1) > 0:
                dic['Without Visualization_set3'] = res_set3_1[i]['SUM(time_to_answer)']
            if len(res_set1_2) > 0:
                dic['Gradual Highlight_set1'] = res_set1_2[i]['SUM(time_to_answer)']
            if len(res_set2_2) > 0:
                dic['Gradual Highlight_set2'] = res_set2_2[i]['SUM(time_to_answer)']
            if len(res_set3_2) > 0:
                dic['Gradual Highlight_set3'] = res_set3_2[i]['SUM(time_to_answer)']
            if len(res_set1_3) > 0:
                dic['Highlight_set1'] = res_set1_3[i]['SUM(time_to_answer)']
            if len(res_set2_3) > 0:
                dic['Highlight_set2'] = res_set2_3[i]['SUM(time_to_answer)']
            if len(res_set3_3) > 0:
                dic['Highlight_set3'] = res_set3_3[i]['SUM(time_to_answer)']
            if len(res_set1_4) > 0:
                dic['Increased Font_set1'] = res_set1_4[i]['SUM(time_to_answer)']
            if len(res_set2_4) > 0:
                dic['Increased Font_set2'] = res_set2_4[i]['SUM(time_to_answer)']
            if len(res_set3_4) > 0:
                dic['Increased Font_set3'] = res_set3_4[i]['SUM(time_to_answer)']
            if len(res_set1_5) > 0:
                dic['Gradual Font_set1'] = res_set1_5[i]['SUM(time_to_answer)']
            if len(res_set2_5) > 0:
                dic['Gradual Font_set2'] = res_set2_5[i]['SUM(time_to_answer)']
            if len(res_set3_5) > 0:
                dic['Gradual Font_set3'] = res_set3_5[i]['SUM(time_to_answer)']
            if len(res_set1_6) > 0:
                dic['Summary Only_set1'] = res_set1_6[i]['SUM(time_to_answer)']
            if len(res_set2_6) > 0:
                dic['Summary Only_set2'] = res_set2_6[i]['SUM(time_to_answer)']
            if len(res_set3_6) > 0:
                dic['Summary Only_set3'] = res_set3_6[i]['SUM(time_to_answer)']
            res.append(dic)
        # print(res)
        return res

@app.get("/countResults/{test_name}")
def get_answer_by_test_name_COUNT(test_name: str):
    res = []
    if test_name != None:
        res_set1_1 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "WithoutVisualization", 1)
        res_set1_2 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualHighlight", 1)
        res_set1_3 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "Highlight", 1)
        res_set1_4 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "IncreasedFont", 1)
        res_set1_5 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualFont", 1)
        res_set1_6 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "SummaryOnly", 1)
        res_set2_1 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "WithoutVisualization", 2)
        res_set2_2 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualHighlight", 2)
        res_set2_3 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "Highlight", 2)
        res_set2_4 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "IncreasedFont", 2)
        res_set2_5 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualFont", 2)
        res_set2_6 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "SummaryOnly", 2)
        res_set3_1 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "WithoutVisualization", 3)
        res_set3_2 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualHighlight", 3)
        res_set3_3 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "Highlight", 3)
        res_set3_4 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "IncreasedFont", 3)
        res_set3_5 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "GradualFont", 3)
        res_set3_6 = StudentAnswersRepository.get_answer_by_test_name_COUNT("\'" + test_name + "\'", "SummaryOnly", 3)
        # for i in range(len(res_set1_1)or len(res_set1_2)or len(res_set1_3)or len(res_set1_4)or len(res_set1_5)or len(res_set1_6)or len(res_set2_1)or len(res_set2_2)or len(res_set2_3)or len(res_set2_4)or len(res_set2_5)or len(res_set2_6)or len(res_set3_1)or len(res_set3_2)or len(res_set3_3)or len(res_set3_4)or len(res_set3_5)or len(res_set3_6)):
        res_len= StudentAnswersRepository.correct_answers_count("\'" + test_name + "\'")
        for i in range(res_len[0]['COUNT(is_correct)']):
            dic = {}
            if len(res_set1_1) > 0 and i<len(res_set1_1):
                dic['studentID'] = res_set1_1[i]['studentID']
                dic['studentAge'] = res_set1_1[i]['studentAge']
                dic['studentGender'] = res_set1_1[i]['studentGender']
                dic['Without Visualization_set1'] = res_set1_1[i]['COUNT(is_correct)*1.25']
            if len(res_set2_1) > 0 and i<len(res_set2_1):
                dic['studentID'] = res_set2_1[i]['studentID']
                dic['studentAge'] = res_set2_1[i]['studentAge']
                dic['studentGender'] = res_set2_1[i]['studentGender']
                dic['Without Visualization_set2'] = res_set2_1[i]['COUNT(is_correct)*1.25']
            if len(res_set3_1) > 0 and i<len(res_set3_1):
                dic['studentID'] = res_set3_1[i]['studentID']
                dic['studentAge'] = res_set3_1[i]['studentAge']
                dic['studentGender'] = res_set3_1[i]['studentGender']
                dic['Without Visualization_set3'] = res_set3_1[i]['COUNT(is_correct)*1.25']
            if len(res_set1_2) > 0 and i<len(res_set1_2):
                dic['studentID'] = res_set1_2[i]['studentID']
                dic['studentAge'] = res_set1_2[i]['studentAge']
                dic['studentGender'] = res_set1_2[i]['studentGender']
                dic['Gradual Highlight_set1'] = res_set1_2[i]['COUNT(is_correct)*1.25']
            if len(res_set2_2) > 0 and i<len(res_set2_2):
                dic['studentID'] = res_set2_2[i]['studentID']
                dic['studentAge'] = res_set2_2[i]['studentAge']
                dic['studentGender'] = res_set2_2[i]['studentGender']
                dic['Gradual Highlight_set2'] = res_set2_2[i]['COUNT(is_correct)*1.25']
            if len(res_set3_2) > 0 and i<len(res_set3_2):
                dic['studentID'] = res_set3_2[i]['studentID']
                dic['studentAge'] = res_set3_2[i]['studentAge']
                dic['studentGender'] = res_set3_2[i]['studentGender']
                dic['Gradual Highlight_set3'] = res_set3_2[i]['COUNT(is_correct)*1.25']
            if len(res_set1_3) > 0 and i<len(res_set1_3):
                dic['studentID'] = res_set1_3[i]['studentID']
                dic['studentAge'] = res_set1_3[i]['studentAge']
                dic['studentGender'] = res_set1_3[i]['studentGender']
                dic['Highlight_set1'] = res_set1_3[i]['COUNT(is_correct)*1.25']
            if len(res_set2_3) > 0 and i<len(res_set2_3):
                dic['studentID'] = res_set2_3[i]['studentID']
                dic['studentAge'] = res_set2_3[i]['studentAge']
                dic['studentGender'] = res_set2_3[i]['studentGender']
                dic['Highlight_set2'] = res_set2_3[i]['COUNT(is_correct)*1.25']
            if len(res_set3_3) > 0 and i<len(res_set3_3):
                dic['studentID'] = res_set3_3[i]['studentID']
                dic['studentAge'] = res_set3_3[i]['studentAge']
                dic['studentGender'] = res_set3_3[i]['studentGender']
                dic['Highlight_set3'] = res_set3_3[i]['COUNT(is_correct)*1.25']
            if len(res_set1_4) > 0 and i<len(res_set1_4):
                dic['studentID'] = res_set1_4[i]['studentID']
                dic['studentAge'] = res_set1_4[i]['studentAge']
                dic['studentGender'] = res_set1_4[i]['studentGender']
                dic['Increased Font_set1'] = res_set1_4[i]['COUNT(is_correct)*1.25']
            if len(res_set2_4) > 0 and i<len(res_set2_4):
                dic['studentID'] = res_set2_4[i]['studentID']
                dic['studentAge'] = res_set2_4[i]['studentAge']
                dic['studentGender'] = res_set2_4[i]['studentGender']
                dic['Increased Font_set2'] = res_set2_4[i]['COUNT(is_correct)*1.25']
            if len(res_set3_4) > 0 and i<len(res_set3_4):
                dic['studentID'] = res_set3_4[i]['studentID']
                dic['studentAge'] = res_set3_4[i]['studentAge']
                dic['studentGender'] = res_set3_4[i]['studentGender']
                dic['Increased Font_set3'] = res_set3_4[i]['COUNT(is_correct)*1.25']
            if len(res_set1_5) > 0 and i<len(res_set1_5):
                dic['studentID'] = res_set1_5[i]['studentID']
                dic['studentAge'] = res_set1_5[i]['studentAge']
                dic['studentGender'] = res_set1_5[i]['studentGender']
                dic['Gradual Font_set1'] = res_set1_5[i]['COUNT(is_correct)*1.25']
            if len(res_set2_5) > 0 and i<len(res_set2_5):
                dic['studentID'] = res_set2_5[i]['studentID']
                dic['studentAge'] = res_set2_5[i]['studentAge']
                dic['studentGender'] = res_set2_5[i]['studentGender']
                dic['Gradual Font_set2'] = res_set2_5[i]['COUNT(is_correct)*1.25']
            if len(res_set3_5) > 0 and i<len(res_set3_5):
                dic['studentID'] = res_set3_5[i]['studentID']
                dic['studentAge'] = res_set3_5[i]['studentAge']
                dic['studentGender'] = res_set3_5[i]['studentGender']
                dic['Gradual Font_set3'] = res_set3_5[i]['COUNT(is_correct)*1.25']
            if len(res_set1_6) > 0 and i<len(res_set1_6):
                dic['studentID'] = res_set1_6[i]['studentID']
                dic['studentAge'] = res_set1_6[i]['studentAge']
                dic['studentGender'] = res_set1_6[i]['studentGender']
                dic['Summary Only_set1'] = res_set1_6[i]['COUNT(is_correct)*1.25']
            if len(res_set2_6) > 0 and i<len(res_set2_6):
                dic['studentID'] = res_set2_6[i]['studentID']
                dic['studentAge'] = res_set2_6[i]['studentAge']
                dic['studentGender'] = res_set2_6[i]['studentGender']
                dic['Summary Only_set2'] = res_set2_6[i]['COUNT(is_correct)*1.25']
            if len(res_set3_6) > 0 and i<len(res_set3_6):
                dic['studentID'] = res_set3_6[i]['studentID']
                dic['studentAge'] = res_set3_6[i]['studentAge']
                dic['studentGender'] = res_set3_6[i]['studentGender']
                dic['Summary Only_set3'] = res_set3_6[i]['COUNT(is_correct)*1.25']
            res.append(dic)
        print(res)
        return res




@app.get("/avgResults/{test_name}")
def get_answer_by_test_name_AVG(test_name: str):
    res = []
    if test_name != None :
        res_set1_1 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "WithoutVisualization", 1)
        res_set1_2 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualHighlight", 1)
        res_set1_3 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "Highlight", 1)
        res_set1_4 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "IncreasedFont", 1)
        res_set1_5 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualFont", 1)
        res_set1_6 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "SummaryOnly", 1)
        res_set2_1 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "WithoutVisualization", 2)
        res_set2_2 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualHighlight", 2)
        res_set2_3 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "Highlight", 2)
        res_set2_4 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "IncreasedFont", 2)
        res_set2_5 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualFont", 2)
        res_set2_6 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "SummaryOnly", 2)
        res_set3_1 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "WithoutVisualization", 3)
        res_set3_2 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualHighlight", 3)
        res_set3_3 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "Highlight", 3)
        res_set3_4 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "IncreasedFont", 3)
        res_set3_5 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "GradualFont", 3)
        res_set3_6 = StudentAnswersRepository.get_answer_by_test_name_AVG("\'" + test_name + "\'", "SummaryOnly", 3)
        for i in range(len(res_set1_1)):
            dic={}
            dic['studentID'] = res_set1_1[i]['studentID']
            dic['studentAge'] = res_set1_1[i]['studentAge']
            dic['studentGender'] = res_set1_1[i]['studentGender']
            if len(res_set1_1) > 0:
                dic['Without Visualization_set1'] = res_set1_1[i]['AVG(time_to_answer)']
            if len(res_set2_1) > 0:
                dic['Without Visualization_set2'] = res_set2_1[i]['AVG(time_to_answer)']
            if len(res_set3_1) > 0:
                dic['Without Visualization_set3'] = res_set3_1[i]['AVG(time_to_answer)']
            if len(res_set1_2) > 0:
                dic['Gradual Highlight_set1'] = res_set1_2[i]['AVG(time_to_answer)']
            if len(res_set2_2) > 0:
                dic['Gradual Highlight_set2'] = res_set2_2[i]['AVG(time_to_answer)']
            if len(res_set3_2) > 0:
                dic['Gradual Highlight_set3'] = res_set3_2[i]['AVG(time_to_answer)']
            if len(res_set1_3) > 0:
                dic['Highlight_set1'] = res_set1_3[i]['AVG(time_to_answer)']
            if len(res_set2_3) > 0:
                dic['Highlight_set2'] = res_set2_3[i]['AVG(time_to_answer)']
            if len(res_set3_3) > 0:
                dic['Highlight_set3'] = res_set3_3[i]['AVG(time_to_answer)']
            if len(res_set1_4) > 0:
                dic['Increased Font_set1'] = res_set1_4[i]['AVG(time_to_answer)']
            if len(res_set2_4) > 0:
                dic['Increased Font_set2'] = res_set2_4[i]['AVG(time_to_answer)']
            if len(res_set3_4) > 0:
                dic['Increased Font_set3'] = res_set3_4[i]['AVG(time_to_answer)']
            if len(res_set1_5) > 0:
                dic['Gradual Font_set1'] = res_set1_5[i]['AVG(time_to_answer)']
            if len(res_set2_5) > 0:
                dic['Gradual Font_set2'] = res_set2_5[i]['AVG(time_to_answer)']
            if len(res_set3_5) > 0:
                dic['Gradual Font_set3'] = res_set3_5[i]['AVG(time_to_answer)']
            if len(res_set1_6) > 0:
                dic['Summary Only_set1'] = res_set1_6[i]['AVG(time_to_answer)']
            if len(res_set2_6) > 0:
                dic['Summary Only_set2'] = res_set2_6[i]['AVG(time_to_answer)']
            if len(res_set3_6) > 0:
                dic['Summary Only_set3'] = res_set3_6[i]['AVG(time_to_answer)']
            res.append(dic)
        print(res)
        return res

@app.get("/readingResults/{test_name}")
def get_answer_by_test_name_reading_timee(test_name: str):
    res = []
    if test_name != None :
        res_set1_1 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "WithoutVisualization", 1)
        res_set1_2 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualHighlight", 1)
        res_set1_3 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "Highlight", 1)
        res_set1_4 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "IncreasedFont", 1)
        res_set1_5 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualFont", 1)
        res_set1_6 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "SummaryOnly", 1)
        res_set2_1 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "WithoutVisualization", 2)
        res_set2_2 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualHighlight", 2)
        res_set2_3 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "Highlight", 2)
        res_set2_4 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "IncreasedFont", 2)
        res_set2_5 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualFont", 2)
        res_set2_6 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "SummaryOnly", 2)
        res_set3_1 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "WithoutVisualization", 3)
        res_set3_2 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualHighlight", 3)
        res_set3_3 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "Highlight", 3)
        res_set3_4 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "IncreasedFont", 3)
        res_set3_5 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "GradualFont", 3)
        res_set3_6 = StudentAnswersRepository.get_answer_by_test_name_reading_time("\'" + test_name + "\'", "SummaryOnly", 3)
        print(res_set1_1)
        for i in range(len(res_set1_1)):
            dic={}
            dic['studentID'] = res_set1_1[i]['studentID']
            dic['studentAge'] = res_set1_1[i]['studentAge']
            dic['studentGender'] = res_set1_1[i]['studentGender']
            if len(res_set1_1) > 0 and i<len(res_set1_1):
                dic['Without Visualization_set1'] = res_set1_1[i]['ReadingTime']
            if len(res_set2_1) > 0 and i<len(res_set2_1):
                dic['Without Visualization_set2'] = res_set2_1[i]['ReadingTime']
            if len(res_set3_1) > 0 and i<len(res_set3_1):
                dic['Without Visualization_set3'] = res_set3_1[i]['ReadingTime']
            if len(res_set1_2) > 0 and i<len(res_set1_2):
                dic['Gradual Highlight_set1'] = res_set1_2[i]['ReadingTime']
            if len(res_set2_2) > 0 and i<len(res_set2_2):
                dic['Gradual Highlight_set2'] = res_set2_2[i]['ReadingTime']
            if len(res_set3_2) > 0 and i<len(res_set3_2):
                dic['Gradual Highlight_set3'] = res_set3_2[i]['ReadingTime']
            if len(res_set1_3) > 0 and i<len(res_set1_3):
                dic['Highlight_set1'] = res_set1_3[i]['ReadingTime']
            if len(res_set2_3) > 0 and i<len(res_set2_3):
                dic['Highlight_set2'] = res_set2_3[i]['ReadingTime']
            if len(res_set3_3) > 0 and i<len(res_set3_3):
                dic['Highlight_set3'] = res_set3_3[i]['ReadingTime']
            if len(res_set1_4) > 0 and i<len(res_set1_4):
                dic['Increased Font_set1'] = res_set1_4[i]['ReadingTime']
            if len(res_set2_4) > 0 and i<len(res_set2_4):
                dic['Increased Font_set2'] = res_set2_4[i]['ReadingTime']
            if len(res_set3_4) > 0 and i<len(res_set3_4):
                dic['Increased Font_set3'] = res_set3_4[i]['ReadingTime']
            if len(res_set1_5) > 0 and i<len(res_set1_5):
                dic['Gradual Font_set1'] = res_set1_5[i]['ReadingTime']
            if len(res_set2_5) > 0 and i<len(res_set2_5):
                dic['Gradual Font_set2'] = res_set2_5[i]['ReadingTime']
            if len(res_set3_5) > 0 and i<len(res_set3_5):
                dic['Gradual Font_set3'] = res_set3_5[i]['ReadingTime']
            if len(res_set1_6) > 0 and i<len(res_set1_6):
                dic['Summary Only_set1'] = res_set1_6[i]['ReadingTime']
            if len(res_set2_6) > 0 and i<len(res_set2_6):
                dic['Summary Only_set2'] = res_set2_6[i]['ReadingTime']
            if len(res_set3_6) > 0 and i<len(res_set3_6):
                dic['Summary Only_set3'] = res_set3_6[i]['ReadingTime']
            res.append(dic)
        print(res)
        return res


@app.get("/rankingResult/{test_name}")
def get_placing_by_test_name(test_name: str):
    if(test_name != None ):
        return StudentAnswersRepository.get_placing_by_test_name("\'"+test_name+"\'")

@app.post("/rank")
def add_rank(rank_info: RankCreate):
    student_id = rank_info.student_id
    withoutVisualization = rank_info.withoutVisualization
    gradualHighlight = rank_info.gradualHighlight
    highlight = rank_info.highlight
    increasedFont = rank_info.increasedFont
    gradualFont = rank_info.gradualFont
    summaryOnly = rank_info.summaryOnly
    textId = rank_info.textId
    return RankRepository.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,
                                      gradualFont, summaryOnly, textId)


@app.post("/updateRankOrder")
def update_rank(rank_info: RankUpdate):
    student_id = rank_info.student_id
    WithoutVisualization_place = rank_info.WithoutVisualization_place
    highlight_place = rank_info.highlight_place
    increasedFont_place = rank_info.increasedFont_place
    summaryOnly_place = rank_info.summaryOnly_place
    gradualHighlight_place = rank_info.gradualHighlight_place
    gradualFont_place = rank_info.gradualFont_place
    # d_places = {firstPlace: "1", secondPlace: "2", thirdPlace: "3", fourthPlace: "4", fifthPlace: "5", sixthPlace: "6" }

    return RankRepository.update_rank(student_id, WithoutVisualization_place,gradualHighlight_place,highlight_place,increasedFont_place,
                                      gradualFont_place,summaryOnly_place)


@app.get("/getTestProperties/{test_name}")
def getTestProperties(test_name: str):
    return VisualizationPropertiesRepository.get_test_properties(test_name)

@app.get("/getTestGlobalInfo/{test_info}")
def getTestProperties(test_info: str):
    test_name, set_place = test_info.split("is")
    data = VisualizationPropertiesRepository.get_test_properties(test_name)
    first_set = []
    second_set = []
    third_set = []

    for text in data:
        # we will change how we get the text sentence with weights!
        text_info = get_text_total_info(int(text['text_id']))
        # print(text_info)
        text['type'] = convert_visualization_ids_to_types(text['visualiztion_id'])
        text['sentences'] = text_info[0]['sentences']
        if text['set_num'] == 1:
            first_set.append(text)
        elif text['set_num'] == 2:
            second_set.append(text)
        else:
            max_value = 0.0
            min_value = 1.0
            for sentence in text['sentences']:
                if float(sentence["weight"]) < min_value:
                    min_value = float(sentence["weight"])
                if float(sentence["weight"]) > max_value:
                    max_value = float(sentence["weight"])

            for sentence in text['sentences']:
                if float(sentence["weight"]) == min_value:
                    sentence["weight"] = str(max_value)
                if float(sentence["weight"]) == max_value:
                    sentence["weight"] = str(min_value)
            third_set.append(text)

    random.shuffle(first_set)
    random.shuffle(second_set)
    random.shuffle(third_set)

    if set_place == "before":
        return first_set + second_set
    else:
        return third_set



@app.post("/saveSummary")
def update_rank(studentSummary: StudentSummary):
    studentId = studentSummary.student_id
    text_id = studentSummary.text_id
    summary = studentSummary.summary
    readingTime = studentSummary.readingTime
    summaryTime = studentSummary.summaryTime
    return StudentRepository.saveStudentSummary(studentId, text_id, summary, readingTime, summaryTime)

def convert_visualization_ids_to_types(id):
    if id == 0:
        return "Without Visualization"
    elif id == 2:
        return "Highlight"
    elif id == 1:
        return "Gradual Highlight"
    elif id == 3:
        return "Increased Font"
    elif id == 4:
        return "Gradual Font"
    elif id == 5:
        return "Summary Only"
    else:
        return "Highlight"



@app.get("/text_weight/{id}")
def Text_weight(id: int):
    return TextRepository.get_text_weight(id)



uvicorn.run(app, host="localhost", port=5000)
# @app.delete("/texts/{id}")
# def delete_text():
#     pass

# @app.put("/texts/{id}")
# def update_text():
#     pass
# pass !@
#jhjhghgh

# uvicorn.run(app, host="localhost", port=3000)
