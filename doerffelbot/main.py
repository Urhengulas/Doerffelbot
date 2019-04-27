# -*- coding: utf-8 -*-

import datetime
import logging
import functions as func
import auto_message as zet
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser


configParser = configparser.ConfigParser()
configParser.read('important.log')
config = configParser['DEFAULT']

TOKEN = config['TOKEN'] #Token von @doerffelbot
old_TOKEN = config['old_TOKEN'] #Token von @johannstodobot
my_chat_id = config['my-chat-id'] #my own telegram-'chat id'

updater = Updater(token=TOKEN) #erstellt den updater --> verarbeitet neue Nachrichten
dispatcher = updater.dispatcher #erstellt dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO) #logging ist f�r Fehlermeldungen


#fügt die Reaktion auf den Befehl "/start" hinzu
start_handler = CommandHandler('start', func.start) #weist dem Befehl /start die Methode start zu
dispatcher.add_handler(start_handler) #f�gt diesen Handler hinzu


#fügt die Reaktion auf den Befehl "/help" hinzu
help_handler = CommandHandler('help', func.helpme) #weist dem Befehl /help die methode help zu
dispatcher.add_handler(help_handler) #fügt diesen Handler hinzu


#f�gt die Reaktion auf den Befehl "/links" hinzu
link_handler = CommandHandler('links', func.links) #weist dem Befehl /links die methode links zu
dispatcher.add_handler(link_handler) #f�gt diesen Handler hinzu


#f�gt die Reaktion auf den Befehl "/vertretung" hinzu
vertretung_handler = CommandHandler('vertretung', func.vertretung) #wei�t dem befehl /vertretung die methode vertretung zu
dispatcher.add_handler(vertretung_handler) #f�gt diesen Handler hinzu


#f�gt die Reaktion auf den Befehl "/wetter" hinzu
wetter_handler = CommandHandler('wetter', func.wetter) #weist dem Befehl /wetter die methode wetter zu
dispatcher.add_handler(wetter_handler) #f�gt diesen Handler hinzu


#react to all non-commands
echo_handler = MessageHandler(Filters.text, func.react) #weist allen Texten die Methode vertretung zu
dispatcher.add_handler(echo_handler) #f�gt diesen Handler hinzu


#Zeitsteuerung
jobq = updater.job_queue #erstellt die job_queue --> alle geplant ablaufenden Arbeitsschritte

job_daily = jobq.run_daily(callback=zet.daily_message,
                           time=datetime.time(hour=10,minute=35)) #t�gliches senden um hour:minute Uhr

##########################################################################################################

def main():
    updater.start_polling() #der Bot f�ngt an zu 'lauschen'
    print("Dörffelbot started polling") #gibt R�ckmeldung

if __name__=='__main__':
    main()

##########################################################################################################