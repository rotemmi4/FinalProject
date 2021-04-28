from model.concrete import StudentAnswersConcrete

def get_answer_by_test_name_SUM(testName, visualization):
    return StudentAnswersConcrete.get_answer_by_test_name_SUM(testName, visualization)

def get_answer_by_test_name_COUNT(testName, visualization):
    return StudentAnswersConcrete.get_answer_by_test_name_COUNT(testName, visualization)

def get_answer_by_test_name_AVG(testName, visualization):
    return StudentAnswersConcrete.get_answer_by_test_name_AVG(testName, visualization)

def get_placing_by_test_name(testName):
    return StudentAnswersConcrete.get_placing_by_test_name(testName)