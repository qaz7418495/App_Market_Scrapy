import pymysql


def connect_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="#Qaz7418495",
    )
    with db.cursor() as cursor:
        sql_create_database = "CREATE DATABASE IF NOT EXISTS GooglePlayApp"
        cursor.execute(sql_create_database)

    db.select_db('GooglePlayApp')
    return db

def create_table(db, table_name):
    with db.cursor() as cursor:
        sql_create_table = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
        """
        cursor.execute(sql_create_table)


def insert_data(db, table_name, data):
    with db.cursor() as cursor:
        sql_insert_data = f"""
        
    """
    cursor.execute()
def connect_close(db):
    db.close()