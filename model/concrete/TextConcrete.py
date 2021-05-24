from model.db import sqlliteDButils
from model.dao import TextDAO

# Building a query - Step 2

def insert_text(name, content):
    query = TextDAO.insert_text(name, content)
    val = (name, content)
    return sqlliteDButils.execute_run(query, val)

def update_text(id, name, content):
    query = TextDAO.update_text(id, name, content)
    return sqlliteDButils.execute_run(query)

def delete_text(id):
    query = TextDAO.delete_text(id)
    val= (id,)
    return sqlliteDButils.execute_run(query,val)

def get_text_by_id(id):
    query = TextDAO.get_text_by_id(id)
    return sqlliteDButils.execute_select(query)

def get_texts():
    query = TextDAO.get_texts()
    return sqlliteDButils.execute_select(query)


def get_all_id_texts():
    query = TextDAO.get_all_id_texts()
    return sqlliteDButils.execute_select(query)

def get_text_weight(id):
    query = TextDAO.get_text_weight(id)
    return sqlliteDButils.execute_select(query)


def get_text_name(id):
    query = TextDAO.get_text_name(id)
    return sqlliteDButils.execute_select(query)
