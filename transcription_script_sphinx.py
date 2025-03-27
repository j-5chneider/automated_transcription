### Download, unzip and move FFmpeg to user folder ########
# https://github.com/BtbN/FFmpeg-Builds/releases

### Run in shell ##########################################
# $env:PATH = "C:\Users\schneider3\ffmpeg\bin;" + $env:PATH

import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("audio_mp3/example2_33min.mp3")
sound.export("audio_wav/example2_33min.wav", format="wav")  # speichert die Datei in einem neuen Ordner


# transcribe audio file                                                         
AUDIO_FILE = "audio_wav/example2_33min.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))