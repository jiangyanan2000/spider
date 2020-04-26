import requests
"""
requests.requests(method,url,**kwargs)
method:请求方法，对应get/put/post/等7种
url：拟获取页面的url链接
kwargs:控制访问的参数，共13个，均为可选项
params:字典或者字节序列，作为参数增加到url中
data:字典、字节序列或者文件对象，作为requests的内容
json:JSON格式的数据，作为requests的内容
headers；字典，HTTP定制头
cookies:字典或者CookieJar，requests中cookie
auth:元组，支持HTTP认证功能
files:字典类型，传输文件
timeout:设定超时时间，秒为单位
proxies：字典类型，设定访问代理服务器，可以增加登陆认证
allow_redirects；True/False,默认为True,重定向开关
stream:True/False,默认为True,获取内容立即下载开关
verify:True/False,默认为True,认证SSL证书开关
cert:本地SSL认证

"""