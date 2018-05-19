'''
需求：改进Person类，在满足之前要求不变的情况下，
将姓名(name)、年龄(age)、性别(sex)变为私有属性
（注意私有属性的定义要求），并使用@property装饰器。
要求使用两种方法
（提示：另一种方法可以直接使用property()函数）。
'''


class Person4:
    def __init__(self, name='任我行', age='60', sex='男'):
        self.__name = name
        self.__age = age
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def sex(self):
        return self.__sex

    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        self.__age = value

    @sex.setter
    def sex(self, value):
        self.__sex = value


def main():
    p1 = Person4()
    p1.name = '令狐冲'  #实际转化为p1.set_name('令狐冲')
    p1.age = 18  #实际转化为p1.set_age(18)
    print(p1.name, p1.age, p1.sex)

    p2 = Person4('东方不败')
    p2.age=22
    print(p2.name, p2.age, p2.sex)

    p3=Person4()
    print(p3.name, p3.age, p3.sex)

    p4=Person4('任盈盈')
    p4.age=18
    p4.sex='女'
    print(p4.name, p4.age, p4.sex)

main()
