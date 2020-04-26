import requests
url = r"https://www.ip138.com/iplookup.asp?ip=202.204.80.112&action=2"
try:
    r = requests.get(url)
    print(r.raise_for_status())
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败！")