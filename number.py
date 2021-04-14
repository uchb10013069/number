#!/usr/bin/python
import tkinter as tk
import numbertest as num
#import numbertest
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image
#安安你好

t2=''
win = tk.Tk()
def event1(*args):
    global  entry1          #Entry 輸入框的變數
    global  comboxlist      #combox 下拉式 變數
    global  result1
    global  label6Str
    t1 = entry1.get()       # 取得用戶所輸入的數字
    if t1 == '':
        twd=9999999
    else:
        twd = float(t1)
    result1=num.numberjudgment(twd,float(t2[3]))
    label6Str.set(result1)


def event2(*args):
    rt1 = num.numberCalculation(label1Str, label2Str, label3Str, label6Str, label7Str)
    global t2
    t2= rt1.split(' ')
    label1Str.set(t2[0])
    label3Str.set(t2[1])
    label2Str.set(t2[2])
    label7Str.set(t2[4])
    entry1.delete(0, 'end')
    label6Str.set("")


    #label6Str.set(t2[3])

# def hello():
#     tkMessageBox.showinfo("Say Hello", "Hello World")  # 顯示訊息視窗
#
#
# btn3 = tk.Button(win, text='say hello',command = hello)
# btn3.place(x=0,y=100)

    #print(total)
    #label1Str.set('%.2f' % total)


#def go(*args):  # 处理事件，*args表示可变参数
    #print(comboxlist.get())  # 打印选中的值

#------------以下為視窗大小-------------------

win.minsize(width=788, height=453)                 #面板初始大小
# win.maxsize(width=1000, height=1000)               #面板最終大小
win.resizable(width=False, height=False)             #面板可否變化

#-----------元件背景------------------------

#img= ImageTk.PhotoImage(Image.open('cat2.jpg'))

# ---以下為背景圖----必須在最上層---------------

background_image = ImageTk.PhotoImage(Image.open('cat.jpg'))   #抓取圖片為背景
background_label = tk.Label(win, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

##---------------視窗上的元件----------------------##

#------------輸入框---------------------------
content = StringVar()

entry1=tk.Entry(win,width=10,font=('Courier', 32), textvariable=content)              #輸入框
#ntry1.place(x=310,y=200)                                       #輸入框位置
entry1.place(x=310,y=20)

#------------按鈕1---------------------------

btn1 =tk.Button(win,text="      確定      ",command=event1,font=('Courier', 32))     #第一個按鈕
#btn1.place(x=0,y=270)               #第一個按鈕位置
btn1.place(x=0,y=130)

#------------按鈕2---------------------------

btn2 =tk.Button(win,text=" 開始  ",command=event2,font=('Courier', 30))     #第一個按鈕
#btn1.place(x=0,y=270)               #第二個按鈕位置
btn2.place(x=600,y=20)


#------------純文字1---------------------------

label1Str=StringVar()                                       #高位元
#label1=tk.Label(win,text='...',textvariable=label1Str,font=('Courier', 50),bg='#CCB38C')
label1=tk.Label(win,text='0000',font=('Courier', 30),bg='#CCB38C',textvariable=label1Str)
#label1.place(x=10,y=200)    #高位元位置
label1.place(x=10,y=20)


#------------純文字2---------------------------

label2Str=StringVar()                                       #低位元
#label2=tk.Label(win,text='0000',font=('Courier', 30),bg='#CCB38C',textvariable=label1Str)
label2=tk.Label(win,text='+',font=('Courier', 30),bg='#CCB38C',textvariable=label2Str)
#label2.place(x=120,y=200)                                       #低位元位置
label2.place(x=120,y=20)

#------------純文字3---------------------------

label3Str=StringVar()
#label3=tk.Label(win,text='...',textvariable=label2Str,font=('Courier', 50),bg='#CCB38C')
label3=tk.Label(win,text='0000',font=('Courier', 30),bg='#CCB38C',textvariable=label3Str)
#label3.place(x=160,y=200)
label3.place(x=160,y=20)



#------------純文字4---------------------------

label4Str=StringVar()
label4=tk.Label(win,text='=',font=('Courier', 30),bg='#CCB38C')
#label4.place(x=270,y=200)
label4.place(x=270,y=20)
"""
rt1 = num.numberCalculation(label1Str,label2Str,label3Str)
t2 = rt1.split(' ')
label1Str.set(t2[0])
label3Str.set(t2[1])
label2Str.set(t2[2])
"""
#------------純文字5---------------------------
y=30
label5Str=StringVar()
label5=tk.Label(win,text='答案:',font=('Courier', 30),bg='#CCB38C')
label5.place(x=10,y=y+200)


#------------純文字6---------------------------

label6Str=StringVar()
label6=tk.Label(win,text='',font=('Courier', 30),bg='#CCB38C',textvariable=label6Str)
label6.place(x=160,y=y+200)

#------------純文字7---------------------------

label7Str=StringVar()
label7=tk.Label(win,text='000',font=('Courier', 20),bg='#CCB38C',textvariable=label7Str)
label7.place(x=10,y=80)

#------------下拉式選單1---------------------------
"""
comvalue = tk.StringVar()                                # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, textvariable=comvalue)    #初始化
comboxlist["values"] = ("個位元", "十位元", "百位元","千位元")
comboxlist.current()                                     #()初始選項
comboxlist.place(x=410,y=20,width=100,height=50)

#------------純文字8---------------------------

label8Str=StringVar()
label8=tk.Label(win,text='請選擇幾輪:',font=('Courier', 30),bg='#CCB38C')
label8.place(x=10,y=120)

#------------下拉式選單1---------------------------

comvalue = tk.StringVar()                                # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, textvariable=comvalue)    #初始化
comboxlist["values"] = ("1","2","3","4","5","6","7","8","9","10")
comboxlist.current()                                     #()初始選項
comboxlist.place(x=250,y=120,width=100,height=50)

"""


#-----------------------------------------
win.mainloop()






