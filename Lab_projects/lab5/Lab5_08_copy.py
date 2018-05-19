from multimethod import multimethod


class Person9():
    def __init__(self, name, age, sex):#初始化属性
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return '{0},{1},{2}'.format(self.name,self.sex,self.age)

    def __repr__(self):
        return self.__str__()

@multimethod(list, object)
def addPerson(l, p):
    l = l + [p]
    return l

@multimethod(list, str)
def addPerson(l, sex):
    p = Person9(sex)
    l = l + [p]
    return l

@multimethod(list, int)
def addPerson(l, age):
    p = Person9(age)
    l = l + [p]
    return l

def main():
    alist = []
    alist = addPerson(alist, Person9('李白', 20, '男'))
    alist = addPerson(alist,20161120232)
    alist = addPerson(alist, "软件工程")
    print(alist)

main()
