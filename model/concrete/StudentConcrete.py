from model.db import sqlliteDButils
from model.dao import StudenInfoDAO

# Building a query - Step 2

def insert_info(student_id, age, gender):
    query = StudenInfoDAO.insert_info()
    val = (student_id, age, gender)
    return sqlliteDButils.execute_run(query, val)


