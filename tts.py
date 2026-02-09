from gtts import gTTS
import os

def beispiel():
    text = "Hallo! Das ist ein Test der Sprachausgabe."
    tts = gTTS(text=text, lang='de')
    tts.save("test.mp3")

    print("Datei 'test.mp3' wurde erstellt!")