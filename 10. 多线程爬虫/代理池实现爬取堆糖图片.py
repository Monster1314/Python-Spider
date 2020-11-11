"""
    目标网址：https://www.duitang.com/

    作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片

    作业要求：用多线程的方式实现

"""

import requests
import threading
import time
import os
import concurrent.futures


def send_requests(url):
    response = requests.get(url=url)
    return response


def parse_data(json_data):
    ls = json_data['data']['object_list']
    img_urls = []
    for i in ls:
        img_urls.append(i['photo']['path'])
    return img_urls


def save_data(filename, data):
    """
    保存数据的方法
    :param filename: 文件名
    :param data: 图片数据
    :return:
    """
    if not os.path.exists('img'):
        os.mkdir('img')
    with open('img/' + filename, mode='wb') as f:
        f.write(data)
        print('下载完成', filename)


def main(url):
    """主函数, 调用其他三个函数"""
    # 1. 调用发送网络请求的方法
    json_data = send_requests(url).json()
    # 2. 调用数据解析的方法
    img_urls = parse_data(json_data)  # 解析很多图片的url地址  -->列表

    for img_url in img_urls:
        filename = img_url.split('/')[-1]  # 图片文件名
        img = send_requests(img_url).content  # 请求图片数据

        # 3. 调用数据保存的方法
        save_data(filename, img)

    # 记录程序运行时间, 必须等到子线程执行完毕, 不然时间是主线程的执行时间


if __name__ == '__main__':
    start_time = time.time()  # 程序开始的时间

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        for num in range(24, 1201, 24):
            url = f'https://www.duitang.com/napi/blog/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&type=feeds&start={num}'
            executor.submit(main, url)

    end_time = time.time() - start_time
    print('花费时间: ', end_time)
