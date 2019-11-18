FROM python:3

RUN pip3 install redis flask

COPY echo-server.py /
COPY logging.cfg /

EXPOSE 65432
ENTRYPOINT ["python", "echo-server.py"]
