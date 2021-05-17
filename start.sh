#!/bin/bash
app="container"
docker build -t local/${app}:latest .
docker run -d -p 56743:80 \
  --name=${app} \
  -v $PWD:/app local/${app}
