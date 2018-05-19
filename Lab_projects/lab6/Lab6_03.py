'''
需求：
继续模拟登录函数。
编写函数装饰器，为多个函数加上认证的功能
（用户的账号密码来源于文件，文件内容请自定义，
请使用上下文管理协议读取文件）。
要求登录成功一次，后续的函数都无需再输入用户名和密码。
'''

user_name = {'name': None}


def authentication(func):
    def wrapper(*args, **kwargs):
        if user_name['name']:  # 如果用户名不为空，则直接运行被装饰的函数
            func(*args, **kwargs)
        else:  # 用户名为空，需要登录验证
            filename = 'loginfile.txt'  # 因为放在同一目录下，所以用相对路径
            with open(filename, 'r') as file:
                line = file.readline()
            login_dict = eval(line)  # 将字符串str当成有效的字典表达式来执行并返回结果（一个字典）
            # 这里需要注意的是loginfile里面需要存放字典
            while True:
                name = input("请输入用户名：").strip()  # 忽略输入的空格
                password = input("请输入密码：").strip()
                if name == login_dict['name'] and password == login_dict['password']:
                    func(*args, **kwargs)
                    user_name['name'] = name  # 将用户名置为非空，这样后续的函数就无需再输入密码和用户名了
                    break
                elif name == 'user' and password != 'password':
                    print("密码错误！")
                else:
                    print("用户名错误！")

    return wrapper


@authentication
def login():
    print("登陆成功！")


@authentication
def login_other_function():
    print("login_other_function.")


def main():
    login()
    login_other_function()


main()
