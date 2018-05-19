'''
需求：
    编写一个任意的程序，要求体现eval函数和exec函数的作用和不同
'''

x = 1


def f():
    y = 2
    a = eval('x+y')
    print('a:' + str(a))
    b = exec('x*y', {'x': 1, 'y': 2})
    print('b:' + str(b))
    exec("for i in range(10):print(i,end=',')")


f()
