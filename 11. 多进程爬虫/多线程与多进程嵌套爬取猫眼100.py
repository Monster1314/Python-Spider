"""
    猫眼100网页, 请用多进程嵌套多线程池方式实现


请在下方编写代码
"""

import requests
import parsel
import concurrent.futures
import csv
import time
import multiprocessing

lock = multiprocessing.Lock()  # 创建线程锁对象


def send_requests(url):
    '''
    向目标url发送请求
    :param url: 目标网址 
    :return: 请求返回response
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'Host': 'maoyan.com',
        'Referer': 'https://maoyan.com/board/4?offset=0',
    }
    response = requests.get(url=url, headers=headers)
    return response


def parse_data(data):
    '''
    解析数据
    :param data: 传入的response数据
    :return: 解析得到的数据列表list
    '''
    selector = parsel.Selector(data.text)
    # print(selector)

    dds = selector.xpath('//div[@class="main"]/dl/dd')
    data_list = []
    for dd in dds:
        name = dd.xpath('.//p[@class="name"]/a/text()').get()
        star = dd.xpath('.//p[@class="star"]/text()').get().strip()
        release_time = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
        score = dd.xpath('.//p[@class="score"]/i[1]/text()').get() + dd.xpath('.//p[@class="score"]/i[2]/text()').get()
        # print(name,star,release_time,score)
        data_list.append([name, star, release_time, score])
    return data_list


def save_data(data):
    """
    保存数据的方法
    :param data: 数据
    :return: None
    """
    with open('maoyan.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        # csv_writer.writerow(['name', 'star', 'releasetime', 'score'])
        for i in data:
            lock.acquire()  # 加锁
            csv_writer.writerow(i)
            lock.release()


def main(url):
    html = send_requests(url)
    
    data_list = parse_data(html)
    
    save_data(data_list)


def multi_thread(url):
    '''定义多线程'''
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(main, url)


if __name__ == '__main__':

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:  # 多进程
        for page in range(0, 91, 10):
            url = f'https://maoyan.com/board/4?offset={page}'
            executor.submit(main, url)

    all_time = time.time() - start_time
    print('花费时间:', all_time)
