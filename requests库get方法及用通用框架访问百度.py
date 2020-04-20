#1.reqeust库的get（）方法
import requests
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(type(r))
# print(r.headers)
# print(r.text)
# print(r.encoding)
# print(r.apparent_encoding)
# r.encoding = "utf-8"
# print(r.text)

#2.示例 用通用框架来访问百度

def getHTMLtext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLtext(url))
