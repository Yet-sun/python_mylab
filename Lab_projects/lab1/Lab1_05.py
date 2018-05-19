print("请输入三角形的三条边：")
a = int(input())
b = int(input())
c = int(input())

if((a+b>c) and (a+c>b) and (b+c>a) and a>0 and b>0 and c>0):
    print("可以构成三角形，三角形的周长为：")
    print(a+b+c)
else:
    print("不能构成三角形")
