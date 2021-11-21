from tkinter import *
import speech_recognition as sr
from playsound import playsound
import os

rootss = Tk()

def main():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
        a = 0
        try:
            print("You have said: \n\n" + r.recognize_google(audio) + "\n")
            print("Audio Recorded Successfully")
            print("You can check your voice in recorded.wav")
            print("And what we record in recorded_text.txt")        
            with open("recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())

            file = open("recorded_text.txt", "w")
            file.write(r.recognize_google(audio))
            file.close()
            a = 1
        except Exception as e:
            a = 2
        
        if a == 1: 
            rootss.destroy()
            os.system('python3 Calc_Point.py')
        else: 
            rootss.destroy()
            os.system('python3 ERROR_GUI.py')

playsound('erro.mp3')
button = Button(rootss, text = 'Can not record, please try again', fg='red', font=("Times New Roman", 16), command=main)
button.place(x = 75, y = 50)

rootss.title('Hello Python')
rootss.geometry("450x200+10+10")
rootss.mainloop()
