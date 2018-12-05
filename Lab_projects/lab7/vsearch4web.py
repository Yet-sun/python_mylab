'''
需求：
扩展上课时所讲的针对英文字符串搜索特定字符串的Web简单应用，
要求如下：
1、增加一个管理功能，可以查看每个用户的搜索历史。
需要记录如下数据：
a、每个Web请求的IP。
b、搜索字符串和特定字符串。
c、搜索结果。
d、接收Web请求的时间。
（所有数据必须存储在数据库中，使用之前所学知识解决）
2、增加一个登录页面，只有登录后才能使用所有功能。
也就是说还需要增加登录验证。
（使用装饰器完成，需要增加一个用户表，增加一些虚拟用户信息）
3、增加一个统计功能，可以根据时间或者IP筛选用户查询记录。
'''

import time
from flask import Flask, render_template, request
from useDB import UseDataBase
from vsearch import search4letters


app = Flask(__name__)  # 创建flask对象


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':
    ip = request.remote_addr
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    requesttime = time.strftime("%b %d %Y %H:%M:%S")  # ("%F")   #将当前获取的时间戳转换为当前日期

    with UseDataBase("vsearch", "") as (udb, dbconn):
        udb.execute("insert into searchhistory values(%s,%s,%s,%s,%s);", (ip, phrase, letters, results, requesttime))
        dbconn.commit()

        udb.execute("select * from searchhistory")
        content = udb.fetchall()

    return render_template('results.html',
                           the_ip=ip,
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           the_time=requesttime,
                           the_content=content, )


# @app.route('/')
@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!', )


# 默认路径访问登录页面
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


# 默认路径访问注册页面
@app.route('/regist', methods=['GET', 'POST'])
def regist():
    return render_template('regist.html')

# 默认路径访问统计页面
@app.route('/count', methods=['GET', 'POST'])
def count()-> 'html':
    title = 'Here are the data count:'

    with UseDataBase("vsearch", "") as (udb, dbconn):
        udb.execute("select * from searchhistory")
        content = udb.fetchall()

    return render_template('count.html',
                           the_title=title,
                           the_content=content, )


# 获取注册请求及处理
@app.route('/registuser', methods=['GET', 'POST'])
def getRigistRequest():
    # 连接数据库把用户名和密码注册到数据库中
    with UseDataBase("vsearch", "") as (udb, dbconn):
        # SQL 插入语句
        sql = "INSERT INTO user(user, password) VALUES (" + request.args.get('user') + ", " + request.args.get(
            'password') + ")"
        udb.execute(sql)
        udb.commit()  # 提交到数据库执行
    return render_template('login.html')  # 注册成功之后跳转到登录页面


# 获取登录参数及处理
@app.route('/login', methods=['GET', 'POST'])
def getLoginRequest():
    # 连接数据库,查询用户名及密码是否匹配及存在
    with UseDataBase("vsearch", "") as (udb, dbconn):
        sql = "select * from user where user=" + request.args.get('user') + " and password=" + request.args.get(
            'password') + ""
        udb.execute(sql)
        results = udb.fetchall()
    if len(results) == 1:
        return render_template('entry.html')  # 登录成功后跳转到entry界面
    else:
        return '用户名或密码不正确'
        # 提交到数据库执行
        udb.commit()


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # 自动监听修改重启
