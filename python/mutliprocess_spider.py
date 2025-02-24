"""
use multiprocess to handle task
download image from https://meirentu.cc/
step: 1. get image src from https://meirentu.cc/
      2. download images

use Queue to transfer information in multiprocess
use urllib to parse url
"""

import requests
from lxml import etree
from urllib import parse
from multiprocessing import Process
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor


def get_image_src(src, queue):
    resp = requests.get(src)
    resp.encoding = "utf-8"
    et = etree.HTML(resp.text)

    href_lists = et.xpath("//div[@class='update_area_content']/ul/li/a/@href")
    for href in href_lists:
        child_page = parse.urljoin(src, href)
        child_page_result = requests.get(child_page)
        child_page_result.encoding = "utf-8"
        tree = etree.HTML(child_page_result.text)
        image_lists = tree.xpath("//div[@class='content_left']//img/@src")
        # need child_page url to bypass Refer check
        image_source = [child_page, image_lists]
        queue.put(image_source)

    print("所有图片链接抓取完毕")
    queue.put("222")


def download(src, refer, name):

    headers = {
        "referer": refer
    }
    # print(f"下载地址:{src}, Refer地址：{refer}\n")
    resp = requests.get(src, headers=headers)
    with open(f"./image/{name}", mode="wb") as f:
        f.write(resp.content)


def download_image(queue):
    with ThreadPoolExecutor(10) as t:
        while True:
            src = queue.get()
            if src == "222":
                break
            else:
                refer = src[0]      # 第一项为Refer地址
                for i in src[1]:
                    name = i.split("/")[-1]
                    t.submit(download, i, refer, name)

    print("所有图片下载完毕！")


if __name__ == '__main__':
    url = "https://meirentu.cc/"
    q = Queue()
    p1 = Process(target=get_image_src, args=(url, q))
    p2 = Process(target=download_image, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
