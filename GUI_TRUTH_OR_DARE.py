import tkinter
from tkinter import *
import random
from truths import *
from dares import *

win = Tk()
win.title("Truth Or Dare")
win.minsize(450,350)

global player1
global player2
global player3
global player4

def p_2():
    global p_n_1
    global p_n_2

    label1 = Label(win,text="Enter the first player's name: ")
    p_n_1 = Entry(win,width=40)
    label1.grid(row=0,column=0)
    p_n_1.grid(row=0, column=3, columnspan=3)

    label2 = Label(win,text="Enter the second player's name: ")
    p_n_2 = Entry(win,width=40)
    label2.grid(row=1,column=0)
    p_n_2.grid(row=1, column=3, columnspan=3)

    sub_p_2 = Button(win,text="Submit Player Names",command=sub_p_n_2)
    sub_p_2.grid(row=2,column=2)

def p_3():
    global p_n_1
    global p_n_2
    global p_n_3

    label1 = Label(win,text="Enter the first player's name: ")
    p_n_1 = Entry(win,width=40)
    label1.grid(row=0,column=0)
    p_n_1.grid(row=0, column=3, columnspan=3)

    label2 = Label(win,text="Enter the second player's name: ")
    p_n_2 = Entry(win,width=40)
    label2.grid(row=1,column=0)
    p_n_2.grid(row=1, column=3, columnspan=3)

    label3 = Label(win,text="Enter the third player's name: ")
    p_n_3 = Entry(win,width=40)
    label3.grid(row=2,column=0)
    p_n_3.grid(row=2, column=3, columnspan=3)

    sub_p_2 = Button(win,text="Submit Player Names",command=sub_p_n_3)
    sub_p_2.grid(row=3,column=1)

def p_4():
    global p_n_1
    global p_n_2
    global p_n_3
    global p_n_4

    label1 = Label(win,text="Enter the first player's name: ")
    p_n_1 = Entry(win,width=40)
    label1.grid(row=0,column=0)
    p_n_1.grid(row=0, column=3, columnspan=3)

    label2 = Label(win,text="Enter the second player's name: ")
    p_n_2 = Entry(win,width=40)
    label2.grid(row=1,column=0)
    p_n_2.grid(row=1, column=3, columnspan=3)

    label3 = Label(win,text="Enter the third player's name: ")
    p_n_3 = Entry(win,width=40)
    label3.grid(row=2,column=0)
    p_n_3.grid(row=2, column=3, columnspan=3)

    label4 = Label(win,text="Enter the fourth player's name: ")
    p_n_3 = Entry(win,width=40)
    label4.grid(row=3,column=0)
    p_n_3.grid(row=3, column=3, columnspan=3)

    sub_p_2 = Button(win,text="Submit Player Names",command=sub_p_n_4)
    sub_p_2.grid(row=4,column=1)

def submit_players():
    if no_of_players.get() == '2':
        submit_btn_p.destroy()
#        exit_btn.destroy()
        no_of_players.delete(0,END)
        p_2()
    elif no_of_players.get() == '3':
        submit_btn_p.destroy()
#        exit_btn.destroy()
        no_of_players.delete(0,END)
        p_3()
    elif no_of_players.get() == '4':
        submit_btn_p.destroy()
#        exit_btn.destroy()
        no_of_players.delete(0,END)
        p_4()
    elif no_of_players.get() >= '5' or no_of_players.get() <= '1':
        label1.destroy()
        no_of_players.destroy()
        submit_btn_p.destroy()
        label_error = Label(win,text="The number of players cannot be lesser than '2' nor greater than '5'")
        label_error.grid(row=0,column=1)
        exit_btn.grid(row=2,column=1,columnspan=2)

#Storing player names

def sub_p_n_2():
    if p_n_1.get() == p_n_2.get():
        win.destroy()

    else:
        player1 = p_n_1.get()
        player2 = p_n_2.get()

        players = (player1,player2)

        def get_player():
            label_greet.destroy()

            def sh_truths():

                def proceeding():
                    label_truth.destroy()
                    label_p_n.destroy()
                    btn_pro.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_truth = Label(0,text="The truth you have say>> "+random.choice(t))
                label_truth.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            def sh_dares():

                def proceeding():
                    label_dare.destroy()
                    label_p_n.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_dare = Label(0,text="The dare you have say>> "+random.choice(d))
                label_dare.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            label_p_n = Label(0,text="It's "+random.choice(players).capitalize()+"'s turn")
            label_p_n.grid(row=2)

            label_choice = Label(0,text="What's Your Choice?")
    #        label_or = Label(0,text="Or")
            truth_button = Button(sec_win,text="Truth", command=sh_truths)
            dare_button = Button(sec_win,text="Dare", command=sh_dares)
            label_choice.grid(row=3,column=1)
    #        label_or.grid(row=3,column=3)
            truth_button.grid(row=3,column=2)
            dare_button.grid(row=3,column=4)

        win.destroy() #destroy the first window

        sec_win = Tk() #getting to a second window
        sec_win.minsize(450,350)
        sec_win.title("Truth Or Dare")

        label_greet = Label(0,text="Hello "+player1.capitalize()+" and "+player2.capitalize())
        label_greet.grid(row=0,column=0)

        def spin():
            get_command = Button(sec_win,text="Press To Start Spin", width=20, command=get_player)
            get_command.grid(row=1,column=4)

        spin()

        sec_win.mainloop()

#    print(players)

def sub_p_n_3():
    if p_n_1.get() == p_n_2.get() or p_n_1.get() == p_n_3.get():
        win.destroy()
    else:
        player1 = p_n_1.get()
        player2 = p_n_2.get()
        player3 = p_n_3.get()

        players = (player1,player2,player3)

        def get_player():
            label_greet.destroy()

            def sh_truths():

                def proceeding():
                    label_truth.destroy()
                    label_p_n.destroy()
                    btn_pro.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_truth = Label(0,text="The truth you have say>> "+random.choice(t))
                label_truth.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            def sh_dares():

                def proceeding():
                    label_dare.destroy()
                    label_p_n.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_dare = Label(0,text="The dare you have say>> "+random.choice(d))
                label_dare.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            label_p_n = Label(0,text="It's "+random.choice(players).capitalize()+"'s turn")
            label_p_n.grid(row=2)

            label_choice = Label(0,text="What's Your Choice?")
    #        label_or = Label(0,text="Or")
            truth_button = Button(sec_win,text="Truth", command=sh_truths)
            dare_button = Button(sec_win,text="Dare", command=sh_dares)
            label_choice.grid(row=3,column=1)
    #        label_or.grid(row=3,column=3)
            truth_button.grid(row=3,column=2)
            dare_button.grid(row=3,column=4)

        win.destroy() #destroy the first window

        sec_win = Tk() #getting to a second window
        sec_win.minsize(450,350)
        sec_win.title("Truth Or Dare")

        label_greet = Label(0,text="Hello "+player1.capitalize()+", "+player2.capitalize()+" and "+player3.capitalize())
        label_greet.grid(row=0,column=0)

        def spin():
            get_command = Button(sec_win,text="Press To Start Spin", width=20, command=get_player)
            get_command.grid(row=1,column=4)

        spin()

        sec_win.mainloop()

def sub_p_n_4():
    if p_n_1.get() == p_n_2.get() or p_n_3.get() or p_n_4.get() or p_n_2.get() == p_n_3.get() or p_n_4.get() or p_n_3.get() == p_n_4.get():
        win.destroy()
    else:
        player1 = p_n_1.get()
        player2 = p_n_2.get()
        player3 = p_n_3.get()
        player4 = p_n_4.get()

        players = (player1,player2,player3,player4)

        def get_player():
            label_greet.destroy()

            def sh_truths():

                def proceeding():
                    label_truth.destroy()
                    label_p_n.destroy()
                    btn_pro.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_truth = Label(0,text="The truth you have say>> "+random.choice(t))
                label_truth.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            def sh_dares():

                def proceeding():
                    label_dare.destroy()
                    label_p_n.destroy()

                    spin()

                label_choice.destroy()
                truth_button.destroy()
                dare_button.destroy()

                label_dare = Label(0,text="The dare you have say>> "+random.choice(d))
                label_dare.grid(row=2)

                btn_pro = Button(sec_win, text="Proceed", command=proceeding)
                btn_pro.grid(row=3)

            label_p_n = Label(0,text="It's "+random.choice(players).capitalize()+"'s turn")
            label_p_n.grid(row=2)

            label_choice = Label(0,text="What's Your Choice?")
    #        label_or = Label(0,text="Or")
            truth_button = Button(sec_win,text="Truth", command=sh_truths)
            dare_button = Button(sec_win,text="Dare", command=sh_dares)
            label_choice.grid(row=3,column=1)
    #        label_or.grid(row=3,column=3)
            truth_button.grid(row=3,column=2)
            dare_button.grid(row=3,column=4)

        win.destroy() #destroy the first window

        sec_win = Tk() #getting to a second window
        sec_win.minsize(450,350)
        sec_win.title("Truth Or Dare")

        label_greet = Label(0,text="Hello "+player1.capitalize()+", "+player2.capitalize()+", "+player3.capitalize()+" and "+player4.capitalize())
        label_greet.grid(row=0,column=0)

        def spin():
            get_command = Button(sec_win,text="Press To Start Spin", width=20, command=get_player)
            get_command.grid(row=1,column=4)

        spin()

        sec_win.mainloop()

#Design of the first popup

label1 = Label(win,text="Enter the number of players: ")
no_of_players = Entry(win,width=40)
submit_btn_p = Button(win,text="Submit", command= submit_players)
#exit_btn = Button(win,text="Exit Program", command=win.quit)


label1.grid(row=0,column=0)
no_of_players.grid(row=0, column=3, columnspan=3)
submit_btn_p.grid(row=1,column=1,columnspan=3)
#exit_btn.grid(row=3,column=2,columnspan=2)

win.mainloop()
