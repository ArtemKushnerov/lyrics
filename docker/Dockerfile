FROM python:3.6

COPY . /lyrics

WORKDIR /lyrics

RUN pip install -r requirements.txt

CMD ["flask", "run"]
