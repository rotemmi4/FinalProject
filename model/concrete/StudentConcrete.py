from model.db import sqlliteDButils
from model.dao import StudenInfoDAO, questionsDAO, AnswersDAO


# Building a query - Step 2

def insert_info(student_id, age, gender):
    query = StudenInfoDAO.insert_info()
    val = (student_id, age, gender)
    return sqlliteDButils.execute_run(query, val)

def get_test_ids():
    query = StudenInfoDAO.get_test_ids()
    return sqlliteDButils.execute_select(query)


def get_questions_by_text_id(text_id):
    query = questionsDAO.get_questions_by_text_id(text_id)
    # val = (int(text_id),)
    return sqlliteDButils.execute_select(query)


def get_all_answers_by_question_id(question_id):
    query = AnswersDAO.get_all_answers_by_question_id(question_id)
    return sqlliteDButils.execute_select(query)


def insert_question_results(results):
    is_correct = results['answer']
    time = results['time']
    question_id = results['question_id']
    student_id = results['student_id']
    query = StudenInfoDAO.insert_question_results(student_id, question_id, is_correct, time)
    val = (student_id, question_id, is_correct, time)
    return sqlliteDButils.execute_run(query, val)


def get_texts_by_test_id(test_id):
    query = StudenInfoDAO.get_texts_by_test_id(test_id)
    return sqlliteDButils.execute_select(query)


def get_type_by_text_id(text_id):
    query = StudenInfoDAO.get_type_by_text_id(text_id)
    return sqlliteDButils.execute_select(query)
