import tkinter as tk
import tkinter.messagebox as mb
from random import randint

win = tk.Tk()
# 窗口名称
win.title('表白小程序')
# 窗口大小及位置   注意 x 是英文字母 x 前两个是窗口大小 后两个是窗口位置
win.geometry('800x500+350+150')

# 创建一个画布，将图片放在画布上
canvas = tk.Canvas(win, width=600, height=300)
image_file = tk.PhotoImage(file='love1.png')
image = canvas.create_image(450, 0, anchor='n', image=image_file)
canvas.pack(side='top')


# 同意按钮功能
def love():
    # 关闭子页面和主页面
    def go():
        lo.destroy()
        win.destroy()

    def clo():
        mb.showinfo('卑微', '你都同意了，约会去嘛❤')

    # 生成子页面
    lo = tk.Toplevel(win)
    lo.title('约会')
    lo.geometry('300x300+500+300')

    img = tk.PhotoImage(file='love2.png')
    the = tk.Label(lo, image=img)
    the.pack()
    tk.Button(lo, text='我们去约会吧', command=go).place(x=110, y=220)

    lo.protocol('WM_DELETE_WINDOW', clo)
    lo.mainloop()


# 不同意按钮功能
def again():
    x = randint(10, 600)
    y = randint(10, 400)
    # 重新设置bt2的文字
    bt2.configure(text=word[randint(0, len(word) - 1)])
    # 重新设置bt2的位置
    bt2.place(x=x, y=y)


# 点击关闭按钮触发的事件
def close():
    mb.showinfo('警告', '小姐姐别想逃')


# 帮助按钮
def do_job():
    do = tk.Toplevel(win)
    do.geometry('300x300+500+300')
    do.title('说明')
    tk.Label(do, text='不同意永远关不掉', font=('微软雅黑', '20')).pack()
    do.mainloop()


# 考虑按钮功能
def kao():
    mb.showinfo('别纠结了', '你完了，你妈让你嫁给我')
    mb.showinfo('别纠结了', '你爸也是这么说的')
    mb.showinfo('别纠结了', '你奶奶也让你嫁给我')
    mb.showinfo('别纠结了', '你哥哥也同意了，你全家都同意')
    mb.showinfo('别纠结了', '你闺蜜说嫁给我没错')
    mb.showinfo('别纠结了', '你爸说不同意就打你')
    mb.showinfo('别纠结了', '接受现实吧，我会对你好的')
    mb.showinfo('别纠结了', '你都是我的人了')


# 鼠标监听事件触发的功能
def a(eve):
    if a:
        x = randint(10, 600)
        y = randint(10, 400)
        bt2.configure(text=word[randint(0, len(word) - 1)])
        bt2.place(x=x, y=y)


tk.Label(win, text='小姐姐，\n观察你很久了！\n做我女朋友好不好?', font=('微软雅黑', '20')).place(x=100, y=100)
word = [
    '我会对你好的', '你爸妈都同意了', '我有车有房', '家务我来做', '孩子我带', '在考虑一下吧', '孩子想生就生', '我妈会游泳', '你最好看',
    '给你买包', '钱都给你', '都给你买', '我秒回消息', '不存私房钱'
]
# 按钮
tk.Button(win, text='同意', command=love, width=13, height=2).place(x=200, y=350)
tk.Button(win, text='考虑考虑', command=kao, width=13, height=2).place(x=400, y=350)
bt2 = tk.Button(win, text='拒绝', command=again, width=13, height=2)
bt2.place(x=600, y=350)

# 给bt2添加鼠标监听事件
bt2.bind('<Motion>', a)

# 菜单栏
menubar = tk.Menu(win)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='帮助', menu=filemenu)
filemenu.add_command(label='说明', command=do_job)
win.config(menu=menubar)

# 锁定关闭按钮并触发close功能
win.protocol('WM_DELETE_WINDOW', close)
# 锁定长宽
win.resizable(False, False)

win.mainloop()