import speech_recognition as sr
import  pyautogui as auto
import wikipedia
import pyttsx3
import datetime

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the speech engine
engine = pyttsx3.init()

# Get the current time
current_time = datetime.datetime.now()

# Define the welcome messages
morning_message = "Good morning! Welcome to the day!"
afternoon_message = "Good afternoon! Welcome back!"
evening_message = "Good evening! Welcome to the evening!"

# Define the time ranges
morning_start = 6  # 6:00 AM
morning_end = 12  # 12:00 PM
afternoon_start = 12  # 12:00 PM
afternoon_end = 18  # 6:00 PM
evening_start = 18  # 6:00 PM
evening_end = 22  # 10:00 PM

# Check the current time and speak the appropriate welcome message
if morning_start <= current_time.hour < morning_end:
    engine.say(morning_message)
elif afternoon_start <= current_time.hour < afternoon_end:
    engine.say(afternoon_message)
elif evening_start <= current_time.hour < evening_end:
    engine.say(evening_message)
else:
    engine.say("Welcome!")

# Define a function to open apps
def open_app(app_name):
    pyautogui.press('winleft')  # Press the Windows key
    pyautogui.write(app_name)  # Type the app name
    pyautogui.press('enter')  # Press Enter

# Define a dictionary of app names and their corresponding voice commands
app_commands = {
    'chrome': 'open chrome',
    'notepad': 'open notepad',
    'calculator': 'open calculator'
}

# Define a function to search Wikipedia
def search_wikipedia(query):
    results = wikipedia.search(query)
    article = wikipedia.page(results[0])
    engine.say(article.content)

# Start the speech recognition loop
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_command = r.recognize_google(audio, language='en-US')
            print(voice_command)
            for app, command in app_commands.items():
                if voice_command == command:
                    open_app(app)
            if 'search' in voice_command:
                query = voice_command.replace('search', '')
                search_wikipedia(query)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that")

# Run the speech engine
engine.runAndWait()
