# #-- coding: utf-8 --
# import re
# import urllib.request
# user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
# headers={'User-Agent':user_agent}
# def getHtml(url):
#     request=urllib.request.Request(url=url,headers=headers)
#     page=urllib.request.urlopen(request)
#     html=page.read().decode('utf-8')
#     #html=page.read()
#     return html
# def getVideo(html):
#     reg=r'data-mp4="(.*?\.mp4)"'
#     imgre=re.compile(reg)
#     imglist=re.findall(imgre,html)
#     x=0
#     for imgurl in imglist:
#         urllib.request.urlretrieve(imgurl,'%s.mp4' %x)
#         x+=1
# html=getHtml('http://www.budejie.com/video/')
# print(getVideo(html))

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import re
import requests
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

url_name = []  # url name

def cbk(a,b,c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0*a*b/c
    if per > 100:
        per = 100
    print('%.2f%%' % per)

def get():
    # 获取源码
    hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = 'http://www.budejie.com/video/'
    html = requests.get(url, headers=hd).text
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)  # 编译
    url_contents = re.findall(url_content, html)  # 匹配

    for i in url_contents:
        # 匹配视频
        url_reg = r'data-original="(.*?)"'  # 图片地址
        url_items = re.findall(url_reg, i)
        # print url_items
        if url_items:  # 判断图片是否存在
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            name_items = re.findall(name_reg, i)
            # print name_items[0]
            for i, k in zip(name_items, url_items):
                url_name.append([i, k])
                print
                i, k
    for i in url_name:  # i[1]=url i[0]=name
        #urllib.request.urlretrieve(i[1], 'video\\%s.mp4' % (i[0].decode('utf-8')))
        urllib.request.urlretrieve(i[1], 'video\\%s.jpg', cbk)


if __name__ == "__main__":
    get()
