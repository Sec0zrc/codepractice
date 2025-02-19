import re

if __name__ == "__main__":

    # res = re.match(r"\d+","123jklfajldkfj12 12314  123123")
    # print(res)
    # print(res.group(0))
    # print(res.groups())

    # pattern = re.compile(r"\d+")
    # result1 = re.findall(pattern,"123kdjfaklj123kjflk342")
    # print(result1)
    #
    #
    # result2 = re.findall(r"(\w+)=(\d+)", "set width=20 and height=10")
    # print(result2)

    # it = re.finditer(r"\d+","akjf1231kdjfalksj123kjdfa21")
    # print(it)
    # for item in it:
    #     print(item.group())

    # result1 = re.split(r"\W+", "hello,world!")
    # print(result1)
    #
    # result2 = re.split(r"(\W+)", " hello, world! ")
    # print(result2)
    #
    # result3 = re.split(r"\W+", " hello, world! .")
    # print(result3)

    s = "1102231990xxxxxxxx"
    result = re.search(r"(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})", s)
    print(result.groupdict())
