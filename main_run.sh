#!/bin/bash

until mysqladmin ping -h db --silent; do
  echo 'waiting for mysqld to be connectable...'
  sleep 2
done

echo " go app is started!"
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port 5000