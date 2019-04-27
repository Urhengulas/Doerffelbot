# -*- coding: utf-8 -*-

from urllib3 import PoolManager
from yahooweather import YahooWeather, UNIT_C
from emoji import emojize
import pickle


#fügt die Reaktion auf den Befehl "/start" hinzu
def start(bot, update): #definiert methode zu /start
    gotten_chat=bot.get_chat(chat_id=update.message.chat.id) #greift alle Daten der Message ab
    print(gotten_chat.first_name+" hat den bot gestartet (chat_id:"+str(gotten_chat.id)+")") #Statusmeldung: wer hat bot gestartet

    bot.send_message(chat_id=update.message.chat_id, text=  ("Hello "+gotten_chat.first_name+"!\nMy name is Doerffelbot.\n"+
                                                            "I'm a student project of two awesome German students "+
                                                            "of the Georg-Samuel-Dörffel-Gymnasium in Weida.\n\n"+
                                                            "At the moment I only react to /help, /links, /vertretung and /wetter, "+
                                                            "but if we have some more ideas which seem usefull to us, we will implement them!\n"+
                                                            "\nPS: If you have any inspirations, please send them to Joheihe@web.de")) #sendet dem User die Begr��ungsmessage
    
    with open("../ids.set", 'rb') as doc:
        ids = pickle.load(doc) #lädt die chat_id-Menge
    ids.add(gotten_chat.id) #fügt die aktuelle chat_id hinzu
    print(gotten_chat.first_name+" wurde der chat_id-Liste hinzugefügt\nids=",ids,"\n") #Statusmeldung: id wurde gespeichert + gibt die Menge der chat_id's aus
    with open("../ids.set", 'wb') as doc:
        pickle.dump(ids, doc) #speichert die chat_id_Menge


#fügt die Reaktion auf den Befehl "/help" hinzu
def helpme(bot, update): #definiert methode zu /help
    gotten_chat=bot.get_chat(chat_id=update.message.chat.id) #greift alle Daten der Message ab
    bot.send_message(chat_id=update.message.chat_id, text=  ("Momentan reagiere ich nur auf die Befehle: /start, /help, /links, /vertretung und /wetter. "+
                                                             "\nSollten wir aber noch weitere Ideen haben, implementieren wir diese nat�rlich! Viel Spa�!")) #sendet dem User die Hilfsmessage
    print(gotten_chat.first_name+" hat um Hilfe gebeten\n") #Statusmeldung: um Hilfe gebeten


#f�gt die Reaktion auf den Befehl "/links" hinzu
def links(bot, update): #definiert methode zu /links
    gotten_chat=bot.get_chat(chat_id=update.message.chat.id) #greift alle Daten der Message ab
    bot.send_message(chat_id=update.message.chat_id, text=  ("Hier sind ein paar interessante Links:\n"+
                                                             " - Homepage: http://www.doerffelgymnasium.de/cms/\n"+
                                                             " - News: http://www.doerffelgymnasium.de/cms/index.php/news\n"+
                                                             " - Schulspeisung: https://www.wakos-gera.de/bestellen/schulspeisung")) #sendet dem User die Hilfsmessage
    print(gotten_chat.first_name+" hat die Links angefordert\n") #Statusmeldung: um Hilfe gebeten


def download_vertretung():
    url = 'www.doerffelgymnasium.de/leitung/vertretung.pdf'
    http = PoolManager()
    resp = http.request('GET', url, preload_content=False)
    with open("Vertretung.pdf", 'wb') as doc:
        doc.write(resp.data)
    resp.release_conn()
    print(file.name,"wurde heruntergeladen")


#f�gt die Reaktion auf den Befehl "/vertretung" hinzu
def vertretung(bot, update): #definiert methode zu /vertretung
    gotten_chat=bot.get_chat(chat_id=update.message.chat.id) #greift alle Daten der Message ab
    
    download_vertretung()

    bot.sendDocument(chat_id=update.message.chat_id, document=open("Vertretung.pdf", 'rb')) #sendet dem user den Vertretungsplan, Bezug durch selbst-downloaden
    print("und zu "+gotten_chat.first_name+" geschickt\n")


#f�gt die Reaktion auf den Befehl "/wetter" hinzu
def wetter(bot, update): #definiert methode zu /wetter
    gotten_chat=bot.get_chat(chat_id=update.message.chat.id) #greift alle Daten der Message ab

    yweather = YahooWeather(704463, UNIT_C) #fragt Wetterdaten ab
    print("Wetterdaten wurden empfangen") #Statusmeldung: Wetterdaten verf�gbar

    if yweather.updateWeather():
        bot.send_message(chat_id=update.message.chat_id, text=
                                                  "Wetter f�r Weida, TH, Germany:"+
                                                  "\nBeschreibung: "+str(yweather.Forecast[0]['text'])+
                                                  "\nAktuelle Temperatur: "+emojize(" :arrow_right:", use_aliases=True)+" "+str(yweather.Now['temp'])+" �C"+emojize(" :arrow_left:", use_aliases=True)+
                                                  "\nH�chsttemperatur: "+emojize(" :arrow_up:", use_aliases=True)+" "+str(yweather.Forecast[0]['high'])+" �C"+emojize(" :arrow_up:", use_aliases=True)+
                                                  "\nNiedrigsttemperatur: "+emojize(" :arrow_down:", use_aliases=True)+" "+str(yweather.Forecast[0]['low'])+" �C"+emojize(" :arrow_down:", use_aliases=True)+
                                                  "\nSonnenaufgang: "+str(yweather.Astronomy['sunrise'])+emojize(" :arrow_heading_up:", use_aliases=True)+
                                                  "\nSonnenuntergang: "+str(yweather.Astronomy['sunset'])+emojize(" :arrow_heading_down:", use_aliases=True)) #schickt aktuelle Wetterdaten
        print("und zu "+gotten_chat.first_name+" geschickt\n")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Konnte yahoo-Wetterdaten nicht empfangen!") #Fehlermeldung
        print("und konnten nicht zu "+gotten_chat.first_name+" geschickt werden\n") #Statusmeldung: Fehler bei Wetterdaten


#react to all non-commands
def react(bot, update): #definiert Methode zu allen anderen messages
    bot.send_message(chat_id=update.message.chat_id, text=  ("Hallo User, ich habe Dich leider nicht verstanden!\nTippe /help um mehr zu erfahren!")) #sendet dem user das Kontextmen�