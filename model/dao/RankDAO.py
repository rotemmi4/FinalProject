
def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly):
    return ("INSERT INTO studentRank (student_id, withoutVisualization_rank, gradualHighlight_rank, highlight_rank, increasedFont_rank, gradualFont_rank, summaryOnly_rank) values (?,?,?,?,?,?,?)")


def update_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont, gradualFont, summaryOnly):
    return (''' UPDATE studentRank
              SET WithoutVisualization_place = ? ,
                  gradualHighlight_place = ? ,
                  highlight_place = ? ,
                  increasedFont_place = ? ,
                  gradualFont_place = ? ,
                  summaryOnly_place = ?
              WHERE student_id = ?''')


def get_rank_by_id(student_id):
    return ("SELECT * FROM studentRank WHERE student_id=?".format(student_id))

def get_all_ranks():
    return ("SELECT * FROM studentRank")
