def insert(test_name, type):
    return ("INSERT INTO test_type values (?,?)")


def delete(name):
    return ("DELETE FROM test_type where name=? ")

def get_answer_by_id(test_id, text_id, visualiztion_id,property_name):
    return ("SELECT * FROM visualiztion_properties where test_id=? and text_id=? and visualiztion_id=? and property_name=?".format(test_id, text_id, visualiztion_id,property_name))

def get_answers():
    return ("SELECT * FROM visualiztion_properties")