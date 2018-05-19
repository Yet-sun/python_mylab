'''
    需求：改进Person类，增加构造函数，
    要求对于姓名(name)、年龄(age)、性别(sex)三个实例属性，
    可以传递任意一个或任意两个参数实例化对象（提示：默认值）。
    接着，请编写测试代码测试你的类定义符合题目要求。

'''


class Person2:
    def __init__(self, name='杜甫', age='20', sex='男'):
        self.name = name
        self.age = age
        self.sex = sex

    def prin_info(self):
        print('name:' + self.name)
        print('age:' + self.age)
        print('sex:' + self.sex)


def main():
    p1 = Person2('李白')
    p2 = Person2('李清照', '19', '女')
    p3 = Person2(age='21')
    p1.prin_info()
    p2.prin_info()
    p3.prin_info()


main()
