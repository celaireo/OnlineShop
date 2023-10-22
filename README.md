# Projet de Boutique en ligne avec Django

Notre projet consiste à mettre en place une API avec Django Rest Framework pour une boutique en ligne.  
Cet API permet à des utilisateurs de consulter un catalogue de produits rangé par catégories, produits et articles. 
Seuls les administrateurs auront la possibilité après authentification, d’ajouter, de modifier ou de supprimer ces informations après consultation. 


## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Si ce n'est pas le cas, téléchargez-le à partir de [Python's Official Website](https://www.python.org/downloads/).


2. Clonez ce dépôt sur votre machine :

- git clone https://github.com/celaireo/OnlineShop.git

3. Accédez au répertoire du projet :
- cd OnlineShop


4. Installez les dépendances requises à partir du fichier `requirements.txt` :
- pip install --upgrade setuptools
- pip install -r requirements.txt


5. Effectuez les migrations de la base de données pour créer les tables nécessaires :
- python manage.py migrate


6. Lancez le serveur de développement :
- python manage.py init_local_dev
- python manage.py runserver

L'application est désormais accessible à l'adresse `http://127.0.0.1:8000/api/`.

## Utilisation de l'API

* Si vous êtes utilisateurs, vous pouvez accéder à ces endpoints via des requêtes HTTP GET pour consulter les données.- `/api/category/` : Liste de toutes les catégories de produits.
  - `/api/product/` : Liste de tous les produits.
  - `/api/article/` : Liste de tous les articles.

* Si vous êtes administrateur, vous pouvez accéder à ces endpoints via des requêtes Http GET, POST, PATCH et DELETE.
  - `/api/admin/category/` : Pour les opérations CRUD sur les catégories de produits.
  - `/api/admin/product/` : Pour les opérations CRUD sur produits.
  - `/api/admin/article/` : Pour les opérations CRUD sur les articles.

## Documentation Swagger

La documentation Swagger de l'API est accessible à l'adresse `http://127.0.0.1:8000/swagger/`. Vous y trouverez des informations détaillées sur les points d'accès de l'API, des exemples de requêtes, et la possibilité d'essayer l'API directement depuis la documentation.

## Interface d'administration

L'interface d'administration Django est accessible à l'adresse `http://127.0.0.1:8000/admin/`. Connectez-vous en utilisant les informations du superutilisateur que vous avez créé précédemment pour gérer les données de la boutique.

## Contribuer

Si vous souhaitez contribuer à ce projet, n'hésitez pas à créer une demande d'extraction (pull request) ou à signaler des problèmes (issues) sur le dépôt GitHub.

## la valeur des username et password
- Username : admin-oc
- Password : password-oc 

