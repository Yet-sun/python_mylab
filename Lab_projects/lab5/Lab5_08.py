'''
需求：
改进Person类，利用multimethod模块，实现一个可重载的方法，
方法的具体功能和效果可以自定（根据自定义函数的难度打分）。
'''
from multimethod import multimethod


class Person9():
    def __init__(self, name):  # 初始化属性
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


@multimethod(list, object)
def addPerson(l, p):
    l = l + [p]
    return l


@multimethod(list, str)
def addPerson(l, sex):
    p = Person9(sex)
    l = l + [p]
    return l


def main():
    alist = []
    alist = addPerson(alist, Person9('李白'))
    alist = addPerson(alist, '20')
    alist = addPerson(alist, "男")
    print(alist)


main()
