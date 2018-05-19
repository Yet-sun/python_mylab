print("请输入一个字符：")
char = input()

a = ord(char)				# 利用ord()函数来获得字符的ASCII

if(a<58 and a>47):			#判断数字的ASCII码
    print("数字")
elif(a>64 and a<107): 		#判断大写字母的ASCII码
    print("大写字母")
elif(a>96 and a<123): 		#判断小写字母的ASCII码
    print("小写字母")
else:
    print("其他字符")
