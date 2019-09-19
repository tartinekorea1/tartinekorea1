FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt --upgrade
ADD . /app/

ENTRYPOINT [ "python" ]
CMD ["application.py"]
