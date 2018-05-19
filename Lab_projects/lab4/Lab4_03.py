'''
    需求:根据实验三中，基于Mysql或者MariaDB新建的测试表：TestTable，
    编写一个可以根据传入的任何SQL语句读取数据的函数，并加入异常处理，
    编写一个可以根据传入的任何SQL语句执行数据操作的函数，也同样加入异常处理。
    （要求：不使用上下文协议管理器）
'''

import mysql.connector


def readData(cursor):
    try:
        cursor.execute("select * from TestTable;")
        content = cursor.fetchall()
        for i in range(content.__len__()):
            print(content[i])
            i += 1
    except Exception as e:
        print("检测到错误：", e)


def excuteData(sql, cursor):
    try:
        cursor.execute(sql)
    except Exception as e:
        print("检测到错误：", e)


def main():
    try:
        conn = mysql.connector.connect(user='root', password='password', database='data_test', buffered=True)
        cursor = conn.cursor()
        sql = "insert into TestTable(id,name,class,sex) values('18','吴二','软件工程','男')"
        readData(cursor)
        excuteData(sql, cursor)
        conn.commit()

        conn.close()
        cursor.close()
    except Exception as e:
        print("检测到错误：", e)


main()
