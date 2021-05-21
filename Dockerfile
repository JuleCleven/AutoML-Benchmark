FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano build-base
ENV STATIC_URL /app/static
ENV STATIC_PATH /var/www/app/AutoML-Benchmark/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
RUN apk del build-base

