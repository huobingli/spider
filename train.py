#!/usr/bin/python#
# -*- coding: UTF-8 -*-
import urllib
import urllib3
import re
import requests


train_list_url = "https://kyfw.12306.cn/otn/resources/js/query/train_list.js?scriptVersion=1.0"
station_list_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002"

train_raw_file = 'train_list.txt'
station_raw_file = 'station_list.txt'

train_cooked_file = 'train_list_format.txt'
station_cooked_file = 'station_list_format.txt'


# 下载所有的车次数据  保存为 train_list.txt文件
def getTrain_list():
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests.get(train_list_url, stream=True, verify=False)
    status = response.status_code
    if status == 200:
        with open(train_raw_file, 'wb') as of:
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:
                    of.write(chunk)


# 分析train_list.txt文件 得出火车 出发站到终点站的数据
def trainListStartToEnd():
    global station_start_end_set
    with open(train_raw_file, 'rb') as of:
        text = of.readline()
        tt = text.decode("utf-8")
        ss = tt.replace("},{", "}\n{").replace("2018-", "\n").replace("[", "\n").split("\n")
        m_list = list()
        for s in ss:
            pattern = re.compile(r'\((\w+-\w+)\)')
            match = pattern.search(s)
            if match:
                m_list.append(match.group(1))

        fp = open(train_cooked_file, 'w+', encoding='utf-8')
        fp.write("{" + '\n')
        for i in range(len(m_list)):
            str1 = str(m_list[i])#.encode("utf-8")
            #str1 = str1.encode("utf-8")
            fp.write(str1)
            fp.write("," + "\n")
        fp.write("}")
        fp.close()
        station_start_end_set = set(m_list)

def getStationInfo():
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests.get(station_list_url, stream=True, verify=False)
    status = response.status_code
    if status == 200:
        with open('station_list.txt', 'wb') as of:
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:
                    of.write(chunk)

# 分析station_list.txt文件 得出各个站点的数据
def stationList():
    global station_set
    with open(station_raw_file, 'rb') as of:
        text = of.readline()
        tt = text.decode("utf-8")
        ss = tt.replace("@", "\n@").split("\n")
        m_list = list()
        for s in ss:
            pattern = re.compile(r'@[0-9a-zA-Z\_\|]+')
            match = pattern.search(s)
            if match:
                m_list.append(match.string)

        fp = open(station_cooked_file, 'w+', encoding='utf-8')
        fp.write("{" + '\n')
        for i in range(len(m_list)):
            str1 = str(m_list[i])#.encode("utf-8")
            #str1 = str1.encode("utf-8")
            fp.write(str1)
            fp.write(";" + "\n")
        fp.write("}")
        fp.close()
        station_set = set(m_list)

def test():
    s1 = "@1|23|456@65|4321"
    ss = s1.replace("@", "\n@").split("\n")
    for s in ss:
        pattern = re.compile(r'@[0-9a-zA-Z\_\|]+')
        match = pattern.search(s)
        if match:
            print(match)

if __name__ == "__main__":
    #getTrain_list()
    #trainListStartToEnd()
    #getStationInfo()
    stationList()
    #test()