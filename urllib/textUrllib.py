# -*- coding: utf-8 -*-
# @Time : 2021/7/3 12:27
# @Author : 焦熘肉
# @File : textUrllib.py
# @Software: : PyCharm

from bs4 import BeautifulSoup #网页解析·获取数据
import re#正则表达·进行文字匹配
import urllib   #定制URL·获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
    basurl="https://movie.douban.com/top250?start"
    #1爬取网页
    datalist = getDate(basurl)
    savepath=".\\豆瓣电影Top250.xls"#这里想写斜杠，要写成双\\表示\要不然就表示成转义字符了，也可前面加r向下一句所示，点前面省略的是文件夹所在地址
    #savepath = r".\"
    #3保存数据
    saveData(savepath)
    #changshi


#爬取网页
def getDate(baseurl):
    datalist = []
    # 2逐一解析数据
    return datalist

def saveData(savepath):
    print("save...")
if __name__ == "__main__":#当程序执行时，默认名字就是main
#调用函数
    main()