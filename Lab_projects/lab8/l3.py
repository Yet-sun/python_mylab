'''
需求：
编写一个程序，动态加载一个l1，l2所写的模块，并使用reload函数重新加载
'''


def test():
    imp_module1 = __import__("l2")  # import l2模块
    print("s =", imp_module1.circular())  # 使用l2模块的circular()函数

    imp_module2 = __import__("l1")  # import l1模块
    print("2 + 3 =", imp_module2.add(2, 3))  # 使用l1模块的add()函数


if __name__ == '__main__':
    test()
