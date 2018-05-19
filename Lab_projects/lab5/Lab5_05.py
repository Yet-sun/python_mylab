'''
需求：
    改进Person类，提供属性读取拦截器，
    当性别不属于’男’或’女’，年龄不在0-120范围内时，
    产生一个自定义异常，并抛出异常。（提示：__setattr__）。
    接着，请编写测试代码测试你的类定义符合题目要求。
'''


class Person6:
    def __setattr__(self, name, value):
        if name == name:
            object.__setattr__(self, name, value)
        if name == 'sex':
            if (value == '男') | (value == '女'):
                object.__setattr__(self, name, value)
            else:
                try:
                    raise SexError("性别只能是男或者女")
                except SexError as se:
                    print("错误——>", se)
        elif name == 'age':
            if (value < 0) | (value > 120):
                try:
                    raise AgeError("年龄必须在0-120范围内")
                except AgeError as ae:
                    print("错误——>", ae)
            else:
                object.__setattr__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            print(name)


class SexError(Exception):
    pass


class AgeError(Exception):
    pass


def main():
    p3 = Person6()
    p3.name = "李白"
    p3.age = 255
    p3.sex = '我'
    print("姓名：", p3.name)
    print("年龄：", p3.age)
    print("性别：", p3.sex)


main()
