
import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def respond(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()
    # tts = gTTS(text=audioString, lang='en')
    # tts.save("speech.mp3")
    # os.system("mpg321 speech.mp3")



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")

    if "what time is it" in data:
        listening = True
        respond(ctime())

    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening

time.sleep(6)
respond("Hi aghead, what can I do for you?")
listening = True


while listening == True:
    data = listen()
    listening = digital_assistant(data)
