# - if 'Got permission denied'
# sudo usermod -a -G docker [user]
# newgrp docker
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # mysql dependencies
  && apt-get install -y default-libmysqlclient-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt ./requirements.txt 
RUN pip install -r ./requirements.txt 

ADD . /app/

EXPOSE 80


# ENV PORT=8000
# CMD gunicorn scrap_chatbot_django.wsgi:application --bind 0.0.0.0:$PORT
# CMD [ "uwsgi", "--http", ":80", "--module", "config.wsgi" ]
CMD python manage.py runserver 0.0.0.0:80



