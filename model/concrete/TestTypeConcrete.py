from model.db import sqlliteDButils
from model.dao import test_typeDAO

def insert_new_test (test_name, type):
    query = test_typeDAO.insert(test_name, type)
    print(query)
    val = (test_name, type)
    return sqlliteDButils.execute_run(query, val)

def delete_test(name):
    query = test_typeDAO.delete(name)
    val = (name,)
    return sqlliteDButils.execute_run(query,val)

def get_all_tests():
    query = test_typeDAO.get_all_tests()
    return sqlliteDButils.execute_select(query)

def get_test_by_name(name):
    query = test_typeDAO.get_test_by_name(name)
    return sqlliteDButils.execute_select(query)