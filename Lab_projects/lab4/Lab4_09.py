'''
需求：
    编写一个任意的程序，要求体现全局语句global和非局部语句nonlocal的作用
'''
a = 0


def f_outer():
    global a
    a = 10
    b = 1
    print(a)

    def f_inner():
        nonlocal b
        b = 11

    f_inner()
    print(b)


f_outer()
