"""
目标网址: https://www.ku6.com/detail/71

作业要求:
    1.用 selenium 财经所需要的数据
    2.需要数据如下所示
        title 视频的标题
        img_url 视频图片对应的url地址
        detail_url 视频详情页url地址
    3.保存为csv数据
请在下方编写代码
"""

from selenium import webdriver

# 打开浏览器请求目标url
driver = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://www.ku6.com/detail/71'
driver.get(url=url)
driver.implicitly_wait(10)

# 查找渲染后的网页中的数据
results = driver.find_elements_by_class_name('video-item')
for result in results:
    title = result.find_element_by_xpath('.//div[2]/h3/a').text
    img_url = result.find_element_by_xpath('.//div/a/img').get_attribute('src')
    doc_url = result.find_element_by_xpath('.//div/a').get_attribute('href')
    print(title, img_url, doc_url)


