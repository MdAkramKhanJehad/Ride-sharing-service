FROM python:3.9-slim

RUN mkdir /Rating_service
WORKDIR /Rating_service

ADD requirements.txt /Rating_service/requirements.txt
RUN pip install -r /Rating_service/requirements.txt

ADD . /Rating_service

#EXPOSE 7000

CMD ["python3","-u","/Rating_service/rating.py"]
