from model.concrete import StudentAnswersConcrete

def get_answer_by_test_name_SUM(testName, visualization, set_num):
    return StudentAnswersConcrete.get_answer_by_test_name_SUM(testName, visualization, set_num)

def get_answer_by_test_name_COUNT(testName, visualization, set_num):
    return StudentAnswersConcrete.get_answer_by_test_name_COUNT(testName, visualization, set_num)

def get_answer_by_test_name_AVG(testName, visualization, set_num):
    return StudentAnswersConcrete.get_answer_by_test_name_AVG(testName, visualization, set_num)

def get_placing_by_test_name(testName):
    return StudentAnswersConcrete.get_placing_by_test_name(testName)

def correct_answers_count(testName):
    return StudentAnswersConcrete.correct_answers_count(testName)

def get_answer_by_test_name_reading_time(testName, visualization, set_num):
    return StudentAnswersConcrete.get_answer_by_test_name_reading_time(testName, visualization, set_num)

def get_student_details(testName):
    return StudentAnswersConcrete.get_student_details(testName)