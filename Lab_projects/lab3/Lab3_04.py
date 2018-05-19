import random,sys

n = int(sys.argv[1])#表示在cmd窗口输入的命令行参数

for i in range(n):
    print(random.randint(0,99))
