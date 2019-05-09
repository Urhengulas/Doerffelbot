# -*- coding: utf-8 -*-

import pickle
from . import functions as func


# time control
def daily_message(bot, job):

    with open("data/ids.set", 'rb') as doc:
        ids = pickle.load(doc)

    print("Zeitsteuerung gestartet\n")

    func.download_vertretung()

    for chat in ids:
        try:
            bot.send_message(
                chat_id=chat, text="Hier ist dein täglicher Vertretungsplan:")
            bot.sendDocument(chat_id=chat, document=open(
                "data/vertretung.pdf", 'rb'))
            print("Vertretungsplan zu "+str(chat)+" geschickt\n")
        except:
            print("Konnte Vertretungsplan nicht zu"+str(chat)+"senden.")
