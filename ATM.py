from tkinter import *
from time import sleep

atm = Tk()
atm.title("Welcome!")
atm.geometry("430x216")

global PIN
global bank_balance
global text_balance

PIN = "2625"
bank_balance = 9000000

text_balance = "Your Bank Balance Is "

def balance():
    label_info_1.destroy()
    label_info_2.destroy()
    label_info_3.destroy()
    label_info_4.destroy()

    bb = Label(atm, text=text_balance+str(bank_balance), font=('times', 12, 'bold'))
    bb.grid(row=1,column=1)

def withdraw():
    label_info_1.destroy()
    label_info_2.destroy()
    label_info_3.destroy()
    label_info_4.destroy()

    def draw():
        bb.destroy()
        withdraw_amt.destroy()
        sub_amt.destroy()

        #amt = withdraw_amt.get()

        #global after

        bank_balance -= int(withdraw_amt.get())

    bb = Label(atm, text=text_balance+str(bank_balance), font=('times', 12, 'bold'))
    bb.grid(row=1,column=1)

    withdraw_amt = Entry(atm)
    withdraw_amt.grid(row=2,column=1)

    sub_amt = Button(atm,text="Withdraw", command=draw)
    sub_amt.grid(row=2,column=2)

def add():
    label_info_1.destroy()
    label_info_2.destroy()
    label_info_3.destroy()
    label_info_4.destroy()

    def add_to_acc():
        add_amt.destroy()
        sub_add.destroy()

        bank_balance += int(add_amt.get())

        bank_after_add = Label(atm,text=text_balance+str(bank_balance))
        bank_after_add.grid(row=2,column=1)

    add_amt = Entry(atm)
    sub_add = Button(atm,text="Add Amount",command=add_to_acc)

    add_amt.grid(row=2,column=1)
    sub_add.grid(row=2,column=2)

def exit():
    label_info_1.destroy()
    label_info_2.destroy()
    label_info_3.destroy()
    label_info_4.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()

    def exitpgm():
        atm.destroy()

    greet = Label(atm, text="Thank You For Visiting!", font=('times', 12, 'bold'))
    greet.pack()

    exit_atm = Button(atm,text="Exit ATM",command=exitpgm)
    exit_atm.pack(side=BOTTOM)

def check():
    if pin.get() == PIN:
        pin.destroy()
        sub0.destroy()

        global b1
        global b2
        global b3
        global b4

        b1 = Button(atm,text=1, padx=25, pady=15, command=balance)
        b2 = Button(atm,text=2, padx=25, pady=15, command=withdraw)
        b3 = Button(atm,text=3, padx=25, pady=15, command=add)
        b4 = Button(atm,text=4, padx=25, pady=15, command=exit)

        global label_info_1
        global label_info_2
        global label_info_3
        global label_info_4

#        label_greet = Label(atm,text="Welcome to ****** Bank!", font=('times', 12, 'bold'))
        label_info_1 = Label(atm,text="To check your bank balance press '1'", font=('times', 10, 'bold'))
        label_info_2 = Label(atm,text="To withdraw cash press '2'", font=('times', 10, 'bold'))
        label_info_3 = Label(atm,text="To add cash press '1'", font=('times', 10, 'bold'))
        label_info_4 = Label(atm,text="To exit press '1'", font=('times', 10, 'bold'))

        b1.grid(row=0,column=0)
        b2.grid(row=1,column=0)
        b3.grid(row=2,column=0)
        b4.grid(row=3,column=0)

#        label_greet.grid(row=0,column=1)
        label_info_1.grid(row=0,column=1)
        label_info_2.grid(row=1,column=1)
        label_info_3.grid(row=2,column=1)
        label_info_4.grid(row=3,column=1)

    else:
        error_label = Label(atm,text="The PIN is incorrect")
        error_label.pack()

pin = Entry(atm)
pin.pack()

sub0 = Button(atm,text="Submit",command=check, padx=15, pady=20)
sub0.pack()

atm.mainloop()
