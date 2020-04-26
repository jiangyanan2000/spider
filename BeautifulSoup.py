"""
BeautifulSoup库是解析、遍历、维护、“标签树”的功能库

"""
import requests
from bs4 import BeautifulSoup
url = r"https://python123.io/ws/demo.html"
r = requests.get(url)
# print(r.text)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())
# print(soup.title)

