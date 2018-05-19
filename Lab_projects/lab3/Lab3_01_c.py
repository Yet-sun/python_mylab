import csv

with open('学生信息表.csv','r',newline='') as csvfile:   #使用with:当文件不用时会自动关闭文件
    # 设置newline=''，否则两行之间会空一行，也可不设
    csvReader = csv.reader(csvfile)     #读文件

    for content in csvReader:   #取出来的content其实是列表
        #print(content)
        for i in content:   #遍历两个列表
            print(i,end=' ')
        print()     #将遍历出来的两个列表的元素换行隔开

'''方法二：不使用with，打出列表
import csv

csvfile = open('学生信息表.csv',newline='')
csvReader = csv.reader(csvfile)

for content in csvReader:
    print(content)

csvfile.close()
'''