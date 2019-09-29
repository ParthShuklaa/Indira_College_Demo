'''
step1: Import package(gtts-Google text to speech lib)
Step2: Create an Object of class
Step3: Save as Mp3
Step4: Play Mp3

'''

from  gtts import gTTS
import os
mytext = "hello everyone, Welcome to Python Workshop"
MyVoice = gTTS(text=mytext,lang ='en',slow='False')
MyVoice.save("MyVoice.Mp3")
os.system("MyVoice.Mp3")

