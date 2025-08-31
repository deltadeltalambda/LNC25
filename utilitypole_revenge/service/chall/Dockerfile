FROM python:3.11-slim-buster
WORKDIR /app

RUN useradd -m chall
RUN apt update
RUN apt install -y socat

COPY src.py .
COPY flag.txt .
COPY answer.json .

RUN chmod +r src.py
RUN chmod +r flag.txt
RUN chmod +r answer.json

USER chall

ENTRYPOINT socat tcp-l:5001,fork,reuseaddr exec:"python src.py"

# docker build -t chall . 
# docker run -p 5001:5001 chall:latest        