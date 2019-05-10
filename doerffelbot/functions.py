# -*- coding: utf-8 -*-

import requests
from yahooweather import YahooWeather, UNIT_C
from emoji import emojize
import pickle
import CONFIG as conf


# reaction for "/start"
def start(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)

    print("{} hat den bot gestartet (chat_id: {})".format(
        gotten_chat.first_name, str(gotten_chat.id)))

    # welcome message
    bot.send_message(chat_id=update.message.chat_id, text=("Hello "+gotten_chat.first_name+"!\nMy name is Doerffelbot.\n" +
                                                           "I'm a student project of two awesome German students " +
                                                           "of the Georg-Samuel-Dörffel-Gymnasium in Weida.\n\n" +
                                                           "At the moment I only react to /help, /links, /vertretung and /wetter, " +
                                                           "but if we have some more ideas which seem usefull to us, we will implement them!\n" +
                                                           "\nPS: If you have any inspirations, please send them to Joheihe@web.de"))

    with open("data/ids.set", 'rb') as doc:
        try:
            ids = pickle.load(doc)
        except:
            ids = set()

    ids.add(gotten_chat.id)

    print("{} wurde der chat_id-Liste hinzugefügt\nids={}\n".format(gotten_chat.first_name, ids))

    with open("data/ids.set", 'wb') as doc:
        pickle.dump(ids, doc)


# reaction for "/help"
def helpme(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)

    bot.send_message(chat_id=update.message.chat_id, text=("Momentan reagiere ich nur auf die Befehle: /start, /help, /links, /vertretung und /wetter. " +
                                                           "\nSollten wir aber noch weitere Ideen haben, implementieren wir diese nat�rlich! Viel Spa�!"))
    print(gotten_chat.first_name+" hat um Hilfe gebeten\n")


# reaction for "/links"
def links(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)

    bot.send_message(chat_id=update.message.chat_id, text=("Hier sind ein paar interessante Links:\n" +
                                                           " - Homepage: http://www.doerffelgymnasium.de/cms/\n" +
                                                           " - News: http://www.doerffelgymnasium.de/cms/index.php/news\n" +
                                                           " - Schulspeisung: https://www.wakos-gera.de/bestellen/schulspeisung"))

    print(gotten_chat.first_name+" hat die Links angefordert\n")


def download_vertretung():

    url = "https://doerffelgymnasium.de/vplan/Vertretung.pdf"

    r = requests.get(url, auth=(conf.vplan["username"], conf.vplan["password"]), stream=True)

    with open("data/vertretung.pdf", 'wb') as doc:
        for chunk in r.iter_content(chunk_size=128):
            doc.write(chunk)
    
        print(doc.name, "wurde heruntergeladen")


# reaction for "/vertretung"
def vertretung(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)

    download_vertretung()

    bot.sendDocument(chat_id=update.message.chat_id,
                     document=open("data/vertretung.pdf", 'rb'))
    print("und zu "+gotten_chat.first_name+" geschickt\n")


# reaction for "/wetter"
def wetter(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)

    # query weather data for "Weida, Germany"
    yweather = YahooWeather(704463, UNIT_C)
    print("Wetterdaten wurden empfangen")

    if yweather.updateWeather():
        bot.send_message(chat_id=update.message.chat_id, text="Wetter f�r Weida, TH, Germany:" +
                         "\nBeschreibung: "+str(yweather.Forecast[0]['text']) +
                         "\nAktuelle Temperatur: "+emojize(" :arrow_right:", use_aliases=True)+" "+str(yweather.Now['temp'])+" �C"+emojize(" :arrow_left:", use_aliases=True) +
                         "\nH�chsttemperatur: "+emojize(" :arrow_up:", use_aliases=True)+" "+str(yweather.Forecast[0]['high'])+" �C"+emojize(" :arrow_up:", use_aliases=True) +
                         "\nNiedrigsttemperatur: "+emojize(" :arrow_down:", use_aliases=True)+" "+str(yweather.Forecast[0]['low'])+" �C"+emojize(" :arrow_down:", use_aliases=True) +
                         "\nSonnenaufgang: "+str(yweather.Astronomy['sunrise'])+emojize(" :arrow_heading_up:", use_aliases=True) +
                         "\nSonnenuntergang: "+str(yweather.Astronomy['sunset'])+emojize(" :arrow_heading_down:", use_aliases=True))  # schickt aktuelle Wetterdaten
        print("und zu "+gotten_chat.first_name+" geschickt\n")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Konnte yahoo-Wetterdaten nicht empfangen!")  # Fehlermeldung
        print("und konnten nicht zu "+gotten_chat.first_name +
              " geschickt werden\n")  # Statusmeldung: Fehler bei Wetterdaten


# react to all non-commands
def react(bot, update):

    bot.send_message(chat_id=update.message.chat_id, text=(
        "Hallo User, ich habe Dich leider nicht verstanden!\nTippe /help um mehr zu erfahren!"))
