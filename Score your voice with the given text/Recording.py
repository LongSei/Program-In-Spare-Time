import speech_recognition as sr

def main():
 
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
            with open("recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())

            file = open("recorded_text.txt", "w")
            file.write(r.recognize_google(audio))
            file.close()
 
        except Exception as e:
            print("Error :  " + str(e))