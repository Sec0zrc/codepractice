"""
scarp image from website
use bs4 to select element in html
target url :https://umei.net/i/

1. get the child page url
2. get the image url
3. download image and save in local

"""
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    domain = "https://umei.net"
    childpage_list = []
    imgaddr_list = []
    resp = requests.get("https://umei.net/i")
    resp.encoding = "utf-8"
    result = resp.text
    page = BeautifulSoup(result, "html.parser")
    div = page.find("div", attrs={"class": "update_area"})

    # get child_page
    li_list = div.find_all("li", attrs={"class": "i_list list_n2"})
    for li in li_list:
        href = li.find("a").get("href")
        childpage_list.append(f"{domain}{href}")

    print(childpage_list)
    # get image url
    for i in childpage_list:
        resp_image = requests.get(i)
        resp_image.encoding = "utf-8"
        result = resp_image.text
        image_page = BeautifulSoup(result, "html.parser")
        div = image_page.find("div", attrs={"class": "image_div"})
        img_addr = div.find("img").get("src")
        imgaddr_list.append(img_addr)
        resp_image.close()

    # download image
    count = 0
    for i in imgaddr_list:
        response = requests.get(i)
        result = response.content
        with open(f"{count}.jpg", mode="wb") as f:
            f.write(result)
        count += 1
    print("所有图片下载完毕")
