'''
需求：改进Person类，增加类属性Count，统计内存中的对象个数，
要求新增对象或者使用del删除对象时，类属性Count自动变化
（提示：析构函数和构造函数的使用）。
接着，请编写测试代码测试你的类定义符合题目要求。
'''


class Person3:
    count = 0

    def __init__(self, name='杜甫', age='20', sex='男'):
        self.name = name
        self.age = age
        self.sex = sex
        Person3.count += 1

    def prin_info(self):
        print('name:' + self.name)
        print('age:' + self.age)
        print('sex:' + self.sex)

    def __del__(self):
        print(self.name, "已删除")
        del self
        Person3.count -= 1

    def get_count():
        print('count:' + str(Person3.count))


def main():
    Person3.get_count()
    p1 = Person3('李白')
    p1.prin_info()
    Person3.get_count()

    p2 = Person3('李清照', '19', '女')
    p2.prin_info()
    Person3.get_count()

    p3 = Person3(age='21')
    p3.prin_info()
    Person3.get_count()

    # 析构
    del p3
    Person3.get_count()
    del p2
    Person3.get_count()
    del p1
    Person3.get_count()


main()
