FROM python:3.11-slim-buster
WORKDIR /app

RUN useradd -m chall
RUN pip install numpy
RUN pip install scikit-network
RUN apt update
RUN apt install -y socat

COPY src.py .
COPY flag.txt .
COPY webpages.txt .

RUN chmod +r src.py
RUN chmod +r flag.txt
RUN chmod +r webpages.txt

USER chall

ENTRYPOINT socat tcp-l:5000,fork,reuseaddr exec:"python src.py"

# docker build -t chall . 
# docker run -p 5000:5000 chall:latest        


