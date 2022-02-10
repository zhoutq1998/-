from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date

data = {
        'url': 'http://thos.tsinghua.edu.cn',
        'id': '',
        'pw': ''
}

# ====================初始化浏览器=======================
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False  # True的话就不会跳出网页
chrome = webdriver.Chrome(options=chrome_options)
chrome.implicitly_wait(10)  # 学校的网页加载太慢，就等一下

# ====================登陆界面===========================
chrome.get(data['url'])
chrome.find_element(By.ID, 'i_user').send_keys(data['id'])
chrome.find_element(By.ID, 'i_pass').send_keys(data['pw'])
chrome.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-block').click()

# ====================学生进出校审批======================
chrome.find_element(By.NAME, '学生进出校审批').click()
chrome.switch_to.frame('formIframe')
js = 'document.getElementById("SQHXRQQS").removeAttribute("readonly")'
chrome.execute_script(js)
chrome.find_element(By.ID, 'SQHXRQQS').clear()
chrome.switch_to.default_content()
chrome.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()
chrome.switch_to.frame('formIframe')
chrome.find_element(By.ID, 'SQHXRQQS').send_keys(str(date.today()))
chrome.switch_to.default_content()
chrome.find_element(By.CLASS_NAME, 'btn.btn-primary.pull-left.btn-block').click()
chrome.close()

