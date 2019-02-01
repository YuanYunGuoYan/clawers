#!/usr/bin/env python3
# -*- coding: utf-8
# author:wangqiyang
import re
import pymysql
import csv
import time
import requests
import multiprocessing
import random
import codecs
from bs4 import BeautifulSoup

# 假装不同的浏览器，这次暂时没有用上。
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; InfoPath.2; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET CLR 1.1.4322)',
]
# 这个实际不用写这么多，为了防止被封，就多写点吧
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    # user_agent_list[random.randint(0, 5)],
    'Connection': 'keep-alive',
    'Cookie': '这里粘贴自己cookie',
    'Host': 'www.ireadweek.com',
    'Referer': 'http://www.ireadweek.com/index.php/Index/index.html',
    'Upgrade-Insecure-Requests': '1'
}


def get_index_url(url):
    wbdata = requests.get(url, headers=header).content
    soup = BeautifulSoup(wbdata, 'html.parser')
    links = soup.select('html > body > div > div > ul > a')
    for link in links:
        try:
            time.sleep(random.randint(1, 3))
            page_url = link.get('href')
            print("page_url:" + "http://www.ireadweek.com" + page_url)
            book_page_url = "http://www.ireadweek.com" + page_url
            wbdata2 = requests.get(book_page_url, headers=header).content.decode('utf-8')
            # print(wbdata2)
            soup2 = BeautifulSoup(wbdata2, 'html.parser')
            dowrload_url = "NONE"
            dowrload_url = soup2.select(
                'html > body > div > div > div.hanghang-za > div.hanghang-box > div.hanghang-shu-content-btn > a')[
                0].get('href')
            print(dowrload_url)
            # body > div > div > div.hanghang - za > div.hanghang - shu - content > div.hanghang - shu - content - font > p: nth - child(1)
            author = soup2.select(
                'html > body > div > div > div.hanghang-za > div.hanghang-shu-content > div.hanghang-shu-content-font > p')[
                0].text
            print(author)
            category = soup2.select(
                'html > body > div > div > div.hanghang-za > div.hanghang-shu-content > div.hanghang-shu-content-font > p')[
                1].text
            print(category)
            book_info = soup2.select(
                'html > body > div > div > div.hanghang-za > div.hanghang-shu-content > div.hanghang-shu-content-font > p')[
                4].text
            print(book_info)
            # body > div > div > div.hanghang - za > div: nth - child(1)
            book_name = soup2.select('html > body > div > div > div.hanghang-za > div.hanghang-za-title')[0].text
            print(book_name)

            with open("C:/BookDownload.csv", 'a', encoding='gb18030', newline='') as f:
                try:
                    # f.write(codecs.BOM_UTF8)
                    f.write(book_name)
                    f.write(',')
                    f.write(author)
                    f.write(',')
                    f.write(category)
                    f.write(',')
                    f.write(dowrload_url)
                    f.write(',')
                    f.write("\n")
                except:
                    pass
        except:
            print("link not found!!!" + link)
            pass


if __name__ == "__main__":
    try:
        pool = multiprocessing.Pool(processes=8)
        print("---------------------1---------------")
        for i in range(1, 219):
            url = "http://www.ireadweek.com/index.php/index/" + str(i) + ".html"
            print("---------------------2---------------" + url)
            pool.apply_async(get_index_url, args=(url,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    except:
        print('abort')