import json

# 读文件
input_csv_file = ("学生信息表.csv")
lines = open(input_csv_file, 'r').readlines()  # 使用readlines()是因为其自动将文件内容分析成一个行的列表，方便操作
lines = [line.strip() for line in lines]  # 将每一行数据加入lines列表里面，忽略空格等

keys = lines[0].split(',')  # 将列表元素切割获取到key（lines[0]拿到的是第一行数据，即key）

line_num = 1
all_lines_len = len(lines)

json_datas = []
while line_num < all_lines_len:
    values = lines[line_num].split(',')
    json_datas.append(dict(zip(keys, values)))
    line_num += 1

json_str = json.dumps(json_datas, ensure_ascii=False, indent=4)
# dump()是将对象序列化，indent选项可格式化json文件，且json.dumps序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
output_json_file = input_csv_file.replace('csv', 'json')  # 修改文件后缀名

# 写文件
f = open(output_json_file, 'w', encoding='utf-8')  # 注意，这里不写encoding的话读出来是乱码
f.write(json_str)
f.close()

print("成功转换")
