APP_NAME=byterun
VENV=venv

setup:
	uv venv $(VENV)
	uv pip install -r  requirements.txt
build:
	sudo docker build -t $(APP_NAME) .
run:
	sudo docker run --rm $(APP_NAME)
test:
	pytest -v
	
test-docker:
	sudo docker run --rm $(APP_NAME) pytest -v

clean:
	rm -rf build/ dist/ *.egg-info __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

