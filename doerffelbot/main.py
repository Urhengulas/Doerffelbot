# -*- coding: utf-8 -*-

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filter

from utilities import get_credentials, setup


def main():

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    TOKEN, _ = get_credentials()

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    setup(updater, dispatcher)

    updater.start_polling()
    logging.info("Dörffelbot started polling")
    updater.idle()


if __name__ == '__main__':
    main()

