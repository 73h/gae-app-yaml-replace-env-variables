FROM python:3.9-buster
COPY ./app /app
CMD [ "python", "/app/main.py"]
