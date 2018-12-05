'''
需求：
编写一个可以求圆形、三角形、矩形、梯形面积的模块，并编写只有独立运行模块代码时才能运行的测试代码。要求必须包含完整的API和模块文档（可以通过help函数查看）。并要求通过__doc__属性分别查看模块注释、类注释和函数注释。
'''

PI = 3.14  # 定义常量π


def circular():
    '''函数circular用于求输入圆的半径，返回该圆的面积'''
    r = int(input("请输入圆的半径："))
    return PI * r ** 2


def triangle():
    '''函数triangle用于输入三角形的三条边，运用海伦公式返回三角形的面积'''
    a = int(input("请输入三角形的三条边："))
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def rectangle():
    '''函数rectangle用于输入矩形的长和宽，返回该矩形的面积'''
    a = int(input("请输入矩形的长和宽："))
    b = int(input())
    return a * b


def trapezoid():
    '''函数trapezoid用于输入梯形的长宽高，返回该梯形的面积'''
    a = int(input("请输入梯形的上底和下底："))
    b = int(input())
    h = int(input("请输入梯形的高:"))
    return (a+b)*h/2

class Polygon:
    '''类多边形Polygon的说明'''
    def polygon(self):
        '''类多边形Polygon的方法polygon的说明'''
        print("polygon")

def main():
    print(trapezoid())

if __name__ == '__main__':
    main()
