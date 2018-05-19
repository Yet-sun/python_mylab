'''
需求：
假设我们有一个类动物基类Animal，
本身带有一个叫声的方法。
我们在其派生类狗和猫中分别重写这个方法分别输出二者的叫声。
这时，如果我们有一个狗猫类同时继承了狗和猫类。
那么他同时也继承了二者的叫声方法，那么我们在实例化该类时，
我们的叫声方法究竟是猫的呢还是狗的呢？
请编程给出上述问题的答案，并分析为什么。
'''


class Animal:
    def call(self):
        print("Animal is calling!")

class Dog(Animal):
    def call(self):
        print("Dog is calling!")

class Cat(Animal):
    def call(self):
        print("Cat is calling!")

class CatDog(Dog,Cat):
    pass

def main():
    a = Animal()
    a.call()
    c=Cat()
    c.call()
    d=Dog()
    d.call()
    cd=CatDog()
    cd.call()

main()