import requests
# r = requests.head("http://httpbin.org/get")
# print(r.headers)

#post()方法
# payload = {"key1":"value1","key2":"value2"}
# r = requests.post("http://httpbin.org/post",data=payload)
# r.raise_for_status()
# print(r.text)

r = requests.post("http://httpbin.org/post",data= "ABc")
print(r.text)