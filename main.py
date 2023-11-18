import os
import time
import psutil
import random
import argparse
import keyboard
import threading
from playsound import playsound
import speech_recognition as sr
from pynput.keyboard import Controller
from google_trans_new import google_translator 

keyboard = Controller()  # Create the controller

#this Fun. types the output

def type_string_with_delay(string):
    for character in string: 
        keyboard.type(character) 
        time.sleep(0.02)  

def translator(text):
       line = str(text)
       translator = google_translator()
       lan_srcfm = translator.detect(text)
       text_to_trans = translator.translate(line , lang_tgt=f'{lan_code}' , lang_src=lan_srcfm)
       type_string_with_delay(text_to_trans)
       
    


IS_System_Running = ""

Selected_Language = ""

lan_code = ""


#this fun. to decide language

def System_Main():
	
	global GUI_Running, IS_System_Running, Selected_Language, lan_code  

	while True:
            system_file = open('TEXT FILES\Running_Status.txt')
            system_Sts = system_file.readline()
            system_file.close

	    if IS_System_Running.strip() == "Running" :
                Language_File = open("D:\\gujrati\\voice-typer-main10\\Voice_Typer\\bin\Debug\\Language_Status.txt")
				Selected_Language = Language_File.readline()
				Language_File.close()

				if Selected_Language.strip() == "English":
					lan_code = ""

				elif Selected_Language.strip() == "gujrati":
					lan_code = 'gu'

				elif Selected_Language.strip() == "hindi":
					lan_code = 'hi'
		
		elif GUI_Running.strip() == " ":
			ThisSystem = psutil.Process(os.getpid())
			ThisSystem.terminate()

thread1 = threading.Thread(target = System_Main)
thread1.start()


#This coverts voice into text

while True:
    def voice_to_text():
        if IS_System_Running.strip() == "Running":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('listining...')
                audio = r.listen(source)
            try:
                print('recho...')
                text_by_voice = r.recognize_google(audio,language = '{}'.format(lan_code))
                translator(text_by_voice)
            except:
                print('please try again')
        # retunr text_by_voice
