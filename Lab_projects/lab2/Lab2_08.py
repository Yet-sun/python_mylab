'''
    需求：
      编写程序。定义元音元组vowels = ( 'a', 'e', 'i', 'o', 'u' )，
      输入一段英文，利用元音元组和其他内置数据结构，统计这段输入文字中，元音出现的个数。
'''

def count(str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for i in vowels:
       count+=str.count(i)

    print("count(vowels) : ",count)

def main():
    str = input()
    count(str)

main()