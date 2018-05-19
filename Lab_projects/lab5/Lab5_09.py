'''
需求：
编写一个类Student，使其继承Person类，
增加一个属性学号（stuNo）, 重写print_info方法，
除了打印个人基本信息，还需要打印学号。
'''
from Lab_projects.lab5.Lab5_01 import Person  # 这里我把Lab5_01里的main()方法注释了


class Student(Person):
    def __init__(self, name, age, sex, stuno):
        Person.__init__(self, name, age, sex)  # 用父类的构造方法初始化基本属性
        self.stuno = stuno  # 子类增加的属性的初始化

    def print_info(self):
        print('name:' + self.name + '\t age:' + self.age +
              '\t sex:' + self.sex + '\t stuNo:' + self.stuno)


def main():
    p1 = Student('李白', '20', '男', '20161120232')
    p2 = Student('李清照', '19', '女', '20161120233')
    p3 = Student('杜甫', '20', '男', '20161120234')
    p1.print_info()
    p2.print_info()
    p3.print_info()


main()
