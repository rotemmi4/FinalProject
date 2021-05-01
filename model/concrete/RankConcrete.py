from model.db import sqlliteDButils
from model.dao import RankDAO


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly):
    query = RankDAO.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly)
    val = (student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly)
    return sqlliteDButils.execute_run(query, val)

def update_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly):
    query = RankDAO.update_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly)
    val = (withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly, student_id)
    return sqlliteDButils.execute_run(query, val)
