FROM ubuntu:16.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip build-essential libssl-dev libffi-dev python3-dev python3-setuptools python3
RUN apt-get install -y nginx supervisor
RUN apt-get install -y tzdata
RUN pip3 install --upgrade pip
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./website /home/docker/website

RUN pip3 install uwsgi
RUN pip3 install -r /home/docker/website/requirements.txt


RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisor.conf /etc/supervisor/conf.d/

EXPOSE 443
CMD ["supervisord", "-n"]
