FROM python:3.9-alpine
COPY ./app /app
CMD ["/app/main.py"]
ENTRYPOINT ["python"]
