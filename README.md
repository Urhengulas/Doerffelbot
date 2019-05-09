# Doerffelbot

**Table of Content**
- [About](#about)
- [Getting started](#getting-started)
  - [CONFIG.py](#configpy)
  - [virtualenv](#virtualenv)
  - [going online](#going-online)

## About
A telegram-bot to access the substitution plan of the Georg-Samuel-Dörffel-Gymnasium in Weida, Thuringia, Germany.

## Getting started

### CONFIG.py
First you have to create a `CONFIG.py` file, which contains the credentials of the bot and the substitution plan.  
This can be done by calling `make setup`:

```shell
$ make setup
```

It will create a file `init_CONFIG.py`,  
which looks like:

```python
TOKEN = "xxxxxxxxxx"
my_chat_id = 123456789
vplan = {"username": "xxxxx", "password": "xxxxx"}
```

After filling in your data you can rename it to `CONFIG.py`.

`make setup` also creates a new directory `data/` and inide two files `ids.set` and `vertretung.pdf`.

### virtualenv
Next you have to install the required python packages:
```shell
$ make dep
```
### going online
Finally you can send the bot online:
```shell
$ make run
```
