
import pyttsx3 #speak audio
import datetime
import webbrowser as wb
import speech_recognition as sr 
import smtplib
import wikipedia #for accessing wikipedia
import os
import pyautogui
import pyjokes
import psutil #battery status and cpu usage

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def time():
     speak("the time is")
     Time=datetime.datetime.now().strftime("%H:%M:%S")
     speak(Time)
     
def date():
    speak("today's date is")
    year=int(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak(month)
    speak(day)
    speak(year)

     

def wish_me():
    
   hour=datetime.datetime.now().hour
   if hour>=6 and hour<12:
      speak("good morning sir!...") 
   elif hour>=12 and hour<18:
      speak("good afternoon sir!.....")
   elif hour>=18 and hour<24:
       speak("good evenning sir!!")
   else:
      speak("good night sir")   
   speak("jarvus at your service . plese tell me how can i help you sir!")   

def take_command():
    r =sr.Recognizer()
    with sr.Microphone() as source:
      speak("Listening....")
      print("Listning...")
      audio=r.listen(source) 

    try:
       text=r.recognize_google(audio, language='en-in')
       print(text)
       
    except Exception as e:
            print(e)
            speak("say that again please") 
        
            return  'None'  
    return text
def jokes():
    speak(pyjokes.get_joke())

#send email
def sendemail(to, content):
      server=smtplib.SMTP('smtp.gmail.com',587) 
      server.ehlo()
      server.starttls()
      server.login('1805688@kiit.ac.in','MANISH12345')
      server.sendmail('1805688@kiit.ac.in',to,content)
      server.close()
#chrome search
#screenshot
#def screenshot():
  #   img= pyautogui.screenshot()
 #    img.save("C:\Users\KIIT\Pictures\Screenshots\ss.png")
def cpu():
     usage = str(psutil.cpu_percentage())
     speak('cpu is at'+ usage)
     battery = psutil.sensor_battery()
     speak("battery is at ")
     speak(battery.percent)
#main function 
if __name__ == "__main__":
    wish_me()
    while True:
       text = take_command().lower()


       if 'time' in text:
           time() 
       elif 'date' in text:
            date()
       elif 'exit' in text:
           speak("have a nice day sir!")
           exit()     
       elif 'wikipedia' in text:   #search in wikipedia
           speak("searching....")
           text=text.replace("wikipedia","")
           result=wikipedia.summary(text, sentences=2)
           print(result)
           speak(result) 
       elif 'search in chrome' in text:
            speak("what should i search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=take_command().lower()
            wb.get(chromepath).open_new_tab(search +'.com')

       elif 'send email' in text:
            try:
                speak("what should i say?")
                content=take_command()
                to='manishyadav2056107@gmail.com'
                sendemail(to,content)
                speak("email has been send successfully....")

            except Exception as e:
                print(e)
                speak("unable to send your email")   

       elif 'shutdown' in text:
           speak("windows shutting down")
           os.system("shutdown -1")
       
       elif 'play songs' in text:
           songs_dir='E:/s9/all/Download'
           songs=os.listdir(songs_dir)
           os.startfile(os.path.join(songs_dir, songs[0]))            
       elif 'remember that' in text:
           speak("what should i remember?")
           data = take_command()
           speak("'you said me to remember "+data)
           remember =open('data.txt','w')
           remember.write(data)
           remember.close()

       elif 'do you know anything' in text:
           remember=open('data.txt', 'r')
           speak("you said me to remember that"+ remember.read())    

       elif 'joke' in text:
           jokes() 
        
       elif 'cpu' in text:
           cpu()
#       elif 'screenshot' in text:
 #          screenshot()

