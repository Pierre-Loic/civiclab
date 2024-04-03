FROM python:3.11-slim

# Définir des variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer cron
RUN apt-get update && apt-get install -y cron

# Copier le fichier crontab dans le conteneur
COPY django-cronjobs /etc/cron.d/django-cronjobs

# Donner les permissions nécessaires et créer le fichier de log
RUN chmod 0644 /etc/cron.d/django-cronjobs \
    && touch /var/log/cron.log

# Appliquer le fichier crontab
RUN crontab /etc/cron.d/django-cronjobs


# Mettre à jour pip
RUN pip install --upgrade pip

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application dans le conteneur
COPY . /app
RUN ls -la /app

# Copier et accorder les permissions d'exécution au script d'entrée
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Définir le script d'entrée comme point d'entrée
ENTRYPOINT ["/entrypoint.sh"]

# Exposer le port sur lequel votre application sera accessible
EXPOSE 8000

# Commande par défaut pour exécuter l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "crue.wsgi:application"]