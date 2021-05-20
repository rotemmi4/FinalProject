from model.concrete import StudentConcrete


def insert_info(student_id, age, gender, studentName):
    return StudentConcrete.insert_info(student_id, age, gender, studentName)


# def update_text(id, name, content):
#     return TextConcrete.update_text(id, name, content)
#
# def delete_text(id):
#     return TextConcrete.delete_text(id)
#
# def get_text_by_id(id):
#     return TextConcrete.get_text_by_id(id)
#
# def get_texts():
#     return TextConcrete.get_texts()

def get_test_ids():
    return StudentConcrete.get_test_ids()


def get_questions_by_text_id(text_id):
    return StudentConcrete.get_questions_by_text_id(text_id)


def get_all_answers_by_question_id(question_id):
    return StudentConcrete.get_all_answers_by_question_id(question_id)


def insert_question_results(results):
    try:
        StudentConcrete.insert_question_results(results)
        return "succeed to insert question results"
    except Exception as e:
        return str(e)


def get_texts_by_test_id(test_id):
    # test_id is String!
    return StudentConcrete.get_texts_by_test_id(test_id)


def get_type_by_text_id(text_id):
    return StudentConcrete.get_type_by_text_id(text_id)


def saveStudentSummary(studentId, text_id, summary, reading_time, summary_time):
    return StudentConcrete.saveStudentSummary(studentId, text_id, summary, reading_time, summary_time)
