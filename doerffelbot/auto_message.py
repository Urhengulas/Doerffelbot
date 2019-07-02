# -*- coding: utf-8 -*-

import logging
import pickle

from doerffelbot.functions import download_vertretung


def daily_message(bot, job):

    logging.info("Zeitsteuerung gestartet")

    with open("data/ids.set", 'rb') as doc:
        ids = pickle.load(doc)

    download_vertretung()
    
    with open("data/vertretung.pdf", "rb") as doc:
        for chat in ids:
            try:
                bot.send_message(
                    chat_id=chat, 
                    text="Hier ist dein täglicher Vertretungsplan:")
                bot.sendDocument(
                    chat_id=chat, 
                    document=doc)

                logging.info(f"Vertretungsplan zu {chat} geschickt")
        except:
            logging.error(f"Konnte Vertretungsplan nicht zu {chat} senden.")

