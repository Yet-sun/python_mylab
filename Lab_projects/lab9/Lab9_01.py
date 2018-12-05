'''
需求：请任意选择一个你熟悉的Python GUI库，实现一个科学计算器。
'''

from tkinter import *
from tkinter.ttk import *


def frame(master):
    # 将共同的属性作为默认值, 以简化Frame创建过程
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


def button(master, text, command):
    # 提取共同的属性作为默认值, 使Button创建过程简化
    w = Button(master, text=text, command=command, width=6)
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w


def back(text):
    if len(text) > 0:
        return text[:-1]  # 利用切片将text最末的字符删除并返回
    else:
        return text


def calc(text):
    try:
        return eval(text)  # 用eval方法计算表达式字符串
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Error'


def calc_mi(text):
    return eval(text * text)


root = Tk()
root.title("Calculator")  # 添加标题

main_menu = Menu()  # 创建最上层主菜单

calc_menu = Menu(main_menu, tearoff=0)  # 创建Calculator菜单, 并加入到主菜单
calc_menu.add_command(label='Quit', command=lambda: exit())
main_menu.add_cascade(label='Calculator', menu=calc_menu)

text = StringVar()

root['menu'] = main_menu  # 将主菜单与root绑定

# 创建文本框
Entry(root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)

style = Style()
style.configure('TButton', padding=5)

# 创建第一行三个按钮
fedit = frame(root)
button(fedit, 'Backspace', lambda t=text: t.set(back(t.get())))
button(fedit, 'Clear', lambda t=text: t.set(''))
button(fedit, '±', lambda t=text: t.set('-(' + t.get() + ')'))
button(fedit, "%", lambda t=text: t.set(calc(t.get())))
button(fedit, "^", lambda t=text: t.set(calc_mi(t.get())))

# 在查阅资料时候发现使用自有的方法能够减少button的代码，每行四个, 创建其余四行按钮
for key in ('789/', '456*', '123-', '0.=+'):
    fsymb = frame(root)
    for char in key:
        if char == '=':
            button(fsymb, char, lambda t=text: t.set(calc(t.get())))
        else:
            button(fsymb, char, lambda t=text, c=char: t.set(t.get() + c))

root.mainloop()
