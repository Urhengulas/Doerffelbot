# Doerffelbot

**Table of Content**
- [About](#about)
- [Getting started](#getting-started)

## About
A telegram-bot to access the substitution plan of the Georg-Samuel-Dörffel-Gymnasium in Weida, Thuringia, Germany.

## Getting started

First you have to create a `CONFIG.py` file, which contains the credentials of the bot and the substitution plan.
```python
TOKEN = "xxxxxxxxxx"
my_chat_id = 123456789
vplan = {"username": "xxxxx", "password": "xxxxx"}
```
Next you have to install the required python packages:
```shell
$ make dep
$ source env/bin/activate
```

Finally you can send the bot online:
```shell
$ make run
```
