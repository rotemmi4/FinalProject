
def insert_info():
    return ("INSERT INTO StudentInfo (studentID, studentAge, studentGender) values (?,?,?);")

def get_test_ids():
    return ("SELECT test_id FROM visualiztion_properties")

# def delete(student_id):
#     return ("DELETE FROM Student_info where student_id=?", [student_id])
#
#
# def get_student_info_by_id(student_id):
#     return ("SELECT * FROM Student_info WHERE student_id=?", [student_id])
#
#
# def get_student_answers(student_id):
#     pass
#
# def get_student_sorted_rank(student_id):
#     pass
#
# def get_student_ranks_for_each_visualization(student_id):
#     pass
#
# def get_student_texts(student_id):
#     pass

def insert_question_results(student_id, question_id, is_correct, time, test_name):
    return ("INSERT INTO StudentAnswers (studentID, question_id, is_correct, time_to_answer, test_name) values (?,?,?,?,?);")


def get_texts_by_test_id(test_name):
    return ('SELECT text_id FROM visualiztion_properties WHERE test_id="' + test_name +'";')

 # here?!
def get_type_by_text_id(test_id):
    return ("SELECT visualiztion_id FROM visualiztion_properties WHERE text_id=" + str(test_id))
