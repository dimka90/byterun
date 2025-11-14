FROM python:3.11.13-slim

WORKDIR /app

COPY pyproject.toml .

# Copy the package
COPY byterun/ ./byterun/

# Install the package
RUN pip install -e ".[dev]"

# Run the application
CMD ["python", "-m", "byterun.main"]
