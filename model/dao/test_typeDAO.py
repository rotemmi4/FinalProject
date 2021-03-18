def insert(test_name, type):
    return ("INSERT INTO test_type values (?,?)")


def delete(name):
    return ("DELETE FROM test_type where name=? ")

def get_all_tests():
    return ("SELECT * FROM test_type ")

def get_test_by_name(name):
    return ("SELECT * FROM test_type WHERE name={}".format("\""+name+"\""))

