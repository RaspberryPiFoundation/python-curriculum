---
title: Messages Secrets — Notes du volontaire
---

# Introduction :
Dans ce projet, les enfants vont apprendre comment créer ton propre programme de chiffrement, pour pouvoir envoyer et recevoir des messages secrets avec un ami. Ce projet présente le concept d'itération (boucle) via une chaîne de charactères.

# Ressources en ligne

__Ce projet utilise Python 3.__ Nous vous conseillons d'utiliser [trinket](https://trinket.io/) pour écrire du Python en ligne. Ce projet contient les Trinkets suivants :

+ [nouveau Trinket Python (vierge) -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Il y a également un trinket qui contient une version finalisée du projet :

+ [‘Messages Secrets’ finalisé -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [‘Calculatrice d'amitié’ finalisé -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

# Ressources hors-ligne
Ce projet pourrait être [complété hors-ligne](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) si préférable.

Vous pouvez trouver une version finalisée du projet dans la section 'Ressources du volontaire', qui contient :

+ messages-finished/messages.py
+ messages-finished/friends.py

(Toutes les ressources ci-dessus sont également téléchargeables comme des fichiers `.zip` pour le projet et les volontaires.)

# Objectifs pédagogiques
+ Itération (exécuter en boucle) pour une chaîne de caractères ;
+ La méthode `find()` ;
+ Modulo (opération) (`%`).

Ce projet couvre des élements des parcours suivants du [Programme de Créativité Numérique Raspberry Pi](http://rpf.io/curriculum) :

+ [Combiner des structures de programmation afin de résoudre des problèmes.](https://www.raspberrypi.org/curriculum/programming/builder)

# Défis
+ Utilisation du Code de Caesar (Chiffrement par décalage) - pour chiffrer et déchiffrer des lettres et mots manuellement ;
+ Clés variables - permettre à l'utilisateur d'entrer une clé choisie ;
+ Chiffrer et déchiffrer des messages - Cryptage et décryptage de messages entiers ;
+ Calulatrice d'amitié - application d'itération d'un texte à une autre problèmatique.

# Foire à questions
+ Quand on cherche avec la fonction `find()` ou `if char in alphabet:`, à noter que les requêtes sont sensible à la casse. Les enfants peuvent utiliser :

	```python
	message = input("Please enter a message to encrypt: ").lower()
	```

	pour transfomer l'entrée en miniscule avant de lancer la recherche.
