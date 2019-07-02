# -*- coding: utf-8 -*-

import os

from telegram import CommandHandler, MessageHandler

from doerffelbot.functions import start, helpme, links, vertretung
from doerffelbot.auto_message import daily_message


def get_credentials():
    """
    Get credentials from credentials file or environ variables.

    Returns:
    string: TOKEN
    dict: VPLAN {"user", "pass"}
    """
    try:
        import CONFIG as conf
        TOKEN = conf.TOKEN
        VPLAN = {
            "user": conf.vplan["username"],
            "pass": conf.vplan["passwort"]
        }
    except ImportError:
        TOKEN = os.environ.get('TOKEN', default=None)
        VPLAN = {
            "user": os.environ.get('VPLAN_USER', default=None),
            "pass": os.environ.get('VPLAN_PASS', default=None)
        }

        if None in [TOKEN, VPLAN["user"], VPLAN["pass"]]:
            assert ImportError

    return TOKEN, VPLAN


def setup(updater, dispatcher):

    register_commands(dispatcher)
    register_jobq(updater)


def register_commands(disp):

    command_list = [('start', start), ('help', helpme), ('links', links), ('vertretung', vertretung)]

    for name, func in command_list:
        register_command(disp, name, func)

    handler = MessageHandler(Filters.text, react)
    disp.add_handler(handler)


def register_command(dispatcher, name, func):

    handler = CommandHandler(name, func)
    dispatcher.add_handler(handler)


def register_jobq(updater):

    updater.jobq.run_daily(
        callback=daily_message,
        time=datetime.time(hour=18, minute=0)
    )

