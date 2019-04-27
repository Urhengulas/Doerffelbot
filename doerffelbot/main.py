# -*- coding: utf-8 -*-

import datetime
import logging
from . import functions as func
from . import auto_message as zet
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import CONFIG as conf


TOKEN = conf.TOKEN  # Token of @doerffelbot
old_TOKEN = conf.old_TOKEN  # Token of @johannstodobot
my_chat_id = conf.my_chat_id  # my own telegram-'chat id'

# init updater: handle incoming messages
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# configure error message logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# register all commands of the bot

start_handler = CommandHandler('start', func.start)
dispatcher.add_handler(start_handler)


help_handler = CommandHandler('help', func.helpme)
dispatcher.add_handler(help_handler)


link_handler = CommandHandler('links', func.links)
dispatcher.add_handler(link_handler)


vertretung_handler = CommandHandler('vertretung', func.vertretung)
dispatcher.add_handler(vertretung_handler)


wetter_handler = CommandHandler('wetter', func.wetter)
dispatcher.add_handler(wetter_handler)


echo_handler = MessageHandler(Filters.text, func.react)
dispatcher.add_handler(echo_handler)


# init job queue: handles all schedules actions
jobq = updater.job_queue

# register daily substitution plan
job_daily = jobq.run_daily(callback=zet.daily_message,
                           time=datetime.time(hour=10, minute=35))


def main():
    
    updater.start_polling()  # bots goes online
    print("Dörffelbot started polling")


if __name__ == '__main__':
    main()
