import random

from MySql.StoredProcedures.Config.db_connect import Client

client = Client.connectDB()
cursor = client.cursor()


class Users:
    # Execute SQL query
    @staticmethod
    def get_all(table_name):
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    @staticmethod
    def insert_one(name, age, email):
        sql = "INSERT INTO Users (user_name, age, user_email) VALUES (%s, %s, %s)"
        val = (name, age, email)
        cursor.execute(sql, val)
        client.commit()

    @staticmethod
    def update_one(name, age):
        sql = "UPDATE Users SET age = (%s) WHERE user_name = (%s)"
        val = (age, name)
        cursor.execute(sql, val)
        client.commit()


    @staticmethod
    def pro_call(sp_name):
        cursor.callproc(sp_name, args=(4,))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for data in rows:
                print(data)
