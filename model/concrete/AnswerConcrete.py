from model.db import sqlliteDButils
from model.dao import AnswersDAO


def insert_answer(option_id, question_id, text_id, is_correct, answer_content):
    query = AnswersDAO.insert_answer(option_id, question_id, text_id, is_correct, answer_content)
    val = (option_id, question_id, text_id, is_correct, answer_content)
    return sqlliteDButils.execute_run(query, val)
