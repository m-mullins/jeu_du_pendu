# jeu_du_pendu

FONCTIONNEMENT
Pour jouer au pendu, il faut exécuter le script jeu_du_pendu.py.
En exécutant le script, la fonction jouer_au_pendu est appelée et permet de débuter le jeu.


FICHIER mots_pendu.txt
Contient la liste de mots que nous utiliserons pour jouer au jeu du pendu.


FICHIER jeu_du_pendu.py
Contient les fonctions qui permettent de jouer au pendu.
Voici une description de chaque fonction du fichier:

generer_mot : lit le fichier texte et retourne un mot au hasard dans la liste

entrer_lettre: demande à l'usager une lettre et retourne la lettre

afficher_etat_lettres: affiche l'état des lettres trouvées et celle encore inconnues

calculer_lettres_restantes: calcule le nombre de lettres restants à trouver et retourne ce nombre

verifier_etat_jeu: vérifie si l'usage a gagné ou perdu. S'il n'a ni gagné ou perdu, le nombre de chances restantes est retourné

jouer_au_pendu: fonction principale qui permet de jouer au jeu
