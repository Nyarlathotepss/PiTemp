# Bienvenue sur le projet Pi-Temp!

L'objectif de ce projet est de permettre à un raspberry pi 3 d'envoyer des informations de températures à un site Django. 
Le site aura pour objectif d'afficher les différentes informations en fonction de l'utilisateur.

# Les dépots

Pour ce projet nous utiliserons 2 dépots Git :

Le premier concernera le site web et sera donc dédié plutôt pour les administrateurs du site.
https://github.com/Nyarlathotepss/PiTemp.git 

Le deuxième se concentrera sur la partie Raspberry et sera donc utilisé par tous les utilisateurs du projet
https://github.com/Nyarlathotepss/Pi-Temp_Raspberry

# Le site Django
Le projet Django est composé de 3 briques applicatives.
Website, Api et Authenticate

Website : La partie dedié au site web
Authenticate : Concerne tout ceux qui touche à l'authentification des utilisateurs
Api : Permet la communication entre 1 Raspberry et le Site. Utilisation de "rest framework" (https://www.django-rest-framework.org/)

## Procédure utilisateur
Se référer au github lié au Raspberry