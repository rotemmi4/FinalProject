
def insert(type):
    return ("INSERT INTO visualiztions (type) values (?)", [type])

def update(id, type):
    return ("UPDATE visualiztions set type=? where id=?)", [type, id])

def delete(id):
    return ("DELETE FROM visualiztions where id=?)", [id])

def get_visualiztion_by_id(id):
    return ("SELECT * FROM visualiztions WHERE id={}".format(id))

def get_visualiztions():
    return ("SELECT * FROM visualiztions")