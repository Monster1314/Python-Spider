import requests


def get_cookies():
    url = 'https://www.lagou.com/jobs/list_python'
    headers = {
        'referer': 'https://www.lagou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    params = {
        'labelWords': '',
        'fromSearch': 'true',
        'suginput': '',

    }
    response = requests.get(url=url, params=params, headers=headers)
    cookies = response.cookies.get_dict()
    return cookies


def get_info(cookies):
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    headers = {
        'origin': 'https://www.lagou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'authority': 'www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    }
    params = {
        'needAddtionalResult': 'false',
    }
    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python',
        'sid': '',
    }
    response = requests.post(url=url, headers=headers, params=params, data=data, cookies=cookies)
    ls = response.json()['content']['positionResult']['result']
    for work in ls:
        print(work["city"], work["companyFullName"], work["companySize"], work["education"], work["positionName"], work["salary"], work["workYear"])


if __name__ == '__main__':
    cookie = get_cookies()
    get_info(cookie)
