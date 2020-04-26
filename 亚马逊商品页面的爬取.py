import requests
kv = {"user-agent":"Mozilla/10.0"}
url = r"https://www.amazon.cn/dp/B07KSBTCCH/ref=sr_1_1?dchild=1&pf_rd_i=1478512071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_p=c34ba49d-561d-46bc-8df5-4e0f8ddd3dc3&pf_rd_r=WHRZJ73A4EMAXR5BHPST&pf_rd_s=merchandised-search-top-1&pf_rd_t=101&qid=1587401907&s=gifts&sr=1-1"
r = requests.get(url,headers=kv)

print(r.status_code)
print(r.encoding)
r.encoding = r.apparent_encoding
print(r.text)
# print(r.request.headers)


