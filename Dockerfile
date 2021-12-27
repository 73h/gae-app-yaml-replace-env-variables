FROM python:3.9-alpine
COPY ./app /app
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /config/python/requirements.txt
CMD ["/app/main.py"]
ENTRYPOINT ["python"]
