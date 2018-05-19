'''
需求：
改进Person类，增加类方法，可以根据有一定格式的字符串，
例如：“小明，20，男”，实例化并返回一个Person对象。
接着，请编写测试代码测试你的类定义符合题目要求。
'''


class Person8:
    def __init__(self, name: str, age: int, sex: str) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def returnPerson(cls, str):
        list = str.split(',')  # 将字符串分割，来作初始化的各个参数
        p = Person8(name=list[0], age=list[1], sex=list[2])  # 将字符串切割出来的子字符串传入__init__()方法，构建实例并对象进行初始化
        return p  # 返回对象


def main():
    str = "小明,20,男"
    print(Person8.returnPerson(str))
    print(Person8.returnPerson(str).name)
    print(Person8.returnPerson(str).age)
    print(Person8.returnPerson(str).sex)


main()
