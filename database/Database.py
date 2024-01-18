import pymysql
import pandas
from sqlalchemy import create_engine

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

def create_table_1(db, table_name):
    with db.cursor() as cursor:
        sql_create_table = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            descriptionHTML TEXT,
            summary TEXT,
            installs INT,
            minInstalls INT,
            realInstalls INT,
            score FLOAT,
            ratings INT,
            reviews INT,
            histogram TEXT,
            price VARCHAR(255),
            free BOOLEAN,
            currency VARCHAR(255),
            sale BOOLEAN,
            saleTime VARCHAR(255),
            originalPrice VARCHAR(255),
            saleText VARCHAR(255),
            offersIAP BOOLEAN,
            inAppProductPrice VARCHAR(255),
            developer VARCHAR(255),
            developerId VARCHAR(255),
            developerEmail VARCHAR(255),
            developerWebsite VARCHAR(255),
            developerAddress VARCHAR(255),
            privacyPolicy VARCHAR(255),
            genre VARCHAR(255),
            genreId VARCHAR(255),
            categories TEXT,
            icon VARCHAR(255),
            headerImage VARCHAR(255),
            screenshots TEXT,
            video BOOLEAN,
            videoImage VARCHAR(255),
            contentRating VARCHAR(255),
            contentRatingDescription VARCHAR(255),
            adSupported BOOLEAN,
            containsAds BOOLEAN,
            released VARCHAR(255),
            updated VARCHAR(255),
            version VARCHAR(255),
            comments TEXT,
            appId VARCHAR(255),
            url VARCHAR(255)
        )
        """
        cursor.execute(sql_create_table)


def create_table_2(db, table_name):
    with db.cursor() as cursor:
        sql_create_table = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id VARCHAR(255) PRIMARY KEY,
            userName VARCHAR(255),
            userImage VARCHAR(255),
            content TEXT,
            score INT,
            thumbsUpCount INT,
            reviewCreatedVersion VARCHAR(255),
            reviewCreatedAt DATETIME,
            at DATETIME,
            replyContent TEXT,
            repliedAt DATETIME,
            appVersion VARCHAR(255)
        )
        """
        cursor.execute(sql_create_table)
def insert_data(db, table_name, df):
    engine = create_engine('mysql+pymysql://root:#Qaz7418495@localhost/GooglePlayApp')  # 修改为你的 MySQL 连接信息
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
def connect_close(db):
    db.close()