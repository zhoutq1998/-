# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from datetime import timedelta
import time
import sys

def run(apply_date, id, passwd):
    data = {
        'url': 'http://thos.tsinghua.edu.cn',
        'id': id,
        'pw': passwd
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.implicitly_wait(10)
    chrome.get(data['url'])
    chrome.find_element(By.ID, 'i_user').send_keys(data['id'])
    chrome.find_element(By.ID, 'i_pass').send_keys(data['pw'])
    chrome.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-block').click()
    chrome.find_element(By.NAME, '学生进出校审批').click()
    chrome.switch_to.frame('formIframe')
    js = 'document.getElementById("SQHXRQQS").removeAttribute("readonly")'
    chrome.execute_script(js)
    chrome.find_element(By.ID, 'SQHXRQQS').clear()
    chrome.switch_to.default_content()
    chrome.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
    chrome.switch_to.frame('formIframe')
    chrome.find_element(By.ID, 'SQHXRQQS').send_keys(apply_date)
    chrome.switch_to.default_content()
    chrome.find_element(By.CLASS_NAME, 'btn.btn-primary.pull-left.btn-block').click()
    chrome.close()

def main():
    args = sys.argv[1:]
    id = args[0]
    passwd = args[1]
    day_num = 1
    if len(args) >= 3:
        day_num = min(int(args[2]), 8)
    for i in range(day_num):
        apply_date = str(date.today()+timedelta(days=i))
        run(apply_date, id, passwd)
        print(apply_date)
        time.sleep(10)

if __name__ == '__main__':
    main()
