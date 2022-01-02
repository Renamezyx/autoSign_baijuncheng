
import pymysql
from Until import *
#pip install pymysql
#pip install cryptography

def addPlan(dateList):
    #addPlan
    #eg: addPlan(createWorkDate("2021-12-08 00:00:00",5)) 
    #连接数据库
    conn = pymysql.connect(host="106.52.76.229",port=3306, user="root", password="Therzyx@123", database="autoSign")
    for date in dateList:
        # 获取一个光标
        cursor = conn.cursor()
        # 定义sql语句
        sql = 'INSERT INTO WorkDate(Date,InTime,OutTime) VALUES (%s,%s,%s);'
        data = [(date["Date"],date["InTime"],date["OutTime"])]
        # 拼接并执行sql语句
        cursor.executemany(sql, data)
        # 涉及写操作要注意提交
        conn.commit()
        # 关闭连接
        cursor.close()
    conn.close()
def changeState(date,state):
    #changeState state:0,1,2
    #eg: changeState("2021-12-08 00:00:00",1)
    #连接数据库
    conn = pymysql.connect(host="106.52.76.229",port=3306, user="root", password="Therzyx@123", database="autoSign")
    # 获取一个光标
    cursor = conn.cursor()
    # 定义sql语句
    sql = 'UPDATE WorkDate SET State = %s WHERE Date = %s;'
    data = [(str(state),date)]
    # 拼接并执行sql语句
    cursor.executemany(sql, data)
    # 涉及写操作要注意提交
    conn.commit()
    # 关闭连接
    cursor.close()
    conn.close()

def findPlanToday():
    #连接数据库
    conn = pymysql.connect(host="106.52.76.229",port=3306, user="root", password="Therzyx@123", database="autoSign")
    # 获取一个光标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * from WorkDate where IF((select State from WorkDate where TO_DAYS(Date) = TO_DAYS(NOW()))<>2,TO_DAYS(Date) = TO_DAYS(NOW()),TO_DAYS(Date) = TO_DAYS(NOW()) + 1) '
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭连接
    cursor.close()
    
    conn.close()
    return result
addPlan(createWorkDate("2021-12-27 00:00:00",5)) 