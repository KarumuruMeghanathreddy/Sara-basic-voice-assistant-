import pyttsx3 as p
import speech_recognition as sr
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class inflow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button')
        enter.click()
class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
                                       
    def play(self ,query):
        self. query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video= self.driver.find_element(By.XPATH,'//*[@id=-"dismissable"]')
        video.click()
engine=p.init()

engine.setProperty('rate',170)
rate=engine.getProperty("rate")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
  engine.say(text)
  engine.runAndWait()
def wishMe():


  hour=datetime.datetime.now().hour

  if hour >= 0 and hour < 12:

      speak("Hello,Good evening.")
 
  elif hour >= 12 and hour < 18:

      speak("Hello,Good Afternoon")

  else:

      speak("Hello,Good Evening")
wishMe()
speak(" I am Sara at your service  How are you?")
r=sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am absolutely buzzing!!,thank you")
    speak("What can I do for you today")
else:
    speak("What can I do for you today")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    
if "information" in text2:
    speak("On what topic do you want information on?")
    print("On what topic do you want information on?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio=r.listen(source)
        infor=r.recognize_google(audio)
    speak("searching {} on wikipedia".format(infor))
    print("searching {} on wikipedia".format(infor))
    assist = inflow()
    assist.get_info(infor)





#YT_auto.py

elif "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))
    
    assist = music()
    assist.play(vid)
    
