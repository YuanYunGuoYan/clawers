import requests
import re

tar_url = "http://45.77.71.217"  # 目标网页
param = {"p": 4622}  # 请求头的参数
proxy = {"http": "http://{}:{}".format("221.8.186.249", "80"),
         "https": "https://{}:{}".format("221.8.186.249", "80")}  # 代理IP
header = {  # 请求头部
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://45.77.71.217/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
url_response = requests.get(url=tar_url, params=param, headers=header)
print(url_response.text)

regex = re.findall(r'url\(\"?(.*?)\"?\)', url_response.text)[1]
print(regex)
src = re.findall(r'src=\"(.*?)\"', url_response.text)[0]
print(src)
#  从图片链接中提取图片名
img_name = re.findall(r'([^/]+.png)', src)[0]
#  请求
image_response = requests.get(url=src, headers=header)
#  保存图片
with open(img_name, "wb") as fw:
    fw.write(image_response.content)
print(regex)
