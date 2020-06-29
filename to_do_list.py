from tkinter import *
import os

'''
This Is really basic type of To-Do List Application as even I'm a fresh man to the tkinter graphics.
'''

root = Tk()
root.title("Your To-Do List")
root.geometry("400x500")
sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

def add_to_list():

    empty.destroy()
    add_more.destroy()

    add = Label(root,text="Add Here >>>")
    add.pack()

    global add_to

    add_to = Entry(root)
    add_to.pack()

    submit = Button(root,text="Add>>",command=store)
    submit.pack()

    exit = Button(root,text="Exit",command=root.quit)
    exit.pack()

def store():
    f = open("toDoListx54if.txt","a")
    f.write(add_to.get())
    f.write("\n")
    f.close()
    add_to.delete(0,END)

#    showi()

if os.path.isfile("toDoListx54if.txt") == False: #Give it a unique name
    f = open("toDoListx54if.txt","x")

if os.path.getsize("toDoListx54if.txt") == 0:
    empty = Label(root,text="Your To-Do List is empty :(")
    empty.pack()

    add_more = Button(root,text="Update Your To-Do List",command=add_to_list)
    add_more.pack()

    exit = Button(root,text="Exit",command=root.quit)
    exit.pack()

def submit_a():
    f = open("toDoListx54if.txt","a")
    f.write(add_to.get())
    f.write("\n")
    f.close()
    add_to.delete(0,END)

#    showi()

def store_a():
    show.destroy()
    add_more_a.destroy()
    delete.destroy()

    add = Label(root,text="Add Here >>>", font=("Times New Roman", 12))
    add.pack()

    global add_to

    add_to = Entry(root)
    add_to.pack()

    submit = Button(root,text="Add>>",command=submit_a)
    submit.pack()

    exit = Button(root,text="Exit",command=root.quit)
    exit.pack()

if os.path.getsize("toDoListx54if.txt") != 0:
    def delete_data():
        os.remove("toDoListx54if.txt")
        if os.path.isfile("toDoListx54if.txt") == False:
            show.destroy()
            add_more_a.destroy()
            delete.destroy()
            res = Label(root, text="Deleted The List!", font=("Times New Roman", 17))
            res.pack()
            exit = Button(root,text="Exit",command=root.quit)
            exit.pack()
        else:
            res = Label(root, text="An error occured please try again later!", font=("Times New Roman", 17))
            res.pack()
            exit = Button(root,text="Exit",command=root.quit)
            exit.pack()

    def showi():
        f = open("toDoListx54if.txt","r")
        tasks = f.read()

        global show
        global add_more_a
        global delete

        show = Label(root,text=tasks, font=("Times New Roman", 13))
        show.pack(side=TOP, anchor=NW)

        add_more_a = Button(root,text="Add To To-Do List",command=store_a)
        add_more_a.pack()

        delete = Button(root,text="Delete The List",command=delete_data)
        delete.pack()

        exit = Button(root,text="Exit",command=root.quit)
        exit.pack()

    showi()

#sb.configure(command=show.yview) I'm not able to get this!

root.mainloop()