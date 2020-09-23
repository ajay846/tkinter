import mysql.connector
from tkinter import *

global password
password = "123"

global msg
msg = ""

global data
data = ""

global subDb
global subCursor

subDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "yourpass@1#",
    database = "main"
)

subCursor = subDb.cursor()
access_window = Tk()
access_window.title("Password Vault")
access_window.config(bg="aqua")
access_window.eval('tk::PlaceWindow . center')

access_window_frame = Frame(access_window)
access_window_frame.grid(row=1, column=0)

def main():

    menu = Menu(access_window_frame)
    menu.add_command(label="Exit", command=lambda: exit(), font=('courier', '10', 'bold'))

    def check_access():
        passKey = get_passKey.get()

        if passKey == password:
            access_window.destroy()

            passwords_window = Tk()
            passwords_window.title("Password Vault")
            passwords_window.eval('tk::PlaceWindow . center')
            passwords_window.minsize(350, 250)

            menu3 = Menu(passwords_window)
            menu3.add_command(label="Exit", command=lambda: exit())

            def getNewPws():
                passwords_window.destroy()

                add_win = Tk()
                add_win.title("Add Passwords")
                add_win.eval('tk::PlaceWindow . center')

                menu5 = Menu()
                menu5.add_command(label="Exit", command=lambda: exit())

                def add():
                    if for_.get() == "" or username.get() == "" or password_.get() == "":
                        msg = "Fill All The Fields!"
                        label_msg = Label(add_win, text=msg, font=('courier', '10', 'bold'))
                        label_msg.grid(row= 4, column=3)
                    else:
                        site = for_.get()
                        user = username.get()
                        password_new = password_.get()

                        try:
                            mysql = "INSERT INTO users_pws(for_website, username, password_) VALUES(%s,%s,%s)"
                            values = (site, user, password_new)

                            subCursor.execute(mysql, values)
                            subDb.commit()

                            add_win.destroy()

                            success_win = Tk()
                            success_win.title("Success!")
                            success_win.eval('tk::PlaceWindow . center')

                            menu4 = Menu()
                            menu4.add_command(label="Exit", command=lambda: exit())

                            msg = "The data Was Stored Successfully!\nRestart The Program To See data"
                            label_msg = Label(success_win, text=msg, font = ('courier', '10', 'italic'))

                            label_msg.pack()

                            success_win.config(menu=menu4)
                            success_win.mainloop()
                        except:
                            error_win = Tk()
                            error_win.title("Error!")

                            menu6 = Menu()
                            menu6.add_command(label="Exit", command=lambda: exit())

                            msg = "An Unexpected Error Occured And The Password Could Not Be Stored!"
                            label_msg = Label(success_win, text=msg, font = ('courier', '10', 'italic'))

                            label_msg.pack()

                            error_win.config(menu=menu6)
                            error_win.mainloop()

                label_for = Label(add_win, text="For ", font=('courier', '10', 'bold'))
                label_username = Label(add_win, text="Username* ", font=('courier', '10', 'bold'))
                label_password = Label(add_win, text="Password* ", font=('courier', '10', 'bold'))
                for_ = Entry(add_win, width=33, font=('courier', '10', 'bold'))
                username = Entry(add_win, width=33, font=('courier', '10', 'bold'))
                password_ = Entry(add_win, width=33, font=('courier', '10', 'bold'))
                add_btn_pws = Button(add_win, text="Add", font=('courier', '10', 'bold'), command=lambda: add(), padx=80, bg='#a9f08d')

                label_for.grid(row=0, column=0, columnspan=3)
                label_username.grid(row=1, column=0, columnspan=3)
                label_password.grid(row=2, column=0, columnspan=3)
                for_.grid(row=0, column=3)
                username.grid(row=1, column=3)
                password_.grid(row=2, column=3)
                add_btn_pws.grid(row=3, column=3)

                add_win.config(menu=menu5)
                add_win.mainloop()

            menu2 = Menu(passwords_window)
            menu2.add_command(label="Add Password", font=('courier', '10', 'bold'), command=getNewPws)
            menu2.add_command(label="Exit", font=('courier', '10', 'bold'), command=lambda: exit())

            subCursor.execute("SELECT * FROM users_pws")
            results = subCursor.fetchall()

            if subCursor.rowcount == 0:
                msg = "No data found, Add Now!"
                label_msg = Label(passwords_window, text=msg, font=('courier', '10', 'bold'))
                label_msg.pack()
            else:
                for data in results:
                    data_label = Label(passwords_window, text="Id: "+str(data[0])+"\nFor: "+str(data[1])+"\nUsername: "+str(data[2])+"\nPassword: "+str(data[3]), font = ('courier', '10', 'bold'))
                    line = Label(passwords_window, text="-----------------------------------")
                    
                    data_label.pack()
                    line.pack()

            passwords_window.config(menu=menu2)
            passwords_window.mainloop()

        elif passKey == "":
            msg = "Please Enter The Password!"
            label_msg = Label(access_window_frame, text=msg, font=('courier', '10', 'bold'))
            label_msg.grid(column=2)

        elif passKey != password:
            get_passKey.delete(0, 'end')
            msg = "Wrong Password!"
            label_msg = Label(access_window_frame, text=msg, font=('courier', '10', 'bold'))
            label_msg.grid(column=2)

        else:
            msg = "An Unexpected Error Occured!"
            label_msg = Label(access_window_frame, text=msg, font=('courier', '10', 'bold'))
            label_msg.grid(column=2)

    label_1 = Label(access_window_frame, text="Enter Access Key ", font=('courier','11','bold'))
    get_passKey = Entry(access_window_frame, border=2, width=33)
    submit_btn = Button(access_window_frame, text="Get Access", font=('courier','11','bold'), command=check_access)
    submit_btn.config(bg="#8be8a4")

    label_1.grid(row=0, column=0, columnspan=3)
    get_passKey.grid(row=0, column=3)
    submit_btn.grid(row=1, column=3)

    access_window.config(menu=menu)
    access_window.mainloop()

if __name__ == "__main__":
    main()

'''
If Someone Could Help Me With The Delete Button It'd Be Great!
'''

