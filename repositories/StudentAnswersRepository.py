from model.concrete import StudentAnswersConcrete

def get_answer_by_test_name(testName):
    return StudentAnswersConcrete.get_answer_by_test_name(testName)