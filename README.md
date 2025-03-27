# How to: automated_transcription

## 1. Install VS Code

* Open the "Microsoft Store" on your laptop
* Type in "VS Code" in the search bar on top
* Click "Install" Button (installations from the store are possible without admin rights)


## 2. Download ffmpeg

* Download "ffmpeg-master-latest-win64-gpl-shared.zip" from [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases)
* Unzip the folder, rename the unzipped folder to "ffmpeg"
* copy the folder "ffmpeg" to C:\Users\[YOUR NAME]\ *(replace [YOUR NAME] with your user's folder name)*

## 3. Create a new folder & workspace in VS Code

* In VS Code create a new folder for your project and make it a workspace
* Within this folder create a folder "audio_mp3" where you'll save your audio files

## 4. Set up the environment

In VS Code, run  this in the shell:

* `pip install git+https://github.com/openai/whisper.git`
* `$env:PATH = "C:\Users\[YOUR NAME]\ffmpeg\bin;" + $env:PATH` *(replace [YOUR NAME] with your user's folder name)*
    - Test if VS Code can find ffmpeg by running `ffmpeg -version` in the shell

# 5. Run the transcription script

* Update the name of your file to transcribe
* Run the script
* ...
* Profit