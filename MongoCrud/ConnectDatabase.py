
from DbConnection import dbConnection
def formCollection():
    client = dbConnection()

    db = client.get_database('userDetails')
    collection = db.users

    return collection