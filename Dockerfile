
FROM python:3.10.14-slim-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py main.py
COPY models.py models.py

CMD [ "python3", "-m" , "main"]
