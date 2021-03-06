from model.dao import StudentAnswersDAO
from model.db import sqlliteDButils


def get_answer_by_test_name_SUM(testName, visualization, set_num):
    query = StudentAnswersDAO.get_answer_by_test_name_SUM(testName, visualization,set_num)
    return sqlliteDButils.execute_select(query)

def get_answer_by_test_name_COUNT(testName, visualization, set_num):
    query = StudentAnswersDAO.get_answer_by_test_name_COUNT(testName, visualization, set_num)
    return sqlliteDButils.execute_select(query)

def get_answer_by_test_name_AVG(testName, visualization, set_num):
    query = StudentAnswersDAO.get_answer_by_test_name_AVG(testName, visualization, set_num)
    return sqlliteDButils.execute_select(query)

def get_placing_by_test_name(testName):
    query = StudentAnswersDAO.get_placing_by_test_name(testName)
    return sqlliteDButils.execute_select(query)

def correct_answers_count(testName):
    query = StudentAnswersDAO.correct_answers_count(testName)
    return sqlliteDButils.execute_select(query)

def get_answer_by_test_name_reading_time(testName, visualization, set_num):
    query = StudentAnswersDAO.get_answer_by_test_name_reading_time(testName, visualization, set_num)
    return sqlliteDButils.execute_select(query)

def get_student_details(testName):
    query = StudentAnswersDAO.get_student_details(testName)
    return sqlliteDButils.execute_select(query)