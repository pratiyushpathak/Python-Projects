# pip install --upgrade setuptools
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("host")
DB_USER = os.getenv("user")
DB_PASSWORD = os.getenv("password")
DB_NAME = os.getenv("DB_NAME")


# Establish MySQL connection
class Client:

    @staticmethod
    def connectDB():
        try:
            connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )

            if connection.is_connected():
                print("Connected to MySQL database")
                return connection

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

