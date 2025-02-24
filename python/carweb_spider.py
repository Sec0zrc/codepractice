"""
scrap info from https://k.autohome.com.cn/146/index_1.html
get carname, mileage, gearbox, price, number, monthly-loan-price, target_url
1. get html source code
2. parse html and extract target information
3. save in file
"""
import requests
from pyquery import PyQuery as pq


def main():
    url = "https://hkcartrader.com/zh/"
    html = get_html_source(url)
    parse_html_source(html)


def get_html_source(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    html = resp.text
    return html


def parse_html_source(html):
    p = pq(html)
    div = p("section.premium-list-section > div > div:nth-child(2) ")
    car_list = div("a.car-item").items()
    f = open("carinfo.csv", "w", encoding="utf-8")
    # parse car_list
    for car in car_list:
        car_name = car("figcaption.caption > div").eq(0).text()
        # if not contains div.more-info  car_name = None
        if not car("figcaption.caption").children('.more-info'):
            car("figcaption.caption").children('div').eq(0).before('<div class="more-info">None</div>')
            car_name = None

        mileage = car("figcaption.caption > div:nth-child(2)").text().replace("行駛里數: ", "").replace(" 公里", "")
        gearbox = car("figcaption.caption > div:nth-child(3)").text().replace("波箱: ", "")
        soldtimes = car("figcaption.caption > div:nth-child(4)").text().replace("首數:", "")
        car_heading = car("div.car-heading > h3").text().strip()
        price = car("div.car-heading > span.price").text()
        f.write(f"{car_name},{mileage},{gearbox},{soldtimes},{car_heading},{price}\n")

    f.close()
    print("网页内容爬取完毕")


if __name__ == '__main__':
    main()
