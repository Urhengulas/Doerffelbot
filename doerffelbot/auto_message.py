# -*- coding: utf-8 -*-

import pickle
from . import functions as func


#Zeitsteuerung
def daily_message(bot, job):
    with open("../ids.set", 'rb') as doc:
        ids = pickle.load(doc) #lädt die chat_id-Menge
    
    print("Zeitsteuerung gestartet\n")
    
    func.download_vertretung()
    
    for chat in ids:
        try:
            bot.send_message(chat_id=chat, text="Hier ist dein täglicher Vertretungsplan:")
            bot.sendDocument(chat_id=chat, document=open("Vertretung.pdf", 'rb')) #sendet dem user den Vertretungsplan, Bezug durch selbst-downloaden
            print("Vertretungsplan zu "+str(chat)+" geschickt\n")
        except:
            print("Konnte Vertretungsplan nicht zu"+str(chat)+"senden.")