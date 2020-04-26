import requests
kv = {"wd":"python"}
r = requests.get("https://www.baidu.com/s",params=kv)
print(r.status_code)
# print(r.text)
print(r.request.url)