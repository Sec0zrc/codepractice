import requests

headers = {
    "referer": "https://meirentu.cc/pic/286468453534.html"
}
resp = requests.get("https://cdn20.mmdb.cc/file/20240620/271835001642/0.jpg", headers=headers)
print(resp.status_code)

