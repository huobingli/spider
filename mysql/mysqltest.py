#!/usr/bin/python#
# -*- coding: UTF-8 -*-

import pymysql
import urllib3
import re
import requests


station_cooked_file = 'station_list_format.txt'
train_cooked_file = 'station_list_format.txt'

# 打开数据库连接
# password  651295570aA
# db = pymysql.Connect("111.231.251.80", "root", "651295570aA", "station")

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()


# 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 插入语句
# sql = "INSERT INTO stationTable(station_py, \
#        station_name, station_code, station_pyqc, station_short_code) \
#        VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
#       ('bjd', '北京东', 'BOP', 'beijingdong', 'bjd')
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 执行sql语句
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()
# 打开数据库连接
# password  651295570aA

def station_insert():
    db = pymysql.Connect("111.231.251.80", "root", "651295570aA", "station")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    with open(station_cooked_file, 'rb') as of:
        for line in of:
            # text = of.readline()
            tt = line.decode("utf-8")
            ss = tt.replace("@", "").split("|")

            c0, c1, c2, c3, c4 = ss[0], ss[1], ss[2], ss[3], ss[4]
            c0 = ss[0]
            c1 = ss[1]
            c2 = ss[2]
            c3 = ss[3]
            c4 = ss[4]
            nl = [c0, c1, c2, c3, c4]

            # SQL 插入语句
            sql = "INSERT INTO stationTable(station_py,\
                    station_name, station_code, station_pyqc, station_short_code)\
                     VALUES ('%s', '%s', '%s', '%s', '%s')" % (c0, c1, c2, c3, c4)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()

    # 关闭数据库连接
    db.close()


def train_insert():
    db = pymysql.Connect("111.231.251.80", "root", "651295570aA", "station")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    with open(train_cooked_file, 'rb') as of:
        for line in of:
            # text = of.readline()
            tt = line.decode("utf-8")
            ss = tt.split("-")

            c0, c1 = ss[0], ss[1]
            c0 = ss[0]
            c1 = ss[1]

            nl = [c0, c1]

            # SQL 插入语句
            sql = "INSERT INTO trainTable(train_start,\
                    train_end)\
                     VALUES ('%s', '%s')" % (c0, c1)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    # station_insert()

    train_insert()