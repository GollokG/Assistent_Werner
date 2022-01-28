import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests
import googletrans
import pyjokes

assistant_name = 'werner'
assistant_keyword = 'werner'
einkaufsliste = []

translator = googletrans.Translator()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang('de')
running = True


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen(ask=None):
    command = ""
    try:
        with sr.Microphone() as source:
            if ask is not None:
                talk(ask)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="de-DE")
            command = command.lower()
    except Exception as e:
        print(e)
    return command


def run_werner():
    command = listen()
    if assistant_keyword in command:
        command = command.replace(assistant_keyword, '')
        print(command)

        if 'sprich mir nach' in command:
            print('Anfrage wird bearbeitet!')
            repeat = command.replace('sprich mir nach', '')  # "sprich mir nach" wird gelöscht (mit nichts ersetzt)
            talk(repeat)

        elif 'uhr' in command:  # Gibt die jetztige Zeit aus
            print('Anfrage wird bearbeitet!')
            time = datetime.datetime.now().strftime('%I:%M')
            date = datetime.date.today().strftime("%d/%m/%Y")
            talk('Es ist ' + date + ' ' + time + 'Uhr')

        elif 'ausschalten' in command:
            global running
            running = False

        else:
            talk('Bitte sage den Befehl erneut.')
            print(command)

try:
    while running:
        run_werner()
except KeyboardInterrupt:
    print('')
finally:
    talk('Adios')
