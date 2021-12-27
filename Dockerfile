FROM python:3.9-alpine
COPY ./app /app
WORKDIR app
CMD [ "python", "main.py"]
