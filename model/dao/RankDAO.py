
def insert_rank(student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order):
    return ("INSERT INTO studentRank (student_id, withoutVisualization, gradualHighlight, highlight, increasedFont,gradualFont, summaryOnly,rank_order) values (?,?,?,?,?,?,?,?)")


def get_rank_by_id(student_id):
    return ("SELECT * FROM studentRank WHERE student_id=?".format(student_id))

def get_all_ranks():
    return ("SELECT * FROM studentRank")
