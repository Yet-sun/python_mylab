'''
改进Person类，利用运算符重载，
实现Person对象的比较方法
（根据姓名顺序比较，同名情况下则使用年龄比较）。
需要考虑姓名为中文的情况，这时采用姓名拼音来比较。
'''

from pypinyin import lazy_pinyin


class Person:
    def __init__(self, name, age, sex):  # 初始化属性
        self.name = name
        self.age = age
        self.sex = sex

    def __gt__(self, other):  # 重载大于运算符
        self.name = ''.join(lazy_pinyin(self.name))
        other.name = ''.join(lazy_pinyin(other.name))  # 汉字转拼音
        if self.name > other.name:
            print(self.name, " > ", other.name)
            return True
        elif self.name == other.name:
            if self.age > other.age:
                print(self.name, " > ", other.name)
            return True
        else:
            print(self.name, " > ", other.name)
            return False

    def __eq__(self, other):  # 重载等于运算符
        self.name = ''.join(lazy_pinyin(self.name))
        other.name = ''.join(lazy_pinyin(other.name))
        if self.name == other.name:
            if self.age == other.age:
                print(self.name, " == ", other.name)
            return True
        else:
            print(self.name, " == ", other.name)
            return False

    def __lt__(self, other):  # 重载小于运算符
        self.name = ''.join(lazy_pinyin(self.name))
        other.name = ''.join(lazy_pinyin(other.name))
        if self.name < other.name:
            print(self.name, " < ", other.name)
            return True
        elif self.name == other.name:
            if self.age < other.age:
                print(self.name, " < ", other.name)
            return True
        else:
            print(self.name, " < ", other.name)
            return False


def main():
    p1 = Person('李白', '20', '男')
    p2 = Person('杜甫', '19', '女')
    p3 = Person('李白', '22', '男')

    # 测试
    # p1 = Person('libai', '20', '男')
    # p2 = Person('dufu', '19', '女')
    # p3 = Person('libai', '22', '男')

    print(p1 < p2)
    print(p1 > p2)
    print(p1 == p2)
    print(p1 < p3)


main()
