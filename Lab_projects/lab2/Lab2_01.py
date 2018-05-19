'''
    需求：
    编写程序用Print语句输出2000年至2500年间的所有闰年，要求每行输出8个。
'''

year = 2000
count = 0

while year<2500:
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,end=" ") #这里设置了end=' '表示将print函数输出的内容改成每输出一个打印一个空格而不是默认的换行
        year=year+1
        count+=1
        if count%8==0:  #每一行输出8个
            print()
    else:
        year+=1