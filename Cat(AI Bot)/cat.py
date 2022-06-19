from datetime import datetime
from logging import exception
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishMe():
   hour = int(datetime.now().hour)
   if hour >= 0 and hour < 12:
      speak("Good Morning Nisarg!")
   elif hour >=12  and hour <= 18:
      speak("Good Afternoon Nisarg!")
   else:
      speak("Good Evening Nisarg!")

   speak("I am your Groot , I am  Nisarg's Virtual Assistant . Please tell me how I can Help You ")

def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
      print("Recognizing...")
      query = r.recognize_google(audio, language= 'en-in')
      print(f"User said: {query}\n")

   except Exception as E:
      # print(e)
      print("Say that again please...")
      speak("Say that again please...")
      return "None"
   return query

def sendEmail(to, content):
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login("guyhidden40@gmail.com", '9922093488')
   server.sendEmail("guyhidden40@gmail.com", to,content)
   server.close()



if __name__ == "__main__":
   wishMe()
   while True:
   # if 1:
      query = takeCommand().lower()
      # execution
      if 'wikipedia' in query:
         speak("searching in wikipedia...")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)

      elif 'open youtube' in query:
         webbrowser.open("youtube.com")
      elif 'open google' in query:
         webbrowser.open("google.com")
      elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")

      elif 'the time' in query:
         strTime = datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, The time is {strTime}")



      elif "play music" in query:
         music_dir = "C:\\Users\\NISARG WATH\\Music\\AI"
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

      elif "open code" in query:
         codePath = "C\\Users\\NISARG WATH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

      elif "email to" in query:
         try:
            speak("What should i say?")
            content = takeCommand()
            to ="nisargwath7@gmail.com"
            sendEmail(to, content)
            speak("Email had been sent!")
         except Exception as e:
            speak("Sorry my friend Nisarg bhai. I am not able to send this email.")

      elif "about yourself"  in query:
         speak(" Hello I am Groot, I am virtual Virtual Assistant developed by Nisarg, I follow all the  stuff which my sir say")


