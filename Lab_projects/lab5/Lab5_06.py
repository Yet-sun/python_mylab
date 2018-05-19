'''
需求：改进Person类，增加静态方法，可以实时打印当前内存中Person对象的个数。
接着，请编写测试代码测试你的类定义符合题目要求。（要求使用该静态方法）
'''


class Person7:
    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        Person7.count += 1

    def __del__(self):
        print(self.name, "已删除")
        Person7.count -= 1
        del self

    def prin_info(self):
        print('name:' + self.name+'\t age:' + self.age+'\t sex:' + self.sex)

    @staticmethod
    def countPerson():
        print("count:", Person7.count)


def main():
    p1 = Person7('李白', '20', '男')
    p2 = Person7('李清照', '19', '女')
    p3 = Person7('杜甫', '20', '男')
    Person7.countPerson()
    p1.prin_info()
    p2.prin_info()
    p3.prin_info()
    del p1
    Person7.countPerson()


main()
