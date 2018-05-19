import csv

info = ['17010002','赵四','女','自动化1701']

csvfile = open('学生信息表.csv','a+',newline='')    #'a+'是追加写入模式

writer = csv.writer(csvfile)   #写入数据
writer.writerow(info)   #因为只有一行数据，所以用writerow()方法

print("写入完毕！")
csvfile.close()

