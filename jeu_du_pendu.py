def generer_mot(fichier_texte):
    import random

    # Lire le fichier texte
    with open(fichier_texte, "r") as file:
        contenu = file.readlines()

    # Choisir le mot au harsard
    mot = random.choice(contenu)

    # Enlever le \n
    mot = mot.replace("\n", "")

    return mot


def entrer_lettre():
    # Demander à l'utilisateur d'entrer une lettre
    lettre = input("Entrez une lettre: ")
    return lettre


def afficher_etat_lettres(mot_genere, lettres_devinees):
    # Initialiser l'etat
    etat = ""

    # Itérer à travers chaque lettre du mot
    for i in range(len(mot_genere)):
        # Vérifier si la lettre a été devinée
        if mot_genere[i] in lettres_devinees:
            etat += mot_genere[i]

        # Afficher "_" sinon
        else:
            etat += "_"

    # Afficher et retourner l'état
    print(f"\n{etat}")
    return etat


def calculer_lettres_restantes(etat):
    # Initialiser le nombre de lettres restantes
    lettres_restantes = 0

    # Itérer à travers chaque lettre de l'etat
    for i in range(len(etat)):
        if etat[i] == "_":
            lettres_restantes += 1

    # Retourner le nombre de lettres restantes
    return lettres_restantes


def vérifier_etat_jeu(lettres_manquees, lettres_restantes, nombre_chances):
    # Initialiser l'état
    etat_jeu = ""

    # Calculer les chances utilisées
    chances_utilisees = len(lettres_manquees)

    # Vérifier si l'usager a gagné
    if lettres_restantes == 0:
        etat_jeu = "Victoire"

    # Vérifier si l'usager a perdu
    elif chances_utilisees >= nombre_chances:
        etat_jeu = "Défaite"

    # Calculer les chances restantes si ni gagné ou perdu
    else:
        chances_restantes = 0
        chances_restantes = nombre_chances - chances_utilisees
        etat_jeu = str(chances_restantes)

    # Retourner l'état du jeu
    return etat_jeu


def jouer_au_pendu():

    # Initialiser les variables et constantes
    NOMBRES_CHANCES = 6
    chances_utilisees = 0
    lettres_devinees = []
    lettres_manquees = []

    # Afficher un mot d'introduction
    print("********* Jeu du pendu *********\n\
Ce programme permet de jour au pendu.\n\
Commencez pas entrer une lettre dans le terminal!\n")

    # Générer un mot au hasard
    mot_genere = generer_mot("mots_pendu.txt")

    # Jouer tant que le joueur a des chances
    while chances_utilisees < NOMBRES_CHANCES:
        # Afficher l'etat actuel des mots
        etat_lettres = afficher_etat_lettres(mot_genere, lettres_devinees)

        # Calculer le nombres de lettres restantes
        lettres_restantes = calculer_lettres_restantes(etat_lettres)

        # Vérifier si l'usager a gagné
        etat_jeu = vérifier_etat_jeu(lettres_manquees, lettres_restantes, NOMBRES_CHANCES)
        if etat_jeu == "Victoire":
            print("Vous avez gagné")
            return

        # Demander au joueur une nouvelle lettre
        nouvelle_lettre = entrer_lettre()

        # Vérifier si la lettre est dans le mot
        if nouvelle_lettre in mot_genere:
            # Mettre à jour la liste de lettres trouvées
            lettres_devinees.append(nouvelle_lettre)
            print(f"La lettre {nouvelle_lettre} est dans le mot")

        else:
            # Mettre à jour la liste de lettres manquées
            lettres_manquees.append(nouvelle_lettre)

            # Incrémenter le nombre de chances utilisées
            chances_utilisees += 1
            print(f"La lettre {nouvelle_lettre} n'est pas dans le mot")

            # Vérifier si l'usager a perdu et quitter si oui
            etat_jeu = vérifier_etat_jeu(lettres_manquees, lettres_restantes, NOMBRES_CHANCES)
            if etat_jeu == "Défaite":
                print("Vous avez perdu")
                print(f"Le mot était: {mot_genere}")
                return

            # Afficher le nombre de chances restantes sinon
            else:
                chancesRestantes = NOMBRES_CHANCES - chances_utilisees
                print(f"Il vous reste {chancesRestantes} chances")


jouer_au_pendu()
