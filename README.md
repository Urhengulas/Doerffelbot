# Doerffelbot

**Table of Content**
- [About](#about)
- [Getting started: fast](#getting-started-fast)
- [Getting started: full](#getting-started-full)
  - [CONFIG.py](#configpy)
  - [virtualenv](#virtualenv)
  - [going online](#going-online)

## About
A telegram-bot to access the substitution plan of the Georg-Samuel-Dörffel-Gymnasium in Weida, Thuringia, Germany.  
The grammar school is certified with the MINT-Dings.

## Getting started: fast
The fasted way to get started is possible by cloning a public gist and pulling the latest image from docker-hub:

```shell
$ git clone git@gist.github.com:f48e23a765f094c3c399c6b6c1e9425f.git
$ cd f48e23a765f094c3c399c6b6c1e9425f/
$ make all
```
It runs for a moment and then it will open `init_CONFIG.py` in `vi`. You now have to fill in the credentials and exit with `:x`.

It finishes with something like:

```
docker run --rm -v "/root/to/Doerffelbot-minimal/data:/app/data" -v "/root/to/Doerffelbot-minimal/CONFIG.py:/app/CONFIG.py" urhengulas/doerffelbot
```

## Getting started: full

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

You need to fill in the actual credentials to use the bot.  
After doing that you can rename it to `CONFIG.py`.

`make setup` also creates a new directory `data/` and inside two files `ids.set` and `vertretung.pdf`.

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
