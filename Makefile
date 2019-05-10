run:
	env/bin/python -m doerffelbot.main

dep:
	# check if virtualenv `env` exists
	if [ ! -d "env" ];then virtualenv env;fi

	# install modules from `requirements.txt
	env/bin/pip install -r requirements.txt

setup:
	# data dir
	if [ ! -d "data" ];then mkdir data;fi
	touch data/ids.set
	touch data/vertretung.pdf

	# CONFIG.py
	touch init_CONFIG.py
	echo 'TOKEN = "xxxxx"' >> init_CONFIG.py
	echo 'my_chat_id = 123456789' >> init_CONFIG.py
	echo 'vplan = {"username": "xxxxx", "password": "xxxxx"}' >> init_CONFIG.py