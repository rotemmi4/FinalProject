from model.concrete import QuestionConcrete


def insert_question(question_id, text_id, question_content):
    return QuestionConcrete.insert_question(question_id, text_id, question_content)

def get_questions_by_id(id):
    return QuestionConcrete.get_questions_by_id(id)

def delete_text(id):
    return QuestionConcrete.delete_question(id)