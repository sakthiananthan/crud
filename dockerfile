FROM python:3-slim-buster
COPY . /python-flask
WORKDIR /python-flask
RUN pip install flask
ENTRYPOINT ["python","main.py"]
