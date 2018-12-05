'''
需求：
继续模拟登录函数。
编写函数装饰器，为多个函数加上认证功能
（用户的账号密码来源于文件，文件内容请自定义，
请使用上下文管理协议读取文件）。
要求登录成功一次，在超时时间（2分钟）内无需重复登录，
超过了超时时间，则必须重新登录。
'''
import time


def authentication(func):
    user = {'name': None, 'login_time': None, 'timeout': 120}  # 这里需要非常注意，一开始我弄成了全局变量，没有考虑，后面修改这里面的值就有问题了，放在装饰器里，就不用考虑了

    # 作用是存放我们需要知道的用户名还有运行函数的时间还有timeout的时间

    def wrapper(*args, **kwargs):
        if user['name']:
            timeout = time.time() - user['login_time']  # 执行时间
            if timeout < user['timeout']:  # 执行时间小于timeout的时间就直接返回函数，如果超时了，就往下执行，重新登录验证
                return func(*args, **kwargs)
        # else:
        filename = 'loginfile.txt'  # 因为放在同一目录下，所以用相对路径
        with open(filename, 'r') as file:
            line = file.readline()
        login_dict = eval(line)  # 将字符串str当成有效的字典表达式来执行并返回结果（一个字典）
        # 这里需要注意的是loginfile里面需要存放字典
        while True:
            name = input("请输入用户名：").strip()  # 忽略输入的前后空格
            password = input("请输入密码：").strip()
            if name == login_dict['name'] and password == login_dict['password']:
                func(*args, **kwargs)
                user['name'] = name  # 修改用户名，一旦登录了，在timeout以内就不需要重新登录
                user['login_time'] = time.time()  # 记录登录函数的运行时间
                break
            elif name == 'user' and password != 'password':
                print("密码错误！")
            else:
                print("用户名错误！")

    return wrapper


@authentication
def login():
    print("登录成功！")
    print(time.asctime(time.localtime(time.time())))  # 将time.time()返回的当前时间的时间戳转换成当前时间
    time.sleep(121)


@authentication
def login_other_function():
    print("login_other_function.")
    print(time.asctime(time.localtime(time.time())))


def main():
    login()
    login_other_function()


main()
