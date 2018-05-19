'''
    需求：编写一个函数，提示输入两个数字a和b，并进行a与b的除法运算，把运算结果打印出来。
    要求对输入和程序进行检测，可以排除所有的错误。
    （要求，可以使用以下的异常检查下面的错误：IOError，ValueError、ZeroDivisionError，和其他所有错误）
'''


def mul(a:float,b:float)->float:
    try:
        result = a / b
        print(result)
    except ZeroDivisionError as zderr:
        print("检测到错误:", zderr)
    else:
        return result

def main():
    try:
        a= float(input("请输入两个数字："))
        b = float(input())
    except IOError as ioerr:
        print("检测到错误:",ioerr)
    except ValueError as verr:
        print("检测到错误:", verr)
    except Exception as err:
        print("检测到错误:", err)
    else:
        print(mul(a,b))

main()
