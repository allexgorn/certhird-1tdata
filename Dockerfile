FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./data.csv /app/data.csv

COPY ./app.py /app/app.py

CMD ["python3", "app.py"]

