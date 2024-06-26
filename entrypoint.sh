#!/bin/sh

# Migrations de la base de données
echo "Création BDD"
python manage.py makemigrations
python manage.py migrate --noinput

echo "Collecte des fichiers statiques"
python manage.py collectstatic --noinput

# Remplir la base de données
python manage.py init_vigicrue
python manage.py init_station
python manage.py init_reperes_crues

# Mise à jour de données si nécessaire
python manage.py update_station

# Démarrer le service cron en arrière-plan
cron -f &

# Lancez le serveur Django
exec "$@"
