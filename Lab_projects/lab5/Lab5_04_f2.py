'''
需求：
    改进Person类，提供属性读取拦截器，
    当性别不属于’男’或’女’，年龄不在0-120范围内时，
    产生一个自定义异常，并抛出异常。（提示：__setattr__）。
    接着，请编写测试代码测试你的类定义符合题目要求。
'''


class Person5:
    def __init__(self, name='任我行', age='60', sex='男'):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def getsex(self):
        return self.__sex

    def setname(self, name_value):
        self.__name = name_value

    def setage(self, value):
        self.__age = value

    def setsex(self, value):
        self.__sex = value

    def delname(self):
        del self.__name

    def delage(self):
        del self.__age

    def delsex(self):
        del self.__sex

    name = property(getname, setname, delname)
    age = property(getage, setage, delage)
    sex = property(getsex, setsex, delsex)


def main():
    p1 = Person5()
    p1.name = '令狐冲'  # 实际转化为p1.setname('令狐冲')
    p1.age = 18  # 实际转化为p1.setage(18)
    print(p1.name, p1.age, p1.sex)

    p2 = Person5('东方不败')
    p2.age = 22
    print(p2.name, p2.age, p2.sex)

    p3 = Person5()
    print(p3.name, p3.age, p3.sex)

    p4 = Person5('任盈盈')
    p4.age = 18
    p4.sex = '女'
    print(p4.name, p4.age, p4.sex)


main()
