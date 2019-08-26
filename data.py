# -*- coding: utf-8 -*-#

"""
File         :      data.py
Description  :  
Author       :      赵金朋
Modify Time  :      2019/5/24 18:01
爬虫test
"""
#爬取网页通用框架
import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__ == '__main__':
    url="http://www.baidu.com"
    print((getHTMLText(url)))