import pymysql
#pip install pymysql
#pip install cryptography
conn = pymysql.connect(host="106.52.76.229",port=3306, user="root", password="Therzyx@123", database="autoSign")
# 得到一个可以执行SQL语句的光标对象
#cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
 
# 定义要执行的SQL语句
sql = "select * from WorkDate"

# 执行SQL语句
cursor.execute(sql)
row = cursor.fetchone()
print(row)
# 关闭光标对象
cursor.close()
 
# 关闭数据库连接
conn.close()