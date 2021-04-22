from model.concrete import RankConcrete


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order):
    return RankConcrete.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order)

def update_rank(student_id, rank_order):
    return RankConcrete.update_rank(student_id,rank_order)