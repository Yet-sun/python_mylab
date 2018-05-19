'''
需求：
    编写两个样例函数（任意功能），一个无输入参数，
    一个需要三个以上输入参数（需要含有位置参数和命名参数）。
    利用函数装饰器，在不改变样例函数代码的情况下，
    分别为这两个函数加入打印执行时间的功能。
'''
import time


def print_excute_time(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()  # 使用导入的time模块获取运行函数前的时间
        func(*args, **kwargs)
        endtime = time.time()  # 使用导入的time模块获取运行函数后的时间
        print("running time:", endtime - starttime, "s")  # 打印运行时间

    return wrapper


@print_excute_time  # 在不改变原有的函数基础上加上计算运行时间的功能（装饰器）
def sample(x, y, z=2):
    print("I am just a sample function!")
    time.sleep(1)  # 使用导入的time模块，使进程挂起1秒
    print("{0}*{1}*{2}=".format(x, y, z), x * y * z)


@print_excute_time
def sample2():
    print("I am just a sample function too!")
    time.sleep(1)
    print(0)


def main():
    x = int(input("input x,y,z:"))
    y = int(input())
    z = int(input())
    sample(x, y, z)
    sample2()


main()
