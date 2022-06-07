import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import time
import random
import datetime

win = tk.Tk()
win.title('随机点名系统')
win.geometry('600x400+500+250')
data = []


def take():
    for s in range(50):
        desc = ''
        if s == 47:
            time.sleep(0.5)
        elif s == 48:
            time.sleep(0.6)
        elif s == 48:
            time.sleep(0.7)
        elif s == 49:
            time.sleep(0.9)
        else:
            time.sleep(0.1)
        classes = random.sample(data, 1)
        if s == 49:
            desc += f'{classes[0]}别看了就是你'
        else:
            desc += f'{classes[0]}'

        text.set(desc)  # 设置内容
        win.update()  # 屏幕更新


def selectExcelfile():
    global data
    sfname = askopenfilename(title='选择Excel文件', filetypes=[('Excel', '*.xlsx'), ('All Files', '*')])
    text1.insert(tk.INSERT, sfname)
    df = pd.DataFrame(pd.read_excel(sfname))
    data = [i for i in df['Unnamed: 1'][2:]]
    now = time.strftime('%Y-%m-%d', time.localtime(time.time())) + "  星期" + str(day)
    win.update()
    now += "\n班级总人数:%s人" % str(len(data))
    l1.config(text='')
    l1.config(text=now)


d = datetime.datetime.now()
day = d.weekday() + 1
now = time.strftime('%Y-%m-%d', time.localtime(time.time())) + "  星期" + str(day)

l1 = tk.Label(win, fg='red', text=now, width=20, height=5, font=('微软雅黑', '14'))
l1.place(x=180, y=5)

text = tk.StringVar()

l2 = tk.Label(win, fg='red', textvariable=text, width=15, height=3, font=('微软雅黑', '20'))
l2.place(x=180, y=100)

text1 = tk.Entry(win, bg='white', width=35)
button1 = tk.Button(win, text='请选择文件', width=8, command=selectExcelfile).place(x=100, y=310)
text1.place(x=180, y=315)

bt = tk.Button(win, text="筛选", width=15, height=2, command=take)
bt.place(x=250, y=260)

win.mainloop()
