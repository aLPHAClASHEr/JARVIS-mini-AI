import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
# Sapi5 is a Microsoft based speech API
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:    
        speak("Good Evening!")
    speak("How may I help you?")



def takeCommand():
    '''
    It takes michrophone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Zara is listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
      
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n" )

    except Exception as e:
        #print(e)
        
        print('Say that again please....')
        return "None"
    return query



if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
    
        #logic for executing tasks for queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open code' in query:
            #codePath = "C:\\Users\\Hazel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.system("Visual Studio Code")

        elif 'play music' in query:
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

        elif 'change the song' in query:
            music_dir = "D:\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))    
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")