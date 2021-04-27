
def insert_answer(option_id, question_id, text_id, is_correct, answer_content):
    return ("INSERT INTO answers (option_id, question_id, text_id, is_correct, answer_content) values (?,?,?,?,?)")


def get_answer_by_id(option_id, question_id):
    return ("SELECT * FROM answers WHERE id=? AND question_id=?".format(option_id, question_id))

def get_answers():
    return ("SELECT * FROM answers")

def get_all_answers_by_question_id(question_id):
    return ("SELECT answer_content, is_correct FROM answers WHERE question_id=" + str(question_id))