import requests
import os
url = r"http://img0.dili360.com/ga/M02/49/B7/wKgBzFqo8ySAT4nUAAry7yQ0MW4188.tub.jpg"
root = r"C:\Users\Admin\Desktop\1\\"
path = root + url.split("/")[-1]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path,"wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")