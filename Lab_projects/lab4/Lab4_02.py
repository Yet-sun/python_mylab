'''
    需求：编写一个函数以读的方式打开一个文件，如果文件路径不对，重新输入，直到输入成功。
'''


def readFile(fiemName: str) -> str:
    try:
        f = open(fiemName, 'r', encoding='utf-8')
        f.readlines()
        print(f)
    except Exception as e:
        print("检测到错误，重新读取：", e)
    finally:
        f.close()


def main():
    while (True):
        try:
            fiemName = input("请输入文件路径：")
            readFile(fiemName)
        except Exception:
            print("错误，请重试！")
        else:
            return None
            break


main()
