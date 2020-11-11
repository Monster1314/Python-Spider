"""
目标网址: https://trade.maoyan.com/ 模拟登录

作业要求:
    1.用 selenium 模拟登录猫眼(首先自己注册一个账号)
    2.登录成功后可能会有一个美团验证(不用理会), 完成上一个需求即可
请在下方编写代码
"""

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://trade.maoyan.com/'
driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(5)

login = driver.find_element_by_xpath('.//div[@class="user-avatar J-login"]/img').click()
phone = driver.find_element_by_id('login-email').send_keys('19999')
password = driver.find_element_by_id('login-password').send_keys('19999')
login_click = driver.find_element_by_class_name('btn').click()


