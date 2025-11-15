FROM python:3.11.13-slim

WORKDIR /app

COPY pyproject.toml .

# Copy the package
RUN pip install -e ".[dev]"
COPY byterun/ ./byterun
COPY test/  ./test
# Install the package


# Run the application
CMD ["python", "-m", "byterun.main"]
