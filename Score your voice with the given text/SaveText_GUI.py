from tkinter import *
import speech_recognition as sr
from playsound import playsound
import os

def save_data():
  name_info = name.get()

  f = open("text_file.txt", "w")
  f.write(name_info + "\n")
  f.close()

def quit():
    root.destroy()
    os.system('python3 Listening_GUI.py')

root = Tk()
root.title('Hello Python')
root.geometry("800x500+10+10")

name = StringVar()
Entry(root, textvariable=name).place(x= 0, y = 100, width = 800, height = 200)
Button(root, text='Save Data', command=lambda:save_data()).place(x = 340, y = 300)

button = Button(root, text = 'Next to the text', command=quit)
button.place(x = 325, y = 400)

root.mainloop()