# Application de location de voitures en ligne

Cette application est une application de location de voitures en ligne complète utilisant Django et Bootstrap3. L'application permet aux utilisateurs de créer des comptes, de réserver des voitures et de rechercher des voitures.

## Fonctionnalités

L'application comprend les fonctionnalités suivantes :

- Gestion des comptes utilisateurs (créer un utilisateur, se connecter, se déconnecter)
- Gestion des réservations de voitures (créer et annuler des réservations de voitures)
- Barre de recherche (outil de recherche de voitures)
- Protection par mot de passe utilisant le hashage.

## Installation

Voici un bref guide pour commencer à utiliser le logiciel :

1. Clonez le repo ou téléchargez le fichier zip.
2. Ouvrez le dossier avec un éditeur de code.
3. Créez un environnement virtuel.
4. Installez toutes les bibliothèques 
5. Effectuez les migrations avec les commandes `python manage.py makemigrations` et `python manage.py migrate`.
6. Lancez le serveur avec la commande `python manage.py runserver`. Le serveur doit fonctionner sur http://127.0.0.1:8000/.
7. Créez un superutilisateur avec la commande `python manage.py createsuperuser`.
8. Ouvrez le panneau d'administration sur http://127.0.0.1:8000/admin.
9. Créez de nouvelles voitures que vous souhaitez louer.
10. Commencez à utiliser l'application !

## Bibliothéques

1. argon2-cffi==21.3.0
2. argon2-cffi-bindings==21.2.0
3. asgiref==3.5.0
4. bcrypt==3.2.0
5. cffi==1.15.0
6. Django==4.0.3
7. django-bootstrap3==21.2
8. dojango==0.5.8
9. pycparser==2.21
10. six==1.16.0
11. sqlparse==0.4.2
12. tzdata==2021.5





## Auteurs

- nouhaila MAKOUDI
- abderrahmane CHARAK
- Mohamed Ayman YAKHMIM
- Anass CHARKAOUI
