from MySql.StoredProcedures.Config.db_connect import Client
from MySql.StoredProcedures.models.User_model import Users


# print(client)

class UserServices:

    @staticmethod
    def get_all(table_name):
        return Users.get_all(table_name)

    @staticmethod
    def insert_one_my_table(name, age, email):
        print("record inserted")
        Users.insert_one(name, age, email)

    @staticmethod
    def update_age(name, data):
        Users.update_one(name, data)
        return

    @staticmethod
    def pro_call(sp_name):
        Users.pro_call(sp_name)