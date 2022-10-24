import time
import datetime
import random
import pandas as pd
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox as mg
from tkinter.filedialog import askopenfilename

win = tk.Tk()
win.title("答题")
WIDTH = '1280'
HEIGHT = '640'
win.geometry(f'{WIDTH}x{HEIGHT}+120+100')

img2_obj = Image.open("img/2.png")
img_obj = Image.open("img/bg.jpg")
img = ImageTk.PhotoImage(img_obj)
img2 = ImageTk.PhotoImage(img2_obj)

temp = []
subject = {}
cur = None

canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack()


def selectExcelfile():
    global subject, temp
    sfname = askopenfilename(title='选择Excel文件', filetypes=[
        ('Excel', '*.xlsx'), ('All Files', '*')])
    df = pd.DataFrame(pd.read_excel(sfname))
    try:
        temp = subject_one = [i for i in df['题目']]
        subject_two = [i for i in df['答案']]
        subject = dict(zip(subject_one, subject_two))
        mg.showwarning("成功", "导入成功！")
    except KeyError:
        mg.showerror("error", "导入是失败，格式错误，请查看帮助")


def random_num():
    global tit, cur
    try:
        canvas.delete(tit)
        canvas.delete(tit2)
        ran = random.randint(0, len(temp) - 1)
        cur = temp[ran]
        try:
            t = cur.split('\n', 1)
        except:
            t = cur
        l = len(t[0])
        if l > 30:
            cur_1 = cur[:30]
            if l - 30 > 30:
                cur_2 = cur[30:60]
                t = cur_1 + '\n' + cur_2 + '\n' + cur[60:]
            else:
                t = cur_1 + '\n' + cur[30:]
        elif len(t) == 2:
            t = t[0] + '\n' + t[1]
        if isinstance(t, list):
            t = t[0]
        tit = canvas.create_text(
            650, 200, text=t, fill="#000000", font=('微软雅黑', '30'), justify='center')
    except:
        mg.showinfo("错误", "请先导入题库")


def show():
    global tit2
    canvas.delete(tit2)
    var = subject[cur]
    tit2 = canvas.create_text(
        680, 480, text=var, fill="#ff242b", font=('微软雅黑', '40'))


def remove():
    canvas.delete(tit)
    canvas.delete(tit2)


def help():
    son = tk.Toplevel(win)
    son.title('帮助')
    son.geometry('500x300+700+300')
    frame = tk.Frame(son)
    frame.pack()
    tk.Label(frame, text='题库格式，\n 题目和答案是固定写法，在下面写具体的题目及答案').pack()
    tk.Label(frame, image=img2).pack()


# 时间
d = datetime.datetime.now()
day = d.weekday() + 1
now = time.strftime('%Y-%m-%d', time.localtime(time.time())
                    ) + "  星期" + str(day)
# 显示时间
c1 = canvas.create_text(450, 15, text=now, font=('微软雅黑', '20'))

# 显示题目
text = tk.StringVar()

tit = canvas.create_text(220, 225, text='')
tit2 = canvas.create_text(220, 225, text='')

ttk.Button(win, text="随机选题", command=random_num).place(x=750, y=0)

ttk.Button(win, text="显示答案", command=show).place(x=830, y=0)

ttk.Button(win, text="清空", command=remove).place(x=910, y=0)

menu = tk.Menu(win)

# window 系统
# menu.add_command(label="选择题库", command=selectExcelfile)
# menu.add_command(label="帮助", command=help)

# mac 系统
menuType = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="工具栏", menu=menuType)
menuType.add_command(label="选择题库", command=selectExcelfile)
menuType.add_command(label="帮助", command=help)

win.config(menu=menu)

win.resizable(False, False)
win.mainloop()
