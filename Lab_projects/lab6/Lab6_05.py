'''
需求：
编写日志装饰器，实现功能如：
一旦某个自定义函数执行，则将消息入到日志文件中，
日志文件路径应可以在装饰器上指定。注意：1、时间的格式。
'''
import time, os


def authentication(logfile):
    def deco(func):
        if not os.path.exists(logfile):  # 该方法用来判断文件是否存在
            with open(logfile, 'w') as f:  # 运用上下文管理器打开文件，不存在文件，创建该文件
                pass

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)  # 调用原方法
            with open(logfile, 'a') as f:  # 运用上下文管理器追加写入文件日志
                f.write('{} {} is running!'.format(time.strftime('%Y-%m-%d %x'),
                                                   func.__name__))  # time.strftime()方法是用来加入日期的格式内容的方法

        return wrapper

    return deco


@authentication('log.txt')  # 在装饰器中加入参数，把文件名作为参数
def login():
    print("登陆成功！")


def main():
    login()


main()
