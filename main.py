from data_scrapy import dataScrapy
from database import Database as DB
if __name__ == '__main__':
    """
    
    driver = googleplay.start()
    app_ids = googleplay.get_app_ids(driver)
    print(app_ids)
    googleplay.get_comments(driver, app_ids)
    
    """
    # 连接数据库
    db = DB.connect_db()

    # 创建app表
    DB.create_table_1(db, "app_details")
    # 创建app_reviews表
    DB.create_table_2(db, "app_reviews")

    # 获取app_id
    app_ids = ['com.instagram.android']
    # 根据app_ids爬取数据
    df_app_details, df_app_reviews = dataScrapy.data_scrapy(app_ids)
    dataScrapy.save_as(df_app_details, df_app_reviews)
    DB.insert_data(db, "app_reviews", df_app_reviews)
    DB.insert_data(db, "app_details", df_app_details)
