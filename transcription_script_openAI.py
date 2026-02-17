### In Shell laufen lassen #################################
# pip install git+https://github.com/openai/whisper.git 

### Run in shell ###########################################
# $env:PATH = "C:\Users\schneider3\ffmpeg\bin;" + $env:PATH

### Can't find file? ########################################
# Settings: python.terminal.executeInFileDir

import whisper

model = whisper.load_model("small")
result = model.transcribe("audio_mp3/example4_29min_german.mp3")
print(result["text"])