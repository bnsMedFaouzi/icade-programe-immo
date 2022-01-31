#!/bin/bash

set -e

echo -e "Running $DJANGO_ENV Env\n*****************\n"

if [[ $DJANGO_ENV = "prod" ]]; then
  echo -e "Starting development server\n***********\n"
  exec python3 src/manage.py runserver 0.0.0.0:5000
else
  echo -e "Invalid config $DJANGO_ENV"
fi
