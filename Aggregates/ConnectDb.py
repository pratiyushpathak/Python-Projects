
from DBConnection import dbConnection
def formCollection(tablename):
    client = dbConnection()

    db = client.get_database('userDetails')
    collection = db[tablename]

    return collection
