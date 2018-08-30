#-- coding: utf-8 --

import urllib.request
import http.cookiejar

url = "http://www.baidu.com"

print("第一种方法")
response1 = urllib.request.urlopen(url)
# print(urllib.request.__file__)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法")
response2 = urllib.request.Request(url)
response2.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(response2)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())


