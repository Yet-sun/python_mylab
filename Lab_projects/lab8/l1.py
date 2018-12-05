'''
需求：
编写一个运算模块，可以实现+、-、*、/和**（幂）运算，并编写测试代码测试。要求必须包含完整的API和模块文档（可以通过help函数查看）
'''
PI = 3.14   #定义常量π

def add(x,y):
    '''
    add(x,y)
    :param x:
    :param y:
    :return: double
    '''
    return x+y  #加法运算

def sub(x,y):
    '''
    sub(x,y)
    :param x:
    :param y:
    :return: double
    '''
    return x-y  #减法运算

def mul(x,y):
    '''
    mul(x,y)
    :param x:
    :param y:
    :return: double
    '''
    return x*y  #乘法运算

def div(x,y):
    '''
    div(x,y)
    :param x:
    :param y:
    :return: double
    '''
    return x/y  #除法运算

def mi(x,y):
    '''
    mi(x,y)
    :param x:
    :param y:
    :return: double
    '''
    return x**y #幂运算

#测试代码：
def main():
    x=int(input("请输入两个数:"))
    y=int(input())
    print("x+y=",add(x,y))
    print("x-y=",sub(x,y))
    print("x*y=",mul(x,y))
    print("x/y=",div(x,y))
    print("x**y=",mi(x,y))

if __name__=='__main__':
    main()
