import requests

if __name__ == '__main__':
    content = input("输入搜索内容：")
    url = f"https://sogou.com/web?query={content}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get(url, headers=headers)
    print(response.status_code)
