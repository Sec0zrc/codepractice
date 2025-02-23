from pyquery import PyQuery

# html = """
#     <ul>
#     <li class="aaa"><a href="www.baidu.com">baidu</a></li>
#     <li class="bbb" id='bb'><a href="www.google.com">google</a></li>
#     <li class="ccc"><a href="www.sougou.com">sougou</a></li>
#     <li class="aaa"><a href="www.aaa.com">aaa</a></li>
#     <li class="ccc"><a href="www.ccc.com">ccc</a></li>
#     <li class="ddd"><a href="www.ddd.com">ddd</a></li>
#     </ul>
# """
# div = """
#     <div><span>hello world!</span></div>
# """
# p = PyQuery(html)
# # 链式操作
# # a = p("li")("a").text()
# # print(a)
# # 后代选择器  "li a"表示li标签里的a标签
# a = p("li a").text()
# print(a)
#
# # 多个标签拿属性
# it = p("li a").items()
# for i in it:
#     print(i.attr("href"))
#
# # 根据id获取标签
# tag = p("#bb a").text()
# print(tag)
#
# # 直接从attr()返回 默认返回第一个标签的属性
# href = p("li a").attr("href")
# print(type(href))
# print(href)
#
# # .html()和.text()方法的区别
# d = PyQuery(div)
# print(d("div").html())  # 输出div内的所有内容，包括html标签
# print(d("div").text())  # 输出div内的所有文本内容，不包括html标签


# 修改html结构
html = """
<HTML>
    <div class="aaa">aaa</div>
    <div class="bbb">bbb</div>
</HTML>
"""

p = PyQuery(html)

# 在div标签后面添加新标签
p("div.aaa").after("""<div class="ccc">ccc</div>""")
# 在div标签内添加标签
p("div.aaa").append("""<span>helo</span>""")
print(p)

# 修改div标签属性
p("div.bbb").attr("class", "aaa")
# 添加新的标签属性
p("div.aaa").attr("id", "111")
# 删除标签属性
p("div.aaa").remove_attr("id")
# 删除标签
p("div.aaa").remove()
print(p)
