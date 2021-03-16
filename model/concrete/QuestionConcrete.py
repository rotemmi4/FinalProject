from model.db import sqlliteDButils
from model.dao import questionsDAO


def insert_question(question_id, text_id, question_content):
    query = questionsDAO.insert_question(question_id, text_id, question_content)
    val = (question_id, text_id, question_content)
    return sqlliteDButils.execute_run(query, val)

def get_questions_by_id(id):
    query = questionsDAO.get_questions_by_id(id)
    return sqlliteDButils.execute_select(query)

def delete_question(id):
    query = questionsDAO.delete_question(id)
    val= (id,)
    return sqlliteDButils.execute_run(query,val)