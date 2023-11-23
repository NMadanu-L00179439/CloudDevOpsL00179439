# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install app
COPY . .

# final configuration
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#ENV FLASK_APP=app
#EXPOSE 8000
#CMD flask run --host 0.0.0.0 --port 8000