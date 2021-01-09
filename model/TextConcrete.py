from model import TextDAO, sqlliteDButils


def insert_text(name, content):
    query = TextDAO.insert_text(name, content)
    return sqlliteDButils.execute_run(query)

def update_text(id, name, content):
    query = TextDAO.update_text(id, name, content)
    return sqlliteDButils.execute_run(query)

def delete_text(id):
    query = TextDAO.delete_text(id)
    return sqlliteDButils.execute_run(query)

def get_text_by_id(id):
    query = TextDAO.get_text_by_id(id)
    return sqlliteDButils.execute_select(query)

def get_texts():
    query = TextDAO.get_texts()
    return sqlliteDButils.execute_select(query)
