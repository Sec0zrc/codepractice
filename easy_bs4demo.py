"""
a simple case  to use BS4
try to use bs4 to get the data from website
target url :https://www.dytt8.com/
get the movie name and download address
1. get child page url
2. get movie name and download addr
3. save data in dianyin.csv

"""

import requests
from bs4 import BeautifulSoup


def get_childpage(url_path):
    childpage_url = []
    response = requests.get(url_path)
    response.encoding = "gbk"
    page = response.text
    page_bs = BeautifulSoup(page, "html.parser")
    divs = page_bs.find("div", attrs={"class": "co_content2"})
    a_list = divs.find_all("a")
    for a in a_list:
        childpage_url.append(a.get("href"))

    return childpage_url


def getinfo(url_list, file):
    domain = "https://www.dytt8.com"
    for i in url_list:
        resp = requests.get(f"{domain}{i}")
        resp.encoding = "gbk"
        result = resp.text
        page_bs = BeautifulSoup(result, "html.parser")
        # get movie name
        td = page_bs.find("td", attrs={"align": "center"})
        name = td.find_all("font")[0].get_text()
        # get movie download addr
        down_addr = td.find("a").get("href")
        file.write(f"{name},{down_addr}\n")
        resp.close()


if __name__ == "__main__":
    url = "https://www.dytt8.com/"
    # skip the first url
    childpages_url = get_childpage(url)[1:]
    f = open("dianyin.csv", "w", encoding="utf-8")
    getinfo(childpages_url, f)
    f.close()
    print("网页爬取完毕")
