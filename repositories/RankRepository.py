from model.concrete import RankConcrete


def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly, textId):
    return RankConcrete.insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,
                                    gradualFont, summaryOnly, textId)


def update_rank(student_id, WithoutVisualization_place, gradualHighlight_place, highlight_place,increasedFont_place, gradualFont_place, summaryOnly_place):

  #  withoutVisualization = d_places["withoutVisualization"]
   # gradualHighlight = d_places["gradualHighlight"]
  #  highlight = d_places["highlight"]
   # increasedFont = d_places["increasedFont"]
   # gradualFont = d_places["gradualFont"]
   # summaryOnly = d_places["summaryOnly"]

    return RankConcrete.update_rank(student_id, WithoutVisualization_place,gradualHighlight_place,highlight_place,increasedFont_place,gradualFont_place,summaryOnly_place)



