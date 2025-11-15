APP_NAME=byterun
VENV=venv

setup:
	echo "Creating virtual environment"
	uv venv $(VENV)
	. $(VENV)/bin/activate
	uv pip install -r  requirements.txt
	echo "Setup Completed"
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
help:
	@echo "ByteRun - Available Commands"
	@echo ""
	@echo "LOCAL DEVELOPMENT (Virtual Environment):"
	@echo "  make setup       - Create venv and install package"
	@echo "  make run         - Run application locally"
	@echo "  make test        - Run tests locally"
	@echo ""
	@echo "DOCKER (Production-like):"
	@echo "  make build       - Build Docker image"
	@echo "  make run-docker  - Run application in Docker"
	@echo "  make test-docker - Run tests in Docker"
	@echo ""
	@echo "UTILITIES:"
	@echo "  make clean       - Remove build artifacts"
	@echo "  make clean-all   - Remove venv and Docker image"
	@echo "  make help        - Show this help"

