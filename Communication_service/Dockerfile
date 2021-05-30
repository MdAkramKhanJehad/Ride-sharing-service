FROM python:3.9-slim

RUN mkdir /Communication_service
WORKDIR /Communication_service

ADD requirements.txt /Communication_service/requirements.txt
RUN pip install -r /Communication_service/requirements.txt

ADD . /Communication_service

EXPOSE 6000

CMD ["python3","-u","/Communication_service/communication.py"]