### In Shell laufen lassen #################################
# $env:PATH = "C:\Users\schneider3\ffmpeg\bin;" + $env:PATH

import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("audio_mp3/example3_11min_clearSpeech.mp3")
sound.export("audio_wav/example3_11min_clearSpeech.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "audio_wav/example3_11min_clearSpeech.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))