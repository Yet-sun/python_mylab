'''
    需求：编写一个递归函数，实现Fabonacci数列
'''


def Fabonacci(n: int) -> int:
    if n == 1 or n == 2:#Fabonacci函数中，n=1和n=2是特殊值
        return 1
    else:
        return Fabonacci(n - 2) + Fabonacci(n - 1)


def main():
    n = int(input("请输入一个整数："))
    print("Fabonacci函数的结果为:" + str(Fabonacci(n)))


main()
