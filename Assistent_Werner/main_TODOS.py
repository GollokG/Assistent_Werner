import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests
import googletrans

# TODO: Variable für Name des Assistenten
# TODO: Variable für Keyword, auf dass der Assistent reagiert

# TODO: Einkaufsliste deklarieren (s. Handout)

translator = googletrans.Translator()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang('de')
running = True


# Methode: Assistent redet
def talk(text):
    # TODO: Gesagten Text in der Konsole ausgeben
    engine.say(text)
    engine.runAndWait()


# Methode: Assistent hört zu
def listen():
    command = ""
    try:
        with sr.Microphone() as source:
            print('ich höre zu...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="de-DE")
            command = command.lower()
    except Exception as e:
        print(e)
    # TODO: Command weitergeben


# Zusammenführen der Methoden talk() und listen(): Der Assistent hört hier zu und antwortet/handelt dementsprechend
def run_werner():
    # TODO: Die Methode listen() aufrufen und das gesagte in einer Variablen (z.B.: command) speichern
    # TODO: Vorbedingung für Befehlsausführungen: Keyword soll im Befehl enthalten sein; (Keyword rausfiltern: s. Handout)

    # TODO: UNTERSCHIEDLICHE FÄHIGKEITEN DES ASSISTENTEN EINBAUEN (IF-ABFRAGEN: s. Handout und Beispiel unten)
    """
            if 'sprich mir nach' in command:
                print('Anfrage wird bearbeitet!')
                repeat = command.replace('sprich mir nach', '')  # "sprich mir nach" wird gelöscht (mit nichts ersetzt)
                talk(repeat)

            elif 'uhr' in command:  # Gibt die jetztige Zeit aus
                print('Anfrage wird bearbeitet!')
                time = datetime.datetime.now().strftime('%I:%M')
                date = datetime.date.today().strftime("%d/%m/%Y")
                talk('Es ist ' + date + ' ' + time + 'Uhr')
    """

    # TODO: Ausschalten des Assistenten (Variable: boolean running)
    # TODO: Befehl nicht verstanden -> Bitte sage erneut


# STARTEN DES ASSISTENTEN
try:
    while running:
        run_werner()
except KeyboardInterrupt:
    print('')
finally:
    # Abschiedsphrase des Assistenten
    talk('Adios')
