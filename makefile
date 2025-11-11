APP_NAME=byterun
VENV=venv

setup:
	uv venv $(VENV)
	uv pip install -r  requirements.txt
build:
	sudo docker build -t $(APP_NAME) .
run:
	sudo docker run --rm $(APP_NAME)

