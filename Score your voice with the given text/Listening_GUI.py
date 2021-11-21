from tkinter import *
import speech_recognition as sr
import os

roots = Tk()

def listening():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
        try:
            print("You have said: \n\n" + r.recognize_google(audio) + "\n")
            print("Audio Recorded Successfully")
            print("You can check your voice in recorded.wav")
            print("And what we record in recorded_text.txt")        
            file = open("recorded_text.txt", "w")
            file.write(r.recognize_google(audio))
            file.close()
            return True
        except Exception as e:
            return False

def maining():
    b = listening()
    if b == False: 
        roots.destroy()
        os.system('python3 ERROR_GUI.py')
    else:
        roots.destroy()
        os.system('python3 Calc_Point.py')
        

button = Button(roots, text = 'Next to record step', fg='red', font=("Times New Roman", 16), command=maining)
button.place(x = 125, y = 60)

roots.title('Hello Python')
roots.geometry("450x200+10+10")
roots.mainloop()