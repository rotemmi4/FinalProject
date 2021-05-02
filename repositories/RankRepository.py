from model.concrete import RankConcrete


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly):
    return RankConcrete.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly)

def update_rank(student_id, d_places):
    withoutVisualization = d_places["withoutVisualization"]
    gradualHighlight = d_places["gradualHighlight"]
    highlight = d_places["highlight"]
    increasedFont = d_places["increasedFont"]
    gradualFont = d_places["gradualFont"]
    summaryOnly = d_places["summaryOnly"]
    return RankConcrete.update_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly)



