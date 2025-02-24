"""
spider for owsap glossary
https://wiki.owasp.org/index.php/Glossary
scrap the data and save in owsap.csv

"""
import requests
import re

if __name__ == "__main__":

    f = open("oswap.csv", "w", encoding="utf-8")
    url = 'https://wiki.owasp.org/index.php/Glossary'
    pattern = r'<h3><span class="mw-headline" id="(?P<word>.*?)">' \
              r'.*?<p>(?P<mean>.*?)</p>'
    regobj = re.compile(pattern, re.S)
    resp = requests.get(url)
    content = resp.text

    result = regobj.finditer(content)

    for item in result:
        word = item.group("word")
        mean = item.group("mean").strip()
        f.write(f"{word}, {mean}\n")

    f.close()
    resp.close()
    print("spider had down")
