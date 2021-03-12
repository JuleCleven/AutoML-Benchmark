FROM python:3.6.1-alpineapk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /clv/AutoML-Benchmark/app/static
COPY ./requirements.txt /clv/AutoML-Benchmark/requirements.txt
RUN pip install -r /clv/AutoML-Benchmark/requirements.txt




