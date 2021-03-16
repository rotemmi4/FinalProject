
def insert_question(number_id, text_id, content):
    return ("INSERT INTO questions (number_id, text_id, question_content) values (?,?,?)")


def delete(number_id, text_id):
    return ("DELETE FROM questions where number_id=? AND text_id=?)", [number_id, text_id])


def get_question_by_id(text_id):
    return ("SELECT * FROM questions WHERE [text_id] in (?)")


   # return ("SELECT * FROM questions WHERE text_id=? ")

