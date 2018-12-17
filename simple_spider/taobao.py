import re
import requests

tar_url = "https://rate.taobao.com/detailCommon.htm"

# 商品链接
refer = "https://item.taobao.com/item.htm?spm=a230r.1.14.119.76bf523Zih6Ob&id=548765652209&ns=1&abbucket=12"
# 从商品链接中提取商品ID
NumId = re.findall(r"id=(\d+)\&", refer)
# 参数
param = {"auctionNumId": NumId,
         "userNumId": "43440508",
         "callback": "json_tbc_rate_summary"}
# 头部信息
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, compress',
          'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive',
          'Upgrade-Insecure-Requests': "1",
          'Referer': refer,
          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0"
          }

try:
    url_content = requests.get(url=tar_url, params=param, headers=header)
    print("url_content: ", url_content.text)
except BaseException as e:
    pass
