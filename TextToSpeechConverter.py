import pyttsx3
from tkinter import *

#convert = input("Enter what to convert to speech: ")

root = Tk()
root.geometry("300x220")
root.title("Text-To-Speech")
root.resizable(False, False)
root.configure(bg='#52ff80')

global engine

engine = pyttsx3.init()
engine.setProperty('rate',140)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speech():
    global convert

    convert = text_field.get(1.0, END)
    print(convert)

    engine.say(convert)
    engine.runAndWait()


global text_field

text_field = Text(root,width=37,height=10, border=1)
text_field.pack()

label_space = Label(root,text="", bg='#52ff80')
label_space.pack()

convert_btn = Button(root,text="Convert",command=speech, border=1)
convert_btn.pack()


root.mainloop()

