'''
需求：
编写类装饰器，为模拟登陆函数加上用户认证的功能。
'''


def authentication(func):
    def wrapper(*args, **kwargs):
        while True:
            name = input("请输入用户名：").strip()  # 忽略输入的空格
            password = input("请输入密码：").strip()
            if name == 'user' and password == 'password':
                func(*args, **kwargs)  # 登陆成功
                break  # 退出循环
            elif name == 'user' and password != 'password':
                print("密码错误！")
            else:
                print("用户名错误！")

    return wrapper


@authentication  # 在不改变原有的函数基础上加上用户登陆认证的功能
def login(name):
    print('欢迎登陆！{0}'.format(name))


def main():
    login('user')


main()
