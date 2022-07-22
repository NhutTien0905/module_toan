import speech_recognition as sr
# from datetime import date
# from datetime import datetime
import time
from gtts import gTTS
import os
import playsound
import pandas as pd 

count = 0
def speak(text):
    global count
    tts = gTTS(text=text, lang='vi')
    tts.save(f'speech{count%2}.mp3')
    playsound.playsound(f'speech{count%2}.mp3')
    os.remove(f'speech{count%2}.mp3')

QnA = pd.read_excel("test.xlsx")
ques = QnA["ques"].to_list()
ques1 = QnA["ques1"].to_list()
ans = QnA["ans"].to_list()

while True:
    # khởi tạo tai 
    robot_ear = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    # khởi tạo não
    robot_brain = ''
    print('...')

    # bắt lỗi Runtime
    try:
        you = robot_ear.recognize_google(audio,language = "vi")
    except:
        you = ''

    if you =='':
        robot_brain = "Xin hãy nói lại"
    elif you == "tạm biệt":
        idx = ques1.index(you)
        robot_brain = ans[idx]
        break
    elif you in ques:
        idx = ques.index(you)
        robot_brain = ans[idx]
    elif you in ques1:
        idx = ques1.index(you)
        robot_brain = ans[idx]
    else:
        robot_brain = 'sao chứ'
    
    print('You:',you)
    print('Robot:',robot_brain)
    speak(robot_brain)

    time.sleep(1)

print('You:',you)
print('Robot:',robot_brain)
speak(robot_brain)
