FROM python:3.12

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y --no-install-recommends \
    speedtest-cli \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

CMD ["python", "main.py"]