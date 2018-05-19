'''
    需求：编写一函数Prime(n)，对于已知正整数n，判断该数是否为素数，如果是素数，返回True，否则返回False。
'''


def Prime(n: int) -> int:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def main():
    n = int(input("请输入一个正整数："))
    print(Prime(n))


main()
