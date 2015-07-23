#!/usr/bin/env python
#-*- coding:UTF-8 -*-
__author__ = 'wxm-Imperio'

import re
import urllib2

from collections import deque

# 定义队列
queue = deque()
# 定义集合，用来标记URL是否访问过
visited = set()

# 起始页面
url = 'http://www.baidu.com'

# 将起始页面加入队列
queue.append(url)
# 计数器
cnt = 0

while queue:
    # 队首元素出队
    url = queue.popleft()
    # 标记为此页面已经访问
    visited |= {url}
    print('已经抓取：' + str(cnt) + '    正在抓取<--' + url.encode('UTF-8'))
    # 抓取记录计数
    cnt += 1

    # 用一个Request对象来映射你提出的HTTP请求
    req = urllib2.Request(url)
    # 通过调用urlopen并传入Request对象，将返回一个相关请求response对象
    urlop = urllib2.urlopen(req)

    # 如果抓到的不是html页面，继续
    # if 'html' not in urlop.read('Content-Type'):
    #     continue

    # 避免程序异常终止，用try...catch处理异常
    try:
        data = urlop.read().decode('UTF-8')
    except:
        continue

    # 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列--->' + x.encode('UTF-8'))