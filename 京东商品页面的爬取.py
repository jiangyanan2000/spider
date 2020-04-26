import requests
r = requests.get("https://item.jd.com/100012686070.html")
print(r.status_code)
print(r.encoding)
r.encoding = r.apparent_encoding
print(r.text)