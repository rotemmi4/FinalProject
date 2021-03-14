from model.db import sqlliteDButils
from model.dao import questionsDAO


def insert_question(number_id, text_id, content):
    query = questionsDAO.insert_question(number_id, text_id, content)
    val = (number_id, text_id, content)
    return sqlliteDButils.execute_run(query, val)


