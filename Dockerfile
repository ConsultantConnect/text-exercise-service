FROM python:3.7.2-slim-stretch
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY /api .
ENTRYPOINT ["python"]
CMD ["app.py"]
