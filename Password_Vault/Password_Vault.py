"""
    *Any issues or doubts related to any of my projects feel free to DM me on my Instagram acc...
    *Link to my instagram -> https://www.instagram.com/u_sai00_
    *Username - u_sai00_
"""
"""
    *I'm using MySQL as my database for this project 
"""

import mysql.connector
from tkinter import *
import webbrowser

global msg
msg = ""

global data
data = ""

global subDb
global subCursor

#Connect to database
subDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootmysql@1#",
    database = "main"
)

#Create cursor
subCursor = subDb.cursor()

#Main Tkinter Window 
access_window = Tk()
access_window.title("Password Vault")
access_window.eval('tk::PlaceWindow . center')
access_window.resizable(False, False)

#Creating frames on access window
access_window_frame = Frame(access_window)
headerFrame = Frame(access_window)

headerFrame.grid(row=0, column=0)
access_window_frame.grid(row=1, column=0)

#To get the main access password from the database table "mainPass"
subCursor.execute("SELECT * FROM mainPass")
passData = subCursor.fetchall()

for passD in passData:
    global password
    password = passD[0]

#Function main
def main():
    name = Label(headerFrame, text="Password Safe", font=('courier', '15', 'bold italic'))
    name.pack()

    menu = Menu(access_window_frame)
    menu.add_command(label="Exit", command=lambda: exit(), font=('courier', '10', 'bold'))

    #Check if user has entered a correct password or not
    def check_access():
        passKey = get_passKey.get()

        if passKey == password:
            access_window.destroy()

            #Window to show stored passwords
            passwords_window = Tk()
            passwords_window.title("Password Vault")
            passwords_window.eval('tk::PlaceWindow . center')
            passwords_window.minsize(400, 250)

            menu3 = Menu(passwords_window)
            menu3.add_command(label="Exit", command=lambda: exit())

            #Another window to get new passwords
            def getNewPws():
                passwords_window.destroy()

                global add_win

                add_win = Tk()
                add_win.title("Add Passwords")
                add_win.eval('tk::PlaceWindow . center')
                add_win.resizable(False, False)

                global menu5

                menu5 = Menu()
                menu5.add_command(label="Exit", command=lambda: exit())

            #Change the main password
            def changePass():
                changeP = Tk()
                changeP.title("Change Password")

                #Varify if the old password is correct
                def varify():
                    subCursor.execute("SELECT * FROM mainPass")
                    passData = subCursor.fetchall()

                    for passD in passData:
                        if oldPass.get() == "" or newPass.get() == "":              #Empty 
                            msg = "The new/old password should not be empty!"
                            lblRes = Label(changeP, text=msg).grid(row=10, column=1)

                        else:
                            if str(oldPass.get()) == str(passD[0]):
                                new = []        #List to store the newly given password
                                new.clear()
                                new.append(newPass.get())

                                #MySQL stuff
                                subCursor.execute("TRUNCATE mainPass")
                                subDb.commit()

                                sql = "INSERT INTO mainPass(password_, id) VALUES(%s, 9)"
                                val = new

                                subCursor.execute(sql, val)
                                subDb.commit()

                                msg = "Password Was Changed!"
                                lblRes = Label(changeP, text=msg).grid(row=3, column=1)
                            else:                                                       #Wrong password
                                msg = "WRONG PASSWORD!"
                                lblRes = Label(changeP, text=msg).grid(row=9, column=0)

                #Tkinter stuff to get new password
                lblOldPass = Label(changeP, text="Old Password")
                oldPass = Entry(changeP, width=33)
                lblNewPass = Label(changeP, text="New Password")
                newPass = Entry(changeP, width=33)
                submitNew = Button(changeP, text="Change Password", command=varify)

                lblOldPass.grid(row=0, column=0)
                oldPass.grid(row=0, column=1)
                lblNewPass.grid(row=1, column=0)
                newPass.grid(row=1, column=1)
                submitNew.grid(row=2, column=0)

                changeP.mainloop()

            #In case you want to contact me
            def contact():
                webbrowser.open("https://www.instagram.com/u_sai00_")

                #Add more passwords
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
                            #MySQL stuff
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
                            pass

                #Tkinter to get newer passwords
                label_for = Label(add_win, text="For ", font=('courier', '10', 'bold'))
                label_username = Label(add_win, text="Username* ", font=('courier', '10', 'bold'))
                label_password = Label(add_win, text="Password* ", font=('courier', '10', 'bold'))
                for_ = Entry(add_win, width=33, font=('courier', '10', 'bold'))
                username = Entry(add_win, width=33, font=('courier', '10', 'bold'))
                password_ = Entry(add_win, width=33, font=('courier', '10', 'bold')).grid(row=2, column=3)
                Label(add_win, text="Required (*)", font=('courier', '8', 'italic')).grid(row=3, column=2)
                add_btn_pws = Button(add_win, text="Add", font=('courier', '10', 'bold'), command=lambda: add(), padx=80, bg='#a9f08d')

                label_for.grid(row=0, column=0, columnspan=3)
                label_username.grid(row=1, column=0, columnspan=3)
                label_password.grid(row=2, column=0, columnspan=3)
                for_.grid(row=0, column=3)
                username.grid(row=1, column=3)
                add_btn_pws.grid(row=3, column=3)

                add_win.config(menu=menu5)
                add_win.mainloop()

            menu2 = Menu(passwords_window)
            menu2.add_command(label="Add Password", font=('courier', '10', 'bold'), command=getNewPws)
            menu2.add_command(label="Exit", font=('courier', '10', 'bold'), command=lambda: exit())
            menu2.add_command(label="Change Main Password", command=changePass)
            menu2.add_command(label="Contact Dev", font=('courier', '10', 'bold'), command= contact)

            subCursor.execute("SELECT * FROM users_pws")
            results = subCursor.fetchall()

            if subCursor.rowcount == 0:
                msg = "No data found, Add Now!"
                label_msg = Label(passwords_window, text=msg, font=('courier', '10', 'bold'))
                label_msg.pack()
            else:
                #SCROLL BAR
                passwordsFrame = Frame(passwords_window)
                passwordsFrame.pack(fill=BOTH, expand=1)

                passwordsCanvas = Canvas(passwordsFrame)
                passwordsCanvas.pack(side=LEFT, expand=1, fill=BOTH)

                pageScroll = Scrollbar(passwordsFrame, orient=VERTICAL, command=passwordsCanvas.yview)
                pageScroll.pack(side=RIGHT, fill=Y)

                passwordsCanvas.configure(yscrollcommand=pageScroll.set)
                passwordsCanvas.bind('<Configure>', lambda e: passwordsCanvas.configure(scrollregion = passwordsCanvas.bbox("all")))

                passwordsFrame_2 = Frame(passwordsCanvas)
                passwordsFrame_2.config(bg="white")

                passwordsCanvas.create_window((0,0), window=passwordsFrame_2, anchor=NW)
                passwordsCanvas.config(bg="white")

                #To delete a entry
                def delete(objToDel):
                    subCursor.execute("DELETE FROM users_pws WHERE id="+str(int(objToDel)))
                    subDb.commit()

                #Show passwords
                for data in results:
                    data_label = Label(passwordsFrame_2, text="Id: "+str(data[0])+"\nFor: "+str(data[1])+"\nUsername: "+str(data[2])+"\nPassword: "+str(data[3]), font = ('courier', '10', 'bold'), bg="white")
                    btn = Button(passwordsFrame_2, text="Delete", command=lambda d=data[0]: delete(d))
                    line = Label(passwordsFrame_2, text="-----------------------------------", bg="white")
                    
                    data_label.pack()
                    btn.pack()
                    line.pack()

            passwords_window.config(menu=menu2)
            passwords_window.mainloop()

        #Few conditions
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

    #Main access window things
    label_1 = Label(access_window_frame, text="Enter Access Key ", font=('courier','11','bold'))
    get_passKey = Entry(access_window_frame, border=2, width=33)
    submit_btn = Button(access_window_frame, text="Get Access", font=('courier','11','bold'), command=check_access)
    submit_btn.config(bg="#8be8a4")

    label_1.grid(row=0, column=0, columnspan=3)
    get_passKey.grid(row=0, column=3)
    submit_btn.grid(row=1, column=3)

    access_window.config(menu=menu)
    access_window.mainloop()

#Pythonic stuff
if __name__ == "__main__":
    main()


