### In Shell laufen lassen #################################
# $env:PATH = "C:\Users\schneider3\ffmpeg\bin;" + $env:PATH

import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("audio_mp3/example2_33min.mp3")
sound.export("audio_wav/example2_33min.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "audio_wav/example2_33min.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))