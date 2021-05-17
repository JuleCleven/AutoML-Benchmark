FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ENV NGINX_WORKER_PROCESSES auto
ENV NGINX_WORKER_CONNECTIONS 1024
ENV NGINX_WORKER_OPEN_FILES 1024
ENV UWSGI_CHEAPER 50
ENV UWSGI_PROCESSES 51
RUN apk --update add bash nano build-base
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
RUN apk del build-base
