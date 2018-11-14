# -*- coding: utf-8 -*-
import re, random, time, datetime, os, pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from fake_useragent import UserAgent
from openpyxl import Workbook
import pandas as pd


wb = Workbook()
sheet = wb.active
sheet.title = "知乎"
item_name = ['name', 'url', 'itemid', 'sellerid']
for j,title in enumerate(item_name):
    sheet.cell(row=1, column=j+1).value = title
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
options.add_argument('disable-gpu')
options.add_argument('useragent="{}"'.format(UserAgent().random))
# options.add_argument('proxy-server={}'.format(requests.get("http://127.0.0.1:5010/get/").text))
driver = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(driver, 30)
# driver.maximize_window()
df = pd.read_excel('产品.xlsx', encoding='gb18030')
links = list(df['链接'].dropna())
driver.get('https://www.tmall.com')
# if os.path.isfile("cookies.pkl"):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)
# else:
#     login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-info"]/a[1]')))
#     login.click()
#     wait2scan = input('>>>>>>>>>扫码后，点击回车继续<<<<<<<<')
#     pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-info"]/a[1]')))
login.click()
wait2scan = input('>>>>>>>>>扫码后，点击回车继续<<<<<<<<')
for url in links:
    driver.get(url)
    time.sleep(random.uniform(1, 3))
    '''
    //ald.taobao.com/recommend.htm?appId=03136&itemId=20328699963 "
    https://img.alicdn.com/imgextra/i1/1653734047/O1CN011flZLzEwq8g87K2_!!0-item_pic.jpg_430x430q90.jpg
    '''
    item_id = driver.find_element_by_xpath('//a[@id="J_AddFavorite"]').get_attribute("data-aldurl")
    seller_id = driver.find_element_by_xpath('//img[@id="J_ImgBooth"]').get_attribute('src')
    item_id = re.findall(re.compile(r'[0-9]{9,15}', re.S), item_id)[0]
    seller_id = re.findall(re.compile(r'[0-9]{9,15}', re.S), seller_id)[0]
    name = driver.find_element_by_xpath('//div[@class="tb-detail-hd"]/h1').text.lstrip().rstrip()
    item_data = [name, driver.current_url, item_id, seller_id]
    sheet.append(item_data)
    wb.save('评论链接.xlsx')
    print('get product_id :{}'.format(item_id))
driver.quit()