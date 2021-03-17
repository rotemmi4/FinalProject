from model.db import sqlliteDButils
from model.dao import questionsDAO


def insert_question(text_id, question_content):
    query = questionsDAO.insert_question(text_id, question_content)
    val = ( text_id, question_content)
    return sqlliteDButils.execute_run(query, val)

def get_questions_by_id(id):
    query = questionsDAO.get_questions_by_id(id)
    return sqlliteDButils.execute_select(query)

def delete_question(id):
    query = questionsDAO.delete_question(id)
    val= (id,)
    return sqlliteDButils.execute_run(query,val)

def get_max_question_id():
    query = questionsDAO.get_max_question_id()
    return sqlliteDButils.execute_select(query)

def get_max_question_id():
    query = questionsDAO.get_max_question_id()
    return sqlliteDButils.execute_select(query)