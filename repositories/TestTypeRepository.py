from model.concrete import TestTypeConcrete

def get_all_tests():
    return TestTypeConcrete.get_all_tests()

def delete_test_by_name(name):
    TestTypeConcrete.delete_test(name)

def save_new_test(name, type):
    TestTypeConcrete.insert_new_test(name,type)