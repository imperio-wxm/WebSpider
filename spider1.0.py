#!/usr/bin/env python
#-*- coding:UTF-8 -*-
__author__ = 'wxm-Imperio'

import urllib2,urllib

url = "http://www.baidu.com"

# 用一个Request对象来映射你提出的HTTP请求
# req = urllib2.Request(url)
# 通过调用urlopen并传入Request对象，将返回一个相关请求response对象
# response = urllib2.urlopen(req)
# the_page = response.read().decode('UTF-8')
# print(the_page)

values = {
    'name':'wxmimperio',
    'location':'shanghai',
    'language':'python'
}

# 编码工作
data = urllib.urlencode(values)
# 发送请求的同时传递data数据
req = urllib2.Request(url, data)
# 接收反馈信息
response = urllib2.urlopen(req)
# 读取反馈内容
the_page = response.read().decode('UTF-8')

print the_page


