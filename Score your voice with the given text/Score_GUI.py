from tkinter import *
import speech_recognition as sr
from playsound import playsound

f = open("score.txt", "r")
point = f.read()
f.close()

window = Tk()

labl=Label(window, text="YOUR SCORE: " + str(point), fg='red', font=("Times New Roman", 16))
labl.place(x=70, y=50)

button = Button(window, text = "OK", command=window.destroy)
button.place(x = 135, y = 80)
window.title('Hello Python')
window.geometry("320x200+10+10")
window.mainloop()