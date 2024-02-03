FROM python:3.9-alpine

WORKDIR /docker

COPY ./ /docker

RUN apk update && pip3 install -r /docker/requirements.txt

EXPOSE 8000

CMD ["python3",  "manage.py", "runserver", "0.0.0.0:8000"]