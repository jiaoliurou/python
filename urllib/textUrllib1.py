# -*- coding: utf-8 -*-
# @Time : 2021/7/3 13:27
# @Author : 焦熘肉
# @File : textUrllib1.py
# @Software: : PyCharm
import urllib.request
import urllib.parse
'''#post一般用于模拟网络用户登陆的内容，这里还要加入cookie的信息登录密码等
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")#转化成字节文件
response = urllib.request.urlopen("http://httpbin.org/post",data= data)#把data信息封装后发给网页，才能反馈网页信息
print(response.read().decode("utf-8"))#使用decode（“utf-8”）解码网页信息会准确防止中文乱码'''
#get请求
'''try:#超时处理,防止爬取过程中出现问题然后可以跳过
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)#timeout=0.1设置缓冲时间，防止被拉黑或网速不够加载不出
    print(response.read().decode("utf-8"))#使用decode（“utf-8”）解码网页信息会准确防止中文乱码
except urllib.error.URLError as e:
    print("time out!")'''
'''#获取headers信息
response = urllib.request.urlopen("http://www.baidu.com",timeout=1)
print(response.status)#返回200是状态码或404
print(response.getheaders())#获取所有header信息 加s，
print("\n")#输出\要用\\，输出换行或者空格就用\一个斜杠,这一句输出的回撤
print("\\n")#输出\要用\\,加上r就是里面些什么就是什么，输出换行或者空格就用\一个斜杠，这一句输出的\n
print(r"\\n")#输出\要用\\，输出换行或者空格就用\一个斜杠，这一句输出的\\n
print(response.getheader("Cookie"))#获取header里单独的value数值，不加s
'''
#以字典的形式发给网站，我们不是爬虫而是浏览器，具体内容在随便进入一个网站，f12-网络-找一段时间-点左下区域网页名-右下区域最后的user-agent中，复制后用字典{}的形式，保存在header里
#具体需要哪些 封装内容就打开一次想登陆网站，找headers的内容封装
"""url="http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding='utf-8')
headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")#这个是封装request的对象作为信息，登陆网站时会把这个信息发给网站，避开网站爬虫认定最重要的是headers
response = urllib.request.urlopen(req)#需要一个响应项，有这个信息的response
print(response.read().decode("utf-8"))"""
url="http://www.douban.com"
headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)#需要一个响应项，有这个信息的response
print(response.read().decode("utf-8"))