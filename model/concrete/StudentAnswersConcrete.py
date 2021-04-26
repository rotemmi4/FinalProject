from model.dao import StudentAnswersDAO
from model.db import sqlliteDButils


def get_answer_by_test_name(testName, visualization):
    query = StudentAnswersDAO.get_answer_by_test_name(testName, visualization)
    return sqlliteDButils.execute_select(query)

def get_placing_by_test_name(testName):
    query = StudentAnswersDAO.get_placing_by_test_name(testName)
    return sqlliteDButils.execute_select(query)

