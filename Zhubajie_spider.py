"""
using lxml.etree.xpath() to get data
scrap the data from https://www.zbj.com/fw/?k=SaaS
get price | company name | service
"""
import requests
from lxml import etree


if __name__ == "__main__":
    url = "https://www.zbj.com/fw/?k=SaaS"
    resp = requests.get(url)
    et = etree.HTML(resp.text)

    # get price
    divs = et.xpath("//div[@class='search-result-list-service']/div")
    f = open("zbj.csv", "w", encoding="utf-8")
    for div in divs:
        price = div.xpath("./div/div[3]/div[1]/span/text()")[0]
        company = div.xpath(".//div[@class='shop-detail']/div/text()")[0]
        # // mean every node  span//text() ==> span/h1/text() + /span/text()
        service = "".join(div.xpath("./div/div[3]/div[2]//span//text()"))
        f.write(f"{price},{company},{service}\n")

    print("网页数据抓取完毕")

