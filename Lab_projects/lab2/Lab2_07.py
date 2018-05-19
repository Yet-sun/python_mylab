'''
    需求：
        编写程序，输入一段文字，利用集合数据结构，统计该文字中出现的字有哪些？
        （提示：重复文字只出现一次）
'''
import collections

def countwords(str):
    c = collections.Counter(str)
    print(c)

def main():
    str_input = str(input("请输入文字："))
    countwords(str_input)

main()

