APP_NAME=byterun
VENV=venv

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r  requirements.txt
build:
	sudo docker build -t $(APP_NAME) .
run:
	sudo docker run --rm $(APP_NAME)

