from model.db import sqlliteDButils
from model.dao import RankDAO


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly):
    query = RankDAO.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly)
    val = (student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly)
    return sqlliteDButils.execute_run(query, val)

def update_rank(student_id, WithoutVisualization_place,gradualHighlight_place,highlight_place,increasedFont_place,gradualFont_place,summaryOnly_place):
    query = RankDAO.update_rank(student_id, WithoutVisualization_place,gradualHighlight_place,highlight_place,increasedFont_place, gradualFont_place,summaryOnly_place)
    val = (WithoutVisualization_place,gradualHighlight_place,highlight_place,increasedFont_place,gradualFont_place,summaryOnly_place, student_id)
    return sqlliteDButils.execute_run(query, val)
