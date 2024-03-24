#!/bin/sh

# Migrations de la base de données
python manage.py makemigrations
python manage.py migrate --noinput

# Remplir la base de données
python manage.py init_vigicrue
python manage.py init_stations
python manage.py init_reperes_crues

# Mise à jour de données si nécessaire
python manage.py update_station

# Lancez le serveur Django
exec "$@"
