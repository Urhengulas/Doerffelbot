# -*- coding: utf-8 -*-

import requests
import pickle

from utilities import get_credentials


def start(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)
    first_name = gotten_chat.first_name
    chat_id = gotten_chat.id

    bot.send_message(chat_id=update.message.chat_id, text=("Hello "+gotten_chat.first_name+"!\nMy name is Doerffelbot.\n" +
                                                           "I'm a student project of two awesome German students " +
                                                           "of the Georg-Samuel-Dörffel-Gymnasium in Weida.\n\n" +
                                                           "At the moment I only react to /help, /links and /vertretung, " +
                                                           "but if we have some more ideas which seem usefull to us, we will implement them!\n" +
                                                           "\nPS: If you have any inspirations, please send them to Joheihe@web.de"))

    logging.info(f"{first_name} hat den bot gestartet (chat_id: {chat_id})")

    with open("data/ids.set", 'rwb') as doc:
        ids = pickle.load(doc)
        ids.add(gotten_chat.id)
        pickle.dump(ids, doc)

    logging.info("{first_name} was added to chat_id-list\nids={ids}")


def helpme(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)
    first_name = gotten_chat.first_name

    bot.send_message(
            chat_id=update.message.chat_id, 
            text=("Momentan reagiere ich nur auf die Befehle: /start, /help, /links und /vertretung.\nSollten wir aber noch weitere Ideen haben, implementieren wir diese natuerlich! Viel Spasz!"))
    
    logging.info(f"{first_name} asked for help")


def links(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)
    first_name = gotten_chat.first_name

    bot.send_message(chat_id=update.message.chat_id, text=("Hier sind ein paar interessante Links:\n" +
                                                           " - Homepage: http://www.doerffelgymnasium.de/cms/\n" +
                                                           " - News: http://www.doerffelgymnasium.de/cms/index.php/news\n" +
                                                           " - Schulspeisung: https://www.wakos-gera.de/bestellen/schulspeisung"))

    logging.info(f"{first_name} request links")


def download_vertretung():

    _, VPLAN = get_credentials()

    url = "https://doerffelgymnasium.de/vplan/Vertretung.pdf"

    r = requests.get(
            url, 
            auth=(
                VPLAN["user"], 
                VPLAN["pass"]), 
            stream=True)

    with open("data/vertretung.pdf", 'wb') as doc:
        for chunk in r.iter_content(chunk_size=128):
            doc.write(chunk)

        logging.info(f"{doc.name} was downloaded and written to disk")


def vertretung(bot, update):

    gotten_chat = bot.get_chat(chat_id=update.message.chat.id)
    user_name = gotten_chat.first_name
    chat_id = update.message.chat_id

    download_vertretung()

    with open("data/vertretung.pdf", "rb") as doc:
        bot.sendDocument(
                chat_id=chat_id,
                document=doc)
    
        logging.info(f"Send {doc.name} to {first_name}")


def react(bot, update):

    chat_id = update.message.chat_id

    bot.send_message(
            chat_id=chat_id,
            text="Hallo User, ich habe Dich leider nicht verstanden!\nTippe /help um mehr zu erfahren!")

