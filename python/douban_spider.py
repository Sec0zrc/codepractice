import requests
import re


def scrap_douban(urlpath, start, file, regobj):
    """scrap douban250 movie info
    movie name , director, year, rating_num, rating_people_num"""

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    resp = requests.get(urlpath + f"?start={start}", headers=headers)
    context = resp.text
    result = regobj.finditer(context)

    for item in result:
        name = item.group("name")
        director = item.group("director")
        year = item.group("year").strip()
        rating = item.group("rating")
        number = item.group("number")
        file.write(f"{name}, {director}, {year}, {rating}, {number}\n")
    resp.close()
    pass


if __name__ == "__main__":

    url = "https://movie.douban.com/top250"
    f = open("douban250.csv", "w", encoding="utf-8")
    reobj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                       r'.*?导演: (?P<director>.*?)&nbsp;'
                       r'.*?<br>(?P<year>.*?)&nbsp'
                       r'.*?<span class="rating_num" property="v:average">(?P<rating>.*?)</span>'
                       r'.*?<span>(?P<number>.*?人评价)', re.S)

    for i in range(0, 10):
        scrap_douban(url, str(i), f, reobj)

    f.close()
    print("网页内容爬取完毕")
