import csv
import os.path
import time
import re
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
comments_list = []


def get_app_ids(driver):
    driver.get("https://play.google.com/store/apps")
    driver.implicitly_wait(10)
    jscontroller_value = "PH175e"
    element = driver.find_element(By.CSS_SELECTOR, f'[jscontroller="{jscontroller_value}"]')
    element_html = element.get_attribute("outerHTML")
    pattern = re.compile(r'com\.[^"]+')
    app_ids = pattern.findall(element_html)
    return app_ids


def get_comments(driver, app_ids):
    for app_id in app_ids:
        url = (f"https://play.google.com/store/apps/details?id={app_id}")
        driver.get(url)
        driver.implicitly_wait(10)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        view_all_comments_button = driver.find_element(By.XPATH,
                                                       "/html/body/c-wiz[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/c-wiz[4]/section/div/div[2]/div[5]/div/div/button")
        driver.implicitly_wait(3)
        driver.execute_script("arguments[0].click();", view_all_comments_button)
        comment_area = driver.find_element(By.CLASS_NAME, "odk6He")
        for _ in range(38):
            driver.execute_script("arguments[0].scrollIntoView({block: 'end', behavior: 'smooth'});", comment_area)
            time.sleep(1.5)
        for i in range(1, 1000):
            print(i)
            xpath = f"/html/body/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[{i}]/div[1]"
            try:
                temp_comment = driver.find_element(By.XPATH, xpath).text
                comments_list.append(temp_comment)
            except NoSuchElementException:
                # 如果找不到元素，跳出循环
                print(f"Element at {xpath} not found. Exiting loop.")
                break
        unique_comments_list = list(set(comments_list))
        export_to_csv(app_id, unique_comments_list)
        comments_list.clear()  # Clear the list for the next app


def export_to_csv(app_id, comments):
    save_path = os.path.join('data', f"{app_id}_comments.csv")
    with open(save_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for comment in comments:
            writer.writerow([comment])


def start():
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"在初始化驱动程序时发生错误：{e}")
        return None

