FROM python:3.9-buster

LABEL maintainer="Heiko Schmidt <heiko@73h.de>"

COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app/main.py"]
