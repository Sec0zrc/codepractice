"""
scrap the info from https://dygod.org/index.htm

1. scrap the child_url from 2023新片精品
2. scrap movie name and download link
3. save info in dygod.csv
"""
import requests
import re


def get_movieinfo(url_path, regobj, file):
    response = requests.get(url_path)
    response.encoding = "gbk"
    content = response.text
    result = regobj.finditer(content)

    for i in result:
        name = i.group("name")
        link = i.group("link")
        file.write(f"{name}, {link}\n")


if __name__ == "__main__":
    url = "https://dygod.org/index.htm"

    # get the area of movie
    movie_regobj = re.compile(r"<p><strong>2023新片精品.(?P<html>.*?)</table>", re.S)
    # get the child page url
    url_regobj = re.compile(r"</a>]<a href='(?P<href>.*?)'>")
    # get movie info
    info_regobj = re.compile(r"◎片　　名(?P<name>.*?)<br />.*?(?P<link>magnet:\?.*?)\">")

    # save info in file
    f = open("dygod.csv", "w", encoding="utf-8")

    # get the area of movie
    resp = requests.get(url)
    resp.encoding = "gbk"
    content1 = resp.text
    html = movie_regobj.search(content1).group("html")
    # print(html)
    # get the child_page url
    result2 = url_regobj.finditer(html)
    for item in result2:
        child_page = "https://dygod.org/" + item.group("href")
        get_movieinfo(child_page, info_regobj, f)

    f.close()
    resp.close()
