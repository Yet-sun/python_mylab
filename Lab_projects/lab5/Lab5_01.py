'''
需求：编写一个类Person，要求具有三个实例属性：
姓名(name)、年龄(age)、性别(sex)，
还具有一个打印信息的函数print_info，
按一定格式打印三个实例属性。
接着，请编写测试代码测试你的类。
'''


class Person:
    def __init__(self, name, age, sex):#初始化属性
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print('name:' + self.name)
        print('age:' + self.age)
        print('sex:' + self.sex)


def main():
    p1 = Person('李白', '20', '男')
    p2 = Person('李清照', '19', '女')
    p3 = Person('杜甫', '20', '男')
    p1.print_info()
    p2.print_info()
    p3.print_info()


main()
