import speech_recognition as sr
from os import path
from pydub import AudioSegment
# files                                                                         
src = "25.mp3"
dst = "25.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")