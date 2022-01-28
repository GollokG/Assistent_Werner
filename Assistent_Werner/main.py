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

        elif 'hallo' in command:
            print("Anfrage wird bearbeitet!")
            name = listen("Hallo, wie ist dein Name?")
            talk(
                'Hallo, ' + name + ' ! Ich bin ' + assistant_name + ', dein persönlicher Sprachassistent. Benutze das Codewort "' + assistant_keyword + '", um mich zu benutzen!')

        elif 'spiele' in command:
            print('Anfrage wird bearbeitet!')
            song = command.replace('spiele', '')
            talk('Spiele ' + song)
            pywhatkit.playonyt(song)

        elif 'öffne meine einkaufsliste' in command:
            counter = 0
            print('Anfrage wird bearbeitet!')
            while counter <= 1:
                command = listen(
                    'Was willst du machen? Sehen, Hinzufügen oder Löschen?')  # Oder Einfach talk und dann command nehmen
                if 'sehen' in command:
                    talk(einkaufsliste)
                    break
                elif 'hinzufügen' in command:
                    item = listen('Was willst du deiner Einkaufsliste hinzufügen?')
                    einkaufsliste.append(item)
                    print(einkaufsliste)
                    break
                elif 'löschen' in command:
                    print(einkaufsliste)
                    item = listen('Was willst du aus deiner Einkaufsliste löschen?')
                    if item in einkaufsliste:
                        einkaufsliste.remove(item)
                        break
                    else:
                        talk("Dieser Gegenstand ist nicht in deiner Einkaufsliste vorhanden!")
                        counter += 1
                    print(einkaufsliste)
                else:
                    talk("Ich habe dich nicht verstanden. Bitte wiederhole den Befehl!")
                    counter += 1

        elif 'öffne' in command:
            print('Anfrage wird bearbeitet!')
            website = command.replace(' öffne ', '')
            talk('Öffne' + website)
            webbrowser.open('www.' + website)

        elif 'route' in command:
            print('Anfrage wird bearbeitet')
            start = listen('Wo möchtest du starten?')
            print(start)
            start = start.replace(' ', '+')
            dest = listen('Wohin soll die Route führen?')
            print(dest)
            dest = dest.replace(' ', '+')
            webbrowser.open('https://www.google.de/maps/dir/' + start + '/' + dest)

        elif 'suche nach' in command:
            print('Anfrage wird bearbeitet!')
            website = command.replace(' suche nach ', '')
            talk('Suche nach' + website)
            webbrowser.open(
                'www.google.com/search?q=' + website)  # Hier die Schüler auffordern herauszufinden, wie die Suchadresse aufgebaut ist

        elif 'uhr' in command:  # Gibt die jetztige Zeit aus
            print('Anfrage wird bearbeitet!')
            time = datetime.datetime.now().strftime('%I:%M')
            date = datetime.date.today().strftime("%d/%m/%Y")
            talk('Es ist ' + date + ' ' + time + 'Uhr')

        elif 'suche auf wikipedia nach' in command:  # Einschränkungen bei '.' im ersten Wikipedia Satz
            print('Anfrage wird bearbeitet!')
            search = command.replace('suche auf wikipedia nach', '')
            info = wikipedia.summary(search, 1)
            talk(info)

        elif 'bist du single' in command:
            print('Anfrage wird bearbeitet!')
            talk('Ich bin in einer Beziehung mit Schrödinger, oder auch nicht.')

        elif 'wie ist das wetter in' in command:
            print('Anfrage wird bearbeitet!')
            city = command.replace('wie ist das wetter in', '')
            url = 'https://wttr.in/' + city
            res = requests.get(url)
            talk('Hier ist der Wetterbericht für ' + city)
            print(res.text)

        elif 'übersetze' in command:
            print('Anfrage wird bearbeitet!')
            input = command.replace('übersetze', '')
            translation = translator.translate(input)
            translation = translation.text
            engine.setProperty('voice', voices[1].id)
            talk(translation)
            engine.setProperty('voice', voices[0].id)

        elif 'witz' in command:
            joke = pyjokes.get_joke(language='de')
            talk(joke)

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
