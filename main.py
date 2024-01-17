from data_scrapy import dataScrapy
from connect_database import connectDatabase as cd
if __name__ == '__main__':
    """
    
    driver = googleplay.start()
    app_ids = googleplay.get_app_ids(driver)
    print(app_ids)
    googleplay.get_comments(driver, app_ids)
    
    """
    # 连接数据库
    db = cd.connect_db()
    # 创建app表
    cd.create_table(db, "app")
    # 创建app_reviews表
    cd.create_table(db, "app_reviews")

    # 获取app_id
    app_ids = ['com.instagram.android']
    # 根据app_ids爬取数据
    dataScrapy.data_scrapy(app_ids)
