#!/bin/bash

set -e

echo -e "Running $DJANGO_ENV Env\n*****************\n"


if [[ $DJANGO_ENV = "development" ]]; then
  if [[ $DJANGO_RUN_MIGRATION = "on" ]]; then
    echo -e "Wait for database to start : Waiting \n"
    exec sleep 10 &
    wait $!
    echo -e "Run migrations : Start \n"
    echo -e "Default database migrations : Start \n"
    exec python3 src/manage.py migrate &
    wait $!
    echo -e "Default database migrations : End \n"
    wait $!

    #exit 0
  fi
  echo -e "Create superuser admin \n***********\n"
  exec python src/manage.py create_admin  -u admin -e admin@admin.com -w admin -f admin -l admin &
  wait $!
  echo -e "Starting development server\n***********\n"
   exec python3 src/manage.py runserver 0.0.0.0:5000
elif [[ $DJANGO_ENV = "test" ]]; then
  echo -e "Running tests\n************\n"
  exec pytest -c ./src/pytest.ini
else
  echo -e "Invalid config $DJANGO_ENV"
fi
