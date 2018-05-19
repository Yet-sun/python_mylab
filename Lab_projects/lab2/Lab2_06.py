'''
    需求：
        编写程序，莫尔斯电码采用了短脉冲和长脉冲（分别为点和点划线）来编码字母和数字。
        例如，字母“A”是点划线，“B”是点划线点点。见附件“完整的摩尔斯电码表.txt”
            1）创建字典，将字符映射到莫尔斯电码。
            2）输入一段英文，翻译成莫尔斯电文。
'''

def mostran(str):
    f=open("D:\\实验2完整的摩尔斯电码表.txt","r")

    mostext=""

    for line in f:
        mostext+=line   #把每一行读取出来添加到一个字符串中

    f.close()
    l=mostext.split()  #把字符串按空格来切割

    l1=l[::2]    #这种间隔切片出来也还是列表，l1是字符，l2是莫斯密码
    l2=l[1::2]
    MosDict=dict(zip(l1,l2))    #转换成字典

    for char in str:
        print(MosDict[char.upper()],end=" ")

def main():
    massage=input("Enter a massage:")

    str=""
    for char in massage:
        str+=char
    mostran(str)

main()
