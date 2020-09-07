#Here I've added just 3 products but more can be added according to your needs

from tkinter import *
import webbrowser

main_window = Tk()
main_window.title("Groceries Bill")
main_window.resizable(False, False)

frame_store_name = Frame(main_window)
frame_products = Frame(main_window)
frame_calc = Frame(main_window, highlightbackground="white", highlightcolor="black", highlightthickness=4)

frame_store_name.grid(row=0)
frame_products.grid(column=0)
#frame_products_bill.grid(row=2, column=3)
frame_calc.grid(row=1, column=1)

label_storeName = Label(frame_store_name, text="STORE NAME HERE", font=("", 20, "bold"))
label_storeName.grid()

def gen_bill():
    products_dict = {
        "apples": 10, "pineapples": 40, "capples": 20
    }

    apples = int(apple_quantity.get())
    pineapples = int(pineapple_quantity.get())
    capples = int(capple_quantity.get())

    total_bill = (products_dict["apples"]*apples) + (products_dict["pineapples"]*pineapples) + (products_dict["capples"]*capples)

    label_info = Label(frame_products, text="\n\nBill", font=("", 12, "bold"))
    label_info.grid(row=5, column=1)
    
    label_bill = Label(frame_products, text="Apples: "+ str(apples) +"\nPineapples: "+ str(pineapples) +"\nCusturd Apples: "+ str(capples) + "\nGrand Total>> "+ str(total_bill))
    label_bill.grid(row=6, column=1)

    webbrowser.open('https://www.instagram.com/iamchintu.u', new=2)


label_apple = Label(frame_products, text="Apple")
apple_quantity = Entry(frame_products)
apple_quantity.insert(0, 0)

label_pineapple = Label(frame_products, text="Pineapple")
pineapple_quantity = Entry(frame_products)
pineapple_quantity.insert(0, 0)

label_capple = Label(frame_products, text="Custurd Apple")
capple_quantity = Entry(frame_products)
capple_quantity.insert(0, 0)

label_apple.grid(row=0, column=0)
label_pineapple.grid(row=1, column=0)
label_capple.grid(row=2, column=0)
#------------------------------------------------------------------------------
apple_quantity.grid(row=0, column=1)
pineapple_quantity.grid(row=1, column=1)
capple_quantity.grid(row=2, column=1)

submit_btn = Button(frame_products, text="Generate Bill", command= lambda: gen_bill())
submit_btn.grid(row=3, column=1)

label_caution = Label(frame_products, text="**Do not leave the entry field blank**")
label_caution.grid(row=4, column=1)

#Calculator

e = Entry(frame_calc, width=45, relief="sunken")
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

b1 = Button(frame_calc, text=1, padx=35,pady=20, command=lambda: add(1), font=('times', 12, 'bold'))
b2 = Button(frame_calc, text=2, padx=35,pady=20, command=lambda: add(2), font=('times', 12, 'bold'))
b3 = Button(frame_calc, text=3, padx=35,pady=20, command=lambda: add(3), font=('times', 12, 'bold'))
b4 = Button(frame_calc, text=4, padx=35,pady=20, command=lambda: add(4), font=('times', 12, 'bold'))
b5 = Button(frame_calc, text=5, padx=35,pady=20, command=lambda: add(5), font=('times', 12, 'bold'))
b6 = Button(frame_calc, text=6, padx=35,pady=20, command=lambda: add(6), font=('times', 12, 'bold'))
b7 = Button(frame_calc, text=7, padx=35,pady=20, command=lambda: add(7), font=('times', 12, 'bold'))
b8 = Button(frame_calc, text=8, padx=35,pady=20, command=lambda: add(8), font=('times', 12, 'bold'))
b9 = Button(frame_calc, text=9, padx=35,pady=20, command=lambda: add(9), font=('times', 12, 'bold'))
b0 = Button(frame_calc, text=0, padx=35,pady=19, command=lambda: add(0), font=('times', 12, 'bold'))
button_add = Button(frame_calc, text="+",padx=34,pady=20, command= btn_add, font=('times', 11, 'bold'))
button_sub = Button(frame_calc, text="-",padx=36,pady=20, command= btn_sub, font=('times', 11, 'bold'))
button_div = Button(frame_calc, text="/",padx=35,pady=20, command= btn_div, font=('times', 11, 'bold'))
button_mul = Button(frame_calc, text="*",padx=35,pady=20, command= btn_mul, font=('times', 11, 'bold'))
button_equal = Button(frame_calc, text="=",padx=125,pady=20, command=equal_btn, font=('times', 12, 'bold'))
button_clear = Button(frame_calc, text="C",padx=35,pady=20, command= btn_clear, font=('times', 11, 'bold'))

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

main_window.mainloop()
