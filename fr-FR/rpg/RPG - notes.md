---
title: Jeu de rôle — Notes du volontaire
---

# Introduction :
Ce projet apprend comment dessiner un jeu à travers le développement d'un jeu de rôle et de labyrinthe. Dans ce jeu, je joueur doit ramasser des objets dans une maison et se retrouve dans une pièce en particulier, tout en évitant les monstres qui traînent dans certaines des pièces. Ce jeu sera réalisé grâce à la manipulation de dictionnaires et de listes.

# Ressources en ligne

__Ce projet utilise Python 3.__ Nous vous conseillons d'utiliser [trinket](https://trinket.io/) pour écrire du Python en ligne. Ce projet contient les Trinkets suivants :

+ ['Jeu de rôle' point de départ -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

Il y a également un trinket qui contient le projet fini :

+ [‘Jeu de rôle’ finalisé -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

# Ressources hors-ligne
Ce projet peut être [complété hors-ligne](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) i préférable. Vous pouvez accéder aux ressources du projet en cliquant sur 'Matériaux du Projet'. Ce lien contient une section 'Ressources du projet', y compris vers des ressources dont les enfants auraient besoin pour compléter le projet hors-ligne. Vérifiez que chaque enfant a accès à une copie de ces ressources. Cette section comporte les fichiers suivants :

+ rpg/rpg.py

Vous pouvez aussi trouver une version finalisée des défis de ce projet dans la section 'Ressources du volontaire', qui contient :

+ rpg-finished/rpg.py

(Toutes les ressources ci-dessus sont également téléchargeables comme des fichiers `.zip` pour le projet et les volontaires.)

# Objectifs pédagogiques
+ Dessin de jeu ;
+ Édition :
	+ Listes ;
	+ Dictionaires.
+ Des expressions Booléenes.

Ce projet couvre des élements des parcours suivants du [Programme de Créativité Numérique Raspberry Pi](http://rpf.io/curriculum) :

+ [Combiner des structures de programmation afin de résoudre des problèmes.](https://www.raspberrypi.org/curriculum/programming/builder)

# Défis
+ Ajoute de nouvelles pièces ;
+ Ajoute des nouveaux articles ;
+ Ajoute des adversaires à éviter ;
+ Développer ton propre jeu.

# Foire à questions
+ Peut-être les enfants auraient besoin d'être rappelés que les éléments d'un dictionnaire/liste sont séparés par des virgules. Par exemple, quand on ajoute une nouvelle pièce au dictionnaire 'rooms', une virgule doit être insérée entre la nouvelle pièce ajoutée et la précédente.
+ Quand on ajoute une nouvelle pièce, les enfants pourraient oublier de relier la pièce existants et la nouvelle qui vient d'être créée. Ça pourrait dire que les enfants peuvent sortir de la pièce mais pas entrer !
+ Le code pour vérifier si le joueur a gagné ou a perdu doit être décalé, afin de s'assure que la contrôle se fait à chaque entrée dans une nouvelle pièce. Si le code n'est pas décalé, cette partie reste à l'extérieur de la boucle principale du jeu et ne s'exécute jamais.
