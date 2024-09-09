FROM python:3.12-slim-bullseye As builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# stage 2
FROM python:3.12-slim-bullseye

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

ENV PYTHONUNBUFFERED=1 

COPY . .

EXPOSE 5000

CMD [ "python3", "./app.py" ]