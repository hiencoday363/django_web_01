# - if 'Got permission denied'
# sudo usermod -a -G docker [user]
# newgrp docker

# build
# docker build -t [name] .

# - remove image
# docker rmi -f [id image]

# list container
# docker ps

# start container
# docker run -p [host port]:[container port] [name image]

# - stop container docker 
# docker container stop [name container]

# - remove container
# docker rm [name container]

# - push heroku
# docker tag [image_name] registry.heroku.com/[app_name]/[type: web]
# docker push registry.heroku.com/[app_name]/[type: web]



# Base Image 

FROM python:3

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
# ENV PYTHONUNBUFFERED 1
# ENV LANG C.UTF-8
# ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# install Microsoft SQL Server requirements.

RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev


# Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#         tzdata \
#         python3-setuptools \
#         python3-pip \
#         python3-dev \
#         python3-venv \
#         git \
#         && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*


# install environment dependencies
# RUN pip3 install --upgrade pip 
# RUN pip3 install pipenv

# Install project dependencies
RUN pip install -r requirements.txt

EXPOSE 8888
CMD gunicorn scrap_chatbot_django.wsgi:application --bind 0.0.0.0:$PORT

