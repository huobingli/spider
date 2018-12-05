from __future__ import print_function
import torndb


def  get_mysql_conn():

    return torndb.Connection(
        host = mysql["host"] + ":" + mysql["port"],
        database = mysql["database"],
        user = mysql["user"],
        password = mysql["password"],
        charset = "utf8")


mysql = {
        "host": "127.0.0.1",
        "port": "3306",
        "database": "test",
        "password": "",
        "user": "root",
        "charset": "utf8"
    }


def  ip2int(ip):

    try:
        hexn = ''.join(["%02X" % long(i) for i in ip.split('.')])
    except Exception, e:
        hexn = ''.join(["%02X" % long(i) for i in '0.0.0.0'.split('.')])
    return long(hexn, 16)


def  int2ip(n):

    d = 256  *  256  *  256
    q = []
    while  d  >  0:
            m, n = divmod(n, d)
        q.append(str(m))
        d = d / 256
    return '.'.join(q)


def  insert_row():

    with open("./ipdata.csv",  'r') as fr:
            lines = fr.readlines()
    nl_p_list = []
    for  l  in  lines:
            ls = l.strip().split(',', 4)
            c1, c2, c3, c4, c5 = ls[0], ip2int(ls[1]), ip2int(ls[2]), ls[3], ls[4]
            nl = [c2, c3, c4, c5]
            nl_p_list.append(nl)

        db = get_mysql_conn()
        db.execute("START TRANSACTION")
        for  i  in  range(len(nl_p_list) / 1000 + 1):
                tmp_nl_p_list = nl_p_list[i * 1000: (i + 1) * 1000]
                ret = db.insertmany(
            'insert into ipdata (startip, endip, country, carrier) values (%s, %s, %s, %s)', tmp_nl_p_list)
            db.execute("COMMIT")

        if  __name__  ==  '__main__':
                insert_row()
              #  print(ip2int('106.39.222.36'))
            with open("./ipdata.csv",  'r') as fr:
                    lines = fr.readlines()
            nl_p_list = []
            for  l  in  lines:
                    ls = l.strip().split(',', 4)
                    c1, c2, c3, c4, c5 = ls[0], ip2int(ls[1]), ip2int(ls[2]), ls[3], ls[4]
                    nl = [c2, c3, c4, c5]
                    nl_p_list.append(nl)
                import random
                import time
                ip_list = map(lambda  x: x[1], random.sample(nl_p_list, 100))
                db = get_mysql_conn()
                ret_list = []
                  # {0}表名
                sql_tmp = 'select {0}.* from (SELECT * FROM `test`.ipdata where %s>=startip order by startip Desc limit 1) {0}'
                sql_list = []
                  # 拼接一个很长的sql
                for  i  in  range(len(ip_list)):
                        sql_list.append(sql_tmp.format('t' + str(i))  %  ip_list[i])
                    sql = ' union all '.join(sql_list)
                    t0 = time.time()
                      #  for row in db.query(sql):
                      #      print(row)
                    dict(zip(ip_list, db.query(sql)))

                    t1 = time.time()
                    for  ip  in  ip_list:
                            ret = db.get(
                        'SELECT * FROM `test`.ipdata where %s>=startip order by startip Desc limit 1', ip)
                        startip, endip = ret.get('startip'), ret.get('endip')
                            if  startip  <=  ip  <=  endip:
                                    ret_list.append((ip, ret.get('country')))
                                else:
                                    ret_list.append((ip, u"unknown"))
                            t2 = time.time()
                            print(t1 - t0)
                            print(t2 - t1)
