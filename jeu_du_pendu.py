def generer_mot(fichierTexte):
    import random
    
    # Lire le fichier texte
    with open(fichierTexte,"r") as file:
        contenu = file.readlines()
    
    # Choisir le mot au harsard
    mot = random.choice(contenu)

    # Enlever le \n
    mot = mot.replace("\n","")

    return mot


def entrer_lettre():
    # Demander à l'utilisateur d'entrer une lettre
    lettre = input("Entrez une lettre: ")
    return lettre


def afficher_etat_lettres(motGenere,lettresDevinees):
    # Initialiser l'etat
    etat = ""
    
    # Itérer à travers chaque lettre du mot
    for i in range(len(motGenere)):
        # Vérifier si la lettre a été devinée
        if motGenere[i] in lettresDevinees:
            etat += motGenere[i]
             
        # Afficher "_" sinon
        else:
            etat += "_"

    # Afficher et retourner l'état
    print(f"\n{etat}")
    return etat


def calculer_lettres_restantes(etat):
    # Initialiser le nombre de lettres restantes
    lettresRestantes = 0

    # Itérer à travers chaque lettre de l'etat
    for i in range(len(etat)):
        if etat[i] == "_":
            lettresRestantes += 1
        
    # Retourner le nombre de lettres restantes
    return lettresRestantes


def vérifier_etat_jeu(lettresManquees,lettresRestantes,nombreChances):
    # Initialiser l'état
    etatJeu = ""

    # Calculer les chances utilisées
    chancesUtilisees = len(lettresManquees)

    # Vérifier si l'usager a gagné
    if lettresRestantes == 0:
        etatJeu = "Victoire"

    # Vérifier si l'usager a perdu
    elif chancesUtilisees >= nombreChances:
        etatJeu = "Défaite"

    # Calculer les chances restantes si ni gagné ou perdu
    else:
        chancesRestantes = 0
        chancesRestantes = nombreChances - chancesUtilisees
        etatJeu = str(chancesRestantes)

    # Retourner l'état du jeu
    return etatJeu  


def jouer_au_pendu():

    # Initialiser les variables et constantes
    NOMBRES_CHANCES = 6
    chancesUtilisees = 0
    lettresDevinees = []
    lettresManquees = []

    # Générer un mot au hasard
    motGenere = generer_mot("mots_pendu.txt")

    # Jouer tant que le joueur a des chances
    while chancesUtilisees < NOMBRES_CHANCES:       
        # Afficher l'etat actuel des mots
        etatLettres = afficher_etat_lettres(motGenere,lettresDevinees)

        # Calculer le nombres de lettres restantes
        lettresRestantes = calculer_lettres_restantes(etatLettres)

        # Vérifier si l'usager a gagné
        etatJeu = vérifier_etat_jeu(lettresManquees,lettresRestantes,NOMBRES_CHANCES)
        if etatJeu == "Victoire":
            print("Vous avez gagné")
            return

        # Demander au joueur une nouvelle lettre
        nouvelleLettre = entrer_lettre()

        # Vérifier si la lettre est dans le mot
        if nouvelleLettre in motGenere:
            # Mettre à jour la liste de lettres trouvées
            lettresDevinees.append(nouvelleLettre)
            print(f"La lettre {nouvelleLettre} est dans le mot")

        else:
            # Mettre à jour la liste de lettres manquées
            lettresManquees.append(nouvelleLettre)

            # Incrémenter le nombre de chances utilisées
            chancesUtilisees += 1
            print(f"La lettre {nouvelleLettre} n'est pas dans le mot")

            # Vérifier si l'usager a perdu et quitter si oui
            etatJeu = vérifier_etat_jeu(lettresManquees,lettresRestantes,NOMBRES_CHANCES)
            if etatJeu == "Défaite":
                print("Vous avez perdu")
                return
            
            # Afficher le nombre de chances restantes sinon
            else:
                chancesRestantes = NOMBRES_CHANCES - chancesUtilisees
                print(f"Il vous reste {chancesRestantes} chances")

jouer_au_pendu()