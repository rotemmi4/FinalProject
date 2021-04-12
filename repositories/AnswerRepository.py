from model.concrete import AnswerConcrete


def insert_answer(option_id, question_id, text_id, is_correct, answer_content):
    return AnswerConcrete.insert_answer(option_id, question_id, text_id, is_correct, answer_content)