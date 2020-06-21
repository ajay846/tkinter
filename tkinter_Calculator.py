import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=45)
e.grid(row=0,column=0,columnspan=3)

def add(number):
    #e.delete(0, END)
    current_num = e.get()
    e.delete(0, END)
    e.insert(0,str(current_num) + str(number))
def btn_clear():
    e.delete(0,END)

def btn_add():
    f_num = e.get()
    global f_number
    f_number = int(f_num)
    e.delete(0,END)
    global math
    math = "add"
def btn_sub():
    f_num = e.get()
    global f_number
    f_number = int(f_num)
    e.delete(0,END)
    global math
    math = "sub"
def btn_div():
    f_num = e.get()
    global f_number
    f_number = int(f_num)
    e.delete(0,END)
    global math
    math = "div"
def btn_mul():
    f_num = e.get()
    global f_number
    f_number = int(f_num)
    e.delete(0,END)
    global math
    math = "mul"

def equal_btn():
    second_number = e.get()
    e.delete(0,END)
    if math == 'add':
        e.insert(0,int(f_number)+int(second_number))
    if math == 'sub':
        e.insert(0,int(f_number)-int(second_number))
    if math == 'div':
        e.insert(0,int(f_number)/int(second_number))
    if math == 'mul':
        e.insert(0,int(f_number)*int(second_number))



b1 = Button(root, text=1, padx=35,pady=20, command=lambda: add(1), font=('times', 12, 'bold'))
b2 = Button(root, text=2, padx=35,pady=20, command=lambda: add(2), font=('times', 12, 'bold'))
b3 = Button(root, text=3, padx=35,pady=20, command=lambda: add(3), font=('times', 12, 'bold'))
b4 = Button(root, text=4, padx=35,pady=20, command=lambda: add(4), font=('times', 12, 'bold'))
b5 = Button(root, text=5, padx=35,pady=20, command=lambda: add(5), font=('times', 12, 'bold'))
b6 = Button(root, text=6, padx=35,pady=20, command=lambda: add(6), font=('times', 12, 'bold'))
b7 = Button(root, text=7, padx=35,pady=20, command=lambda: add(7), font=('times', 12, 'bold'))
b8 = Button(root, text=8, padx=35,pady=20, command=lambda: add(8), font=('times', 12, 'bold'))
b9 = Button(root, text=9, padx=35,pady=20, command=lambda: add(9), font=('times', 12, 'bold'))
b0 = Button(root, text=0, padx=35,pady=19, command=lambda: add(0), font=('times', 12, 'bold'))
button_add = Button(root, text="+",padx=34,pady=20, command= btn_add, font=('times', 11, 'bold'))
button_sub = Button(root, text="-",padx=36,pady=20, command= btn_sub, font=('times', 11, 'bold'))
button_div = Button(root, text="/",padx=35,pady=20, command= btn_div, font=('times', 11, 'bold'))
button_mul = Button(root, text="*",padx=35,pady=20, command= btn_mul, font=('times', 11, 'bold'))
button_equal = Button(root, text="=",padx=125,pady=20, command=equal_btn, font=('times', 12, 'bold'))
button_clear = Button(root, text="C",padx=35,pady=20, command= btn_clear, font=('times', 11, 'bold'))

b1.grid(row="3",column="0")
b2.grid(row="3",column="1")
b3.grid(row="3",column="2")

b4.grid(row="2",column="0")
b5.grid(row="2",column="1")
b6.grid(row="2",column="2")

b7.grid(row="1",column="0")
b8.grid(row="1",column="1")
b9.grid(row="1",column="2")

b0.grid(row="4",column="1")
button_add.grid(row=4, column=0)
button_sub.grid(row=4, column=2)
button_div.grid(row=5, column=0)
button_mul.grid(row=5, column=2)
button_clear.grid(row=5,column=1)
button_equal.grid(row=6,column=0, columnspan=3)

root.mainloop()
