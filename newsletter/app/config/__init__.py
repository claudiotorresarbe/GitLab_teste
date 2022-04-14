from allsql import Sqlite

db = Sqlite('./database.db')

class CreateAll:

    def __init__(self):
        db.create_database(db)
        db.create_table('example',self.__example__())

    def __example__(self):
        txt = 'id integer primary key autoincrement,'
        txt += 'email text,'
        txt += 'status integer'
        return txt
    