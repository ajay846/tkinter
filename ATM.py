from tkinter import *
from time import sleep

atm = Tk()
atm.title("Welcome!")
atm.geometry("430x216")
atm.resizable(False,False)

#def main():

global PIN
global bank_balance
global text_balance
global delay

PIN = "2625"
bank_balance = 9000000

text_balance = "Your Bank Balance Is $"

delay = 5

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
        global bank_balance

        bb.destroy()
        withdraw_amt.destroy()
        sub_amt.destroy()

        #global after

        bank_balance -= int(withdraw_amt.get())

    global bb
    global withdraw_amt

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

        global bank_balance

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

    label_info = Label(atm,text="Your Personal Details Are Safe", font=('times', 8, 'bold'))
    label_info.pack()

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

    elif pin.get() == "" or pin.get() == None and pin.get() != None:
        error_label = Label(atm,text="Please Enter the PIN")
        error_label.pack()

#        sleep(delay)

    elif pin.get() != PIN and pin.get() != None or pin.get() != "":
        error_label = Label(atm,text="The PIN is incorrect")
        error_label.pack()

#       sleep(delay)

pin = Entry(atm)
pin.pack()

sub0 = Button(atm,text="Log In",command=check, padx=15, pady=10)
sub0.pack()

atm.mainloop()


'''
    There is a bug in the code. If someone could solve it it'd be of a great help!
'''

'''
    The error is below
        Exception in Tkinter callback
        Traceback (most recent call last):
          File "C:\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
            return self.func(*args)
          File "C:\Users\Uttarkar Sai Nath\Desktop\Python\Tkinter\ATM.py", line 48, in draw
            bank_balance -= int(withdraw_amt.get())
          File "C:\Python\Python36\lib\tkinter\__init__.py", line 2682, in get
            return self.tk.call(self._w, 'get')
        _tkinter.TclError: invalid command name ".!entry2"
'''

'''
    If someone has any solution for this pls dm me on my instagram account @iamsainath.u
'''

