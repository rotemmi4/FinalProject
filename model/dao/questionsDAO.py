
def insert_question(text_id, question_content):
    return ("INSERT INTO questions (text_id, question_content) values (?,?)")


def delete(question_id):
    return ("DELETE FROM questions WHERE [question_id] in (?)")
    #return ("DELETE FROM questions where number_id=? AND text_id=?)", [number_id, text_id])


def get_questions_by_id(text_id):
    #return ("SELECT * FROM questions WHERE [text_id] is (?)")
    return ("SELECT * FROM questions WHERE text_id=" + str(text_id))


def get_max_question_id():
    return ("SELECT MAX(question_id) AS queId FROM questions ")

def get_max_question_id():
    return ("SELECT MAX(question_id) AS queId FROM questions ")