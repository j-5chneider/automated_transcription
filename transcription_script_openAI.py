### In Shell laufen lassen #################################
# pip install git+https://github.com/openai/whisper.git 

### Run in shell ##########################################
# $env:PATH = "C:\Users\schneider3\ffmpeg\bin;" + $env:PATH

import whisper

model = whisper.load_model("small")
result = model.transcribe("audio_mp3/example2_33min.mp3")
print(result["text"])