import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
# getting property voices from engine
voices=engine.getProperty('voices')
# settine voice of david
engine.setProperty('voices',voices[0].id)

# global speak function to speak 
def speak(message):
    # This method will speak whatever is passed as string
    engine.say(message)
    engine.runAndWait()

# This function is invoked everytime the application is started , and it's greet you ont the basis of your system date and time.
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour <=12:
        speak("Good Morning ,boss ,How may I help You")
    elif hour>=12 and hour<16:
        speak("Good Afternoon ,boss ,How may I help You")
    elif hour>=16 and hour<20:
        speak("Good Evening ,boss ,How may I help You")
    else:
        speak("Good Night ,boss ,How may I help You")

# This funtion take input from user in form of speech 
def takeCommand ():
    # It takes microphone input and return string output from it
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        # print(e)
        print("Timed out.")
        exit()

    return query


# Main functioalities of our app starts from here.
if __name__ == '__main__':
    wishMe()

    # Main section for cotinuous listning 
    while True:
        query=takeCommand().lower()
        
        # search something from the wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('Wikipedia',"")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia , ")
            print(results)
            speak(results)

        # Open youtube in your default browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # Open and search specified thing on youtube on your browser.
        elif 'on youtube' in query:
            query=query.replace('on youtube','')
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        # open google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # open and search specified thing on google on your browser
        elif 'on google' in query:
            query=query.replace('on google','')
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # open stackoverflow website on your browser
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        # search a problem on stackoverflow in your browser.
        elif 'on stackoverflow' in query:
            query=query.replace('on stackoverflow','')
            webbrowser.open(f"https://stackoverflow.com/search?q={query}")
        
        # open spotify in you browser.
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        # open and search specific song on spotify on browser if you are logged in of your spotify account.
        elif 'on spotify' in query:
            query=query.replace('on spotify','')
            webbrowser.open(f"https://open.spotify.com/search/{query}")

        # Open instagram in your browser.
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        # Open Facebook in your browser.
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        # To get Current time in form of speech.
        elif 'current time' in query:
            strTime=datetime.datetime.now().strftime("%H %M %S")
            speak(f"sir , The time is {strTime}")

        # To exit from the program.
        elif ('quit' or 'shutdown') in query:
            speak("Quiting sir , Thanks for your time. see you next Time ")
            exit()
        else:
            speak("Sorry sir , I didn't understand ,please speak again")