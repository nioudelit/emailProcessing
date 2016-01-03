# Vérifier avec Processing et un petit script Python si on a reçu un ou des nouveaux e-mails sur sa boi-boite.

Est requis:

1. Savoir se placer dans un dossier avec la console
2. Savoir executer un script python avec la console
3. Savoir repérer les variables à remplacer
4. Bases en Processing

## 1. Fontionnement

Ce programme n'est pas optimal (boucle infinie et sleep() avec python), mais dans le cadre d'installation à but artistique à la con, il pourrait avoir son utilité, voici comment il fonctionne.

**mail.py**

Un script python (mail.py)compte le nombre de mail reçus sur votre boite mail. Pour qu'il fonctionne, il vous faudra changer le contenu de quelques variables (précisions en commentaires). Une fois placé dans le bon dossier, il faudra lancer le script avec : 

> python mail.py

Si vous avez bien paramétré ce fichier, il s'affichera des informations relatives au contenu de votre boite mail.

*Je vous conseille de vous créer une nouvelle boite mail vierge, parce que ça va récupérer tous les mails que vous avez reçu. Si vous en avez 20.000, ça va prendre un peu plus de temps.*

Le programme, au sein d'une boucle va compter le nombre de mails à l'interieur d'une variable, sauvegarder cette valeur dans un fichier ("nbr.txt"). Si la valeur de la variable correspond au nombre sauvegardé, pas de nouveaux messages, on écrit un magnifique "0" dans le fichier ("verif.txt"). Dans le cas contraire, si le nombre sauvegardé est différent du suivant, vous avez au moins un nouveau message. On écrit un "1" dans "verif.txt". Au prochain tour de boucle, si vous n'avez pas de nouveaux messages, un zéro remplacera le "1": tout se passera bien.

Vous comprenez qu'au tout premier lancement, quoi qu'il arrive, le programme vous dira qu'il y a des nouveaux messages (si vous avez au moins un mail reçu).

**graphique.pde**

Une fois que le programme Python est lancé (il tournera en boucle, il s'actualise toutes les minutes, faites CTRL+C pour arreter), ouvrez le fichier Processing, "graphique.pde". Il vous faudra changer la variable "raccourci" est mettre un lien correct qui corresponde à l'organisation de vos fichiers sur votre ordinateur.
Au premier tour de boucle du fichier mail.py, le fond sera gris. Au deuxième, si vous avez au moins un message sur votre boite, il deviendra vert. Au troisième, si vous n'avez pas de messages, le fond restera vert tant que vous n'avez pas "relevé" le changement, par le biais d'un clic de souris. Si vous voulez que le fond soit noir ou vert à chaque tour de boucle sans interaction particulière, changez la condition.

``` if(numero == 1){
background(0, 255, 0);
}
else {
background(0);
}```

### Changer la fréquence d'actualisation
Allez voir tout à la fin du fichier mail.py, remplacez 60 (= 1 minute) par la valeur voulue.

### Interfacer avec Arduino
On pourrait faire clignoter un LED avec Arduino, en ne passant que par Python. Quelques lignes de code supplémentaires dans le fichier mail.py feront l'affaire. Une petite recherche sur votre moteur de recherche favori et vous trouverez la réponse: "arduino python", "blink led arduino with python"… 


Sources : http://www.developpez.net/forums/d717901/autres-langages/python-zope/reseau-web/recuperer-messages-compte-gmail/



