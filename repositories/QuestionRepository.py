from model.concrete import QuestionConcrete


def insert_question(number_id, text_id, content):
    return QuestionConcrete.insert_question(number_id, text_id, content)

def get_questions():
    return QuestionConcrete.get_questions()