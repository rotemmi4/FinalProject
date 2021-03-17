from model.concrete import QuestionConcrete


def insert_question(text_id, question_content):
    return QuestionConcrete.insert_question(text_id, question_content)

def get_questions_by_id(id):
    return QuestionConcrete.get_questions_by_id(id)

def delete_text(id):
    return QuestionConcrete.delete_question(id)

def get_max_question_id():
    return QuestionConcrete.get_max_question_id()
