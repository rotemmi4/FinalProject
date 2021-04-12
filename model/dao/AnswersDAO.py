
def insert_answer(option_id, question_id, text_id, is_correct, answer_content):
    return ("INSERT INTO answers (option_id, question_id, text_id, is_correct, answer_content) values (?,?,?,?,?)")

