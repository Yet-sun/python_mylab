'''
需求:编写一个函数，计算算三角形面积，TriangleArea(a,b,c)，其中a,b,c为分别为三角形三条边，要求a,b,c为强制命名参数。
'''

def TriangleArea(*,x:int,y:int,z:int)->float:#利用海伦公式计算三角形面积
    #在定义函数的时候第一个参数为*，这里不是带*的可变参数，就是简单的使用强制命名参数
    c=0.5*(x+y+z)
    area = (c*(c-x)*(c-y)*(c-z))**0.5
    return area

def main():
    a=int(input("请输入三角形的三条边a,b,c："))
    b=int(input())
    c=int(input())
    print(TriangleArea(x=a,y=b,z=c))

main()