import tkinter
from tkinter import *
import os
import sqlite3

print("Follow me on my Instagram https://www.instagram.com/iamsainath.u/")

global conn
global c
conn = sqlite3.connect("dbTODOLISTS.db")

c = conn.cursor()

print("Connected to "+str(sqlite3.version))


'''
c.execute("""CREATE TABLE tasks (
				tasks_are text
		)""")
		'''

main_win = Tk()
main_win.title("Need To Do")
main_win.resizable(False, False)

tasks_list = Listbox(main_win, bg="white", fg="black", width=60, selectbackground="#e6b1b1", selectforeground="black")
tasks_list.grid(row=0, column=0, columnspan=3)

c.execute("SELECT * FROM tasks")

todoTasks = c.fetchall()

for task_one in todoTasks:
	tasks_list.insert(END, task_one)

def add_task():
	if tasks_list.size() >= 10:
		task_given.delete(0, END)
		task_given.insert(END, "Only 10 tasks allowed")

		task_given.config(state='disabled')
		submit_task.config(state='disabled')

	else:
		try:
			listForTODO = []

			listForTODO.append(task_given.get())

			c.execute("INSERT INTO tasks VALUES(?)", listForTODO)

			conn.commit()

			tasks_list.insert(END, task_given.get())
			task_given.delete(0, END)

		except:
			print("Error Connecting")

def exit_():
	main_win.destroy()

def help_win():
	help_window = Tk()
	help_window.title("Help")
	help_window.resizable(False, False)

	help_win_menu = Menu(help_window)

	def exit_help():
		help_window.destroy()

	help_win_menu.add_command(label="Exit Help Window", command=exit_help)

	label_help = Label(help_window, text="To add tasks there is a entry on the lower side\nTo delete click on task and press the given delete button", font=('times',15,'bold'))
	label_help.pack()

	help_window.config(menu = help_win_menu)
	help_window.mainloop()

def delete_sel_task():
    return

    ''' Was Unable to do this. If anyone knows how to do this dm me on my Instagram>> https://www.instagram.com/iamsainath.u/ '''

def delete_all_task():
	c.execute("DELETE FROM tasks WHERE rowid = 1")
	c.execute("DELETE FROM tasks WHERE rowid = 2")
	c.execute("DELETE FROM tasks WHERE rowid = 3")
	c.execute("DELETE FROM tasks WHERE rowid = 4")
	c.execute("DELETE FROM tasks WHERE rowid = 5")
	c.execute("DELETE FROM tasks WHERE rowid = 6")
	c.execute("DELETE FROM tasks WHERE rowid = 7")
	c.execute("DELETE FROM tasks WHERE rowid = 8")
	c.execute("DELETE FROM tasks WHERE rowid = 9")
	c.execute("DELETE FROM tasks WHERE rowid = 10")

	conn.commit()

	tasks_list.delete(0, END)

label = Label(main_win, text="Enter New Task Here>>")
label.grid(row=1,column=0)

task_given = Entry(main_win, width=27)
task_given.grid(row=1,column=1)

submit_task = Button(main_win, text="Add", command=add_task, relief=GROOVE)
submit_task.grid(row=1,column=2)

del_task = Button(main_win, text="Delete Selected", command=delete_sel_task, relief=GROOVE)
del_task.grid(row=2,column=0)

del_all = Button(main_win, text="Delete All", command=delete_all_task, relief=GROOVE)
del_all.grid(row=2,column=2)

menu = Menu(main_win)

menu.add_command(label="Help", command=help_win)
menu.add_command(label="Exit To Do Task", command=exit)

main_win.config(menu = menu)
main_win.mainloop()