import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound

earings=sr.Recognizer()

with sr.Microphone() as source:
    print("listening...")
    earings.adjust_for_ambient_noise(source)
    voice=earings.listen(source)
    text=earings.recognize_google(voice)
    print(text)




translator=Translator(from_lang='en',to_lang="ml")

translation=translator.translate(text)

print(translation)

mal=gTTS(translation,lang="ml")
mal.save("voice.mp3")
playsound("voice.mp3")