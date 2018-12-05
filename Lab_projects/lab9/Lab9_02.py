'''
需求：请任意选择一个你熟悉的Python GUI库，实现一个简单文本编辑器。
'''
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

filename = ''


def openfile():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileName:' + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def new():
    global filename
    root.title('未命名文件')
    filename = None
    textPad.delete(1.0, END)


def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()


def saveas():
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title('FileName:' + os.path.basename(f))


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


def author():
    showinfo('author:', 'sunyue')


root = Tk()
root.title('简易文本编辑器')
root.geometry("800x500+100+100")  # 界面大小

menubar = Menu(root)  # 菜单栏
root.config(menu=menubar)

filemenu = Menu(menubar)  # 文件菜单栏
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=new)  # accelerator设置快捷键
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar)  # 编辑菜单栏
editmenu.add_command(label="剪切", accelerator="Ctrl + X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl + C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl + V", command=paste)
editmenu.add_command(label="全选", accelerator="Ctrl + A", command=selectAll)
editmenu.add_separator()  # 分隔线
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + y', command=redo)
menubar.add_cascade(label="编辑", menu=editmenu)

aboutmenu = Menu(menubar)  # about菜单栏
aboutmenu.add_command(label="作者", command=author)
menubar.add_cascade(label="about", menu=aboutmenu)

toolbar = Frame(root, height=25, bg='WhiteSmoke')  # toolbar

shortButton = Button(toolbar, text='打开', command=openfile)
shortButton.pack(side=RIGHT, padx=5, pady=5)
shortButton = Button(toolbar, text='保存', command=save)
shortButton.pack(side=RIGHT)

toolbar.pack(expand=NO, fill=X)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
