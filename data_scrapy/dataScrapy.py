import os
import numpy as np
from google_play_scraper import app, reviews_all, Sort, reviews
import pandas as pd
import ssl


def data_scrapy(app_ids):
    # 跳过ssl证书验证
    ssl._create_default_https_context = ssl._create_unverified_context

    for app_id in app_ids:
        # 获取app详情
        app_details = app(
            app_id,
            lang='en',
            country='us'
        )
        # print(app_details)    # 返回形式为dict[str]

        # 获取app评论（500条）
        app_reviews = reviews(
            app_id,
            count=500,
            lang='en',
            country='us',
            sort=Sort.NEWEST
        )
        # print(app_reviews)  # 返回形式为tuple[list[dict]]

        # 从元组中提取，转为list[dict]形式
        app_reviews_list = app_reviews[0]

        # 将列表形式转换为dataframe，列名为review
        df_app_review = pd.DataFrame(np.array(app_reviews_list), columns=['review'])

        # 将字典形式拆开成多列，列名为key值
        df_app_review = df_app_review.join(pd.DataFrame(df_app_review.pop('review').tolist()))

        # 将app_details转为DataFrame
        df_app_details = pd.DataFrame([app_details])

        # 创建数据保存路径
        save_path = f'data/{app_details["title"]}'

        # 创建app文件夹
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # 将app详情导出到文件夹中 app名字_details.csv
        df_app_details.to_csv(f'{save_path}/{app_details["title"]}_details.csv', index=False)
        # 将app评论导出到文件夹中 app名字_reviews.csv
        df_app_review.to_csv(f'{save_path}/{app_details["title"]}_reviews.csv', index=False)
