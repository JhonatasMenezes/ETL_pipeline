import mysql.connector as mysql

class DatabaseConnecor:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd="admin"
        )
        cls.connection = db_connection
