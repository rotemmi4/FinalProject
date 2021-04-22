from model.db import sqlliteDButils
from model.dao import RankDAO


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order):
    query = RankDAO.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order)
    val = (student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order)
    return sqlliteDButils.execute_run(query, val)

def update_rank(student_id,rank_order):
    query = RankDAO.update_rank(student_id,rank_order)

    return sqlliteDButils.execute_select(query)
