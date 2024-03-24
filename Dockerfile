FROM python:3.11-slim

# Définir des variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer les paquets nécessaires pour pipenv
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip \
    && pip install pipenv

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier Pipfile et Pipfile.lock dans le conteneur
COPY Pipfile Pipfile.lock /app/

# Installer les dépendances du projet en utilisant pipenv
# Le drapeau --system installe les paquets dans le système plutôt que dans un environnement virtuel
# Le drapeau --deploy échouera si le Pipfile.lock est obsolète
RUN pipenv install --system --deploy

# Copier le reste du code source de l'application dans le conteneur
COPY . /app

# Copier et accorder les permissions d'exécution au script d'entrée
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Définir le script d'entrée comme point d'entrée
ENTRYPOINT ["/entrypoint.sh"]

# Commande par défaut pour exécuter l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "crue.wsgi:application"]
