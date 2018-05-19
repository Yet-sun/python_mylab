'''
需求：编写一个函数过滤输入列表中，不大于0的数值，要求使用Lamda表达式和filter()函数
'''


def lamdaFilterFunction(l: list) -> None:
    for i in filter(lambda x: x > 0, l):  # lamda表达式与filter函数的结合使用
        print(i, end=' ')


def main():
    l = input("请输入一个列表:").split(' ')  # 对输入的值用spilt()函数按空格进行分割，返回的是列表
    l = [int(l[i]) for i in range(len(l))]  # 这里将列表的值用for循环一个元素一个元素的由str类型转换为int型
    lamdaFilterFunction(l)


main()
