# import pyttsx3

# robot_mouse = pyttsx3.init()
# voices = robot_mouse.getProperty('voices',language = "vi") 
# robot_mouse.setProperty('voice', voices[1].id)

# robot_brain = 'chào'
# robot_mouse.say(robot_brain)
# robot_mouse.runAndWait()
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def speak(t):
    tts = gTTS(text = t,lang = "vi")
    fname = 'voice.mp3'
    tts.save(fname)
    playsound.playsound(fname)

speak('xin chào')
