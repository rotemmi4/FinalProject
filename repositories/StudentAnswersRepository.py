from model.concrete import StudentAnswersConcrete

def get_answer_by_test_name(testName, visualization):
    return StudentAnswersConcrete.get_answer_by_test_name(testName, visualization)

def get_placing_by_test_name(testName):
    return StudentAnswersConcrete.get_placing_by_test_name(testName)