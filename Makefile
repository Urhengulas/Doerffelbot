dep:
	# check if virtualenv `env` exists
	if [ ! -d "env" ];then virtualenv env;fi

	# install modules from `requirements.txt
	env/bin/pip install -r requirements.txt