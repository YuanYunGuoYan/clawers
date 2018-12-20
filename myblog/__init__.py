import requests

if __name__ == "__main__":
    tar_url = "http://45.77.71.217"
    param = {"page_id": 10}  # 请求头的参数
    header = {  # 请求头部
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://45.77.71.217/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    url_response = requests.get(url=tar_url, params=param)
    print(url_response.status_code, url_response.text)
