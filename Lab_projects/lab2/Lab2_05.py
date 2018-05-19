'''
    需求:
        编写程序，使用字典来创建程序，提示用户输入电话号码，并用英文单词形式显示数字。
        例如：输入138显示为“one three eight”。
'''

def getdict(phone):
    A=[i for i in range(0,10)]  #用range函数产生一个0-9的随机数
    B=["zero","one","two","three","four","five","six","seven","eight","nine"]
    mydict=dict(zip(A,B))   #将两个列表转换成字典
                            #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

    for i in phone:
        print(mydict[int(i)],end=' ')  #这里设置了end=' '表示将print函数输出的内容改成每输出一个打印一个空格而不是默认的换行

def main():
    phone=input("Please enter a series phone number:")
    getdict(phone)

main()