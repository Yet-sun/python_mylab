from pymysql import *
import mysql.connector

class UseDataBase(object):
    def __init__(self,data_test,password):
        #创建Connection连接，在上下文管理器中连接数据库连接
        self.conn = connect(host='localhost',port=3306,database=str(data_test),user='root',password=str(password),charset='utf8')
        #获得Cursor(游标)对象
        self.cs1=self.conn.cursor()

    def __enter__(self):
        return (self.cs1,self.conn)#这里返回的两个参数，就是with语句中传入的两个参数

    def __exit__(self, type, value, tb):
        self.cs1.close()
        self.conn.close()

with UseDataBase("data_test","") as (udb,dbconn):#,dbcoon):
    count = udb.execute("select * from TestTable;")
    content = udb.fetchall()#fetchall(self):接收全部的返回结果行.
    #print(connect)
    for i in range(len(content)):
        print(content[i])
        i += 1

    #udb.execute("insert into TestTable(id,name,class,sex) values('22','李七','软件工程','女')")
    #dbconn.commit()