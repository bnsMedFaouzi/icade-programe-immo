#!/bin/bash

set -e

echo -e "Running $DJANGO_ENV Env\n*****************\n"

if [[ $DJANGO_ENV = "development" ]]; then
  echo -e "Starting development server\n***********\n"
  exec python3 src/manage.py runserver 0.0.0.0:5000
elif [[ $DJANGO_ENV = "testing" ]]; then
  echo -e "Running tests\n************\n"
  exec cd src && pytest
else
  echo -e "Invalid config $DJANGO_ENV"
fi
