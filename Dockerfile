FROM python:3.11.13-slim

WORKDIR /app
COPY  requirements.txt .
RUN  pip install -r requirements.txt
COPY . .
EXPOSE 7000
CMD ["python", "./src/main.py"]