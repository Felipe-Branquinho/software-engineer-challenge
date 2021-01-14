FROM python:3.6

EXPOSE 3000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD python ./src/app.py