#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e


#while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
#  sleep 3
#done

#echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py runserver 0.0.0.0:8000