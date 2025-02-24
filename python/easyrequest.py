#!/usr/bin/python

from urllib.request import urlopen
import requests


# practice request

# test requests.get
def get():
    req_get = requests.get("https://httpbin.org/get")
    print(req_get.status_code)
    print(req_get.reason)
    print(req_get.apparent_encoding)


def post():
    myobj = {'fname': 'test', 'lname': 'admin'}
    req_post = requests.post("https://httpbin.org/post", data=myobj)
    print(req_post.status_code)
    print(req_post.json())
    pass


# send a post request to Baidu Translate
def post_baidu():
    url = "https://fanyi.baidu.com/sug"
    data = {
        'kw': input("please enter a word: ")
    }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    #                         (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    # }
    response = requests.post(url, data=data)
    return response


def header():
    # set header
    keyword = {'name': "lihua"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    res = requests.get("https://httpbin.org/get", params=keyword, headers=headers)
    # print(response.status)
    # print(response.encode)
    # print(response.url)
    print(res.status_code)


def use_urlopen():
    url = "http://www.baidu.com"
    response = urlopen(url)
    # print(response.read().decode("utf-8"))
    return response


def get_douban():
    url = "https://movie.douban.com/j/chart/top_list"
    params = {
        'type': '13',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=header)
    print(response.json())


if __name__ == "__main__":
    # get()
    # post()
    # header()
    # res = use_urlopen()
    # with open("baidu.html",mode="w",encoding="utf-8") as f:
    #     f.write(res.read().decode("utf-8"))
    #

    # response = post_baidu()
    # print(response.status_code)
    # print(response.json())
    get_douban()

    pass
