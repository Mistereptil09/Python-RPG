# Importation du module random pour générer des nombres aléatoires
import random

# Création des variables pour les couleurs de texte avec des codes ANSI
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Création de la classe "Personnage" pour représenter les personnages du jeu
class Personnage:
    def __init__(self, nom, attaque, pv, defense, esquive, experience, points, vivant):
        self.nom = nom
        self.attaque = attaque
        self.pv = pv
        self.defense = defense
        self.esquive = esquive
        self.experience = experience
        self.points = points
        self.vivant = vivant

# Fonction pour créer tous les personnages du jeu à partir de l'objet "Personnage"
def initialiser_personnages():
    nom = input(WHITE + "Entrez le nom de votre personnage : " + RESET)
    joueur = Personnage(nom=nom, attaque=20, pv=100, defense=15, esquive=15, experience=0, points=0, vivant=True)
    gobelin = Personnage(nom="gobelin", attaque=10, pv=50, defense=5, esquive=25, experience=20, points=10, vivant=True)
    troll = Personnage(nom="troll", attaque=25, pv=100, defense=10, esquive=0, experience=40, points=20, vivant=True)
    return joueur, gobelin, troll

# Fonction pour la partie calcul de dégâts avec un attaquant et sa cible
# Fonction pour attaquer un ennemi
def attaquer(attaquant, cible, niveau, ennemis):
    precision = random.randint(1, 100)
    print(WHITE + "Précision : " + str(precision))

    if precision > cible.esquive and attaquant.vivant:
        degats = attaquant.attaque - cible.defense
        if degats <= 0:
            print(YELLOW + "L'attaque n'a pas causé de dégâts !")
        elif precision >= 90:
            degats *= 2
            cible.pv -= degats
            print(RED + f"{cible.nom} subit un coup critique de {degats} dégâts.")
        else:
            cible.pv -= degats
            print(WHITE + f"{cible.nom} subit {RED}{degats} dégâts.")

        if cible.pv <= 0:
            cible.vivant = False
            if cible in ennemis:
                ennemis.remove(cible)
                print(GREEN + f"\nL'attaque a achevé {cible.nom} !")
                print(WHITE + f"Votre expérience a augmenté de {BLUE}{cible.experience} points")
                print(WHITE + f"Votre score a augmenté de {BLUE}{cible.points} points")
                attaquant.experience += cible.experience
                attaquant.points += cible.points
                augmenter_niveau(niveau)
        else:
            print(WHITE + f"{cible.nom} a maintenant {GREEN}{cible.pv} PV." + RESET)
    else:
        print(YELLOW + f"{cible.nom} n'a pas été touché" + RESET)


# Fonction pour augmenter le niveau et les statistiques du joueur avec une variable expérience
def augmenter_niveau(niveau):
    if joueur.experience >= niveau * 20:
        niveau += 1
        print(MAGENTA + "\nVous êtes monté de niveau ! \nVous êtes niveau " + str(niveau) + " !")
        joueur.experience -= niveau * 20
        print(WHITE + "Il vous manque " + str(niveau * 20) + " XP jusqu'au prochain niveau !")
        print(CYAN + "Vos statistiques avant le gain de niveau :\n" + "Attaque : " + str(joueur.attaque) + "\n" +
              "Défense : " + str(joueur.defense) + "\n" + "PV : " + str(joueur.pv) + "\n" +
              "Taux d'esquive : " + str(joueur.esquive) + "%")

        #fait les caluls pour augmenter les statistiques du joueur
        joueur.attaque += niveau * 5 - 5
        joueur.defense += niveau * 4 - 4
        joueur.pv += 100 + niveau * 20 - 20
        joueur.esquive += niveau * 2 - 2
        if joueur.esquive > 60:
            joueur.esquive = 60
        print(CYAN + "\nVos statistiques après le gain de niveau :\n" + "Attaque : " + str(joueur.attaque) + "\n" +
              "Défense : " + str(joueur.defense) + "\n" + "PV : " + str(joueur.pv) + "\n" +
              "Taux d'esquive : " + str(joueur.esquive) + "%\n" + RESET)
        return niveau, joueur

# Fonction pour générer des ennemis en fonction du niveau
def generer_ennemis(niveau, ennemis, compteur_goblin=0, compteur_troll=0):
    if len(ennemis) < niveau:
        for i in range(niveau):
            choix = random.randint(1, 2)
            if choix == 1:
                compteur_goblin += 1
                gobelin = Personnage(nom="gobelin " + str(compteur_goblin), attaque=10, pv=50, defense=5, esquive=25, experience=20, points=10, vivant=True)
                ennemis.append(gobelin)
                print(WHITE + "Les statistiques de " + str(gobelin.nom) + ":\n" +
                      "Attaque : " + str(gobelin.attaque) + "\n" + "Défense : " + str(gobelin.defense) + "\n" +
                      "PV Max : " + str(gobelin.pv) + "\n" + "Taux d'esquive : " + str(gobelin.esquive) + "%")
            if choix == 2:
                compteur_troll += 1
                troll = Personnage(nom="troll " + str(compteur_troll), attaque=25, pv=100, defense=10, esquive=0, experience=40, points=20, vivant=True)
                ennemis.append(troll)
                print(WHITE + "Les statistiques de " + str(troll.nom) + ":\n" +
                      "Attaque : " + str(troll.attaque) + "\n" + "Défense : " + str(troll.defense) + "\n" +
                      "PV Max : " + str(troll.pv) + "\n" + "Taux d'esquive : " + str(troll.esquive) + "%")
            print("Vous avez " + str(len(ennemis)) + " ennemi !")
    return ennemis

# Bloc principal du programme
if __name__ == "__main__":
    joueur, gobelin, troll = initialiser_personnages()
    niveau = 1
    experience = 0
    score = 0
    ennemis = []

    # Affichage des statistiques initiales du joueur
    print(CYAN + "Vos statistiques de départ :\n" + "Attaque : " + str(joueur.attaque) + "\n" +
          "Défense : " + str(joueur.defense) + "\n" + "PV Max : " + str(joueur.pv) + "\n" +
          "Taux d'esquive : " + str(joueur.esquive) + "%\n")

    # Boucle principale du jeu
    while joueur.vivant:
        ennemis = generer_ennemis(niveau, ennemis)

        # Boucle pour choisir et attaquer un ennemi
        while True:
            choix = input(WHITE + "Choisissez un ennemi à attaquer entre 1 et " + str(
                len(ennemis)) + " (ou tapez 'non' pour quitter) : \n")

            if choix.lower() == "non":
                joueur.vivant = False
                break

            try:
                choix = int(choix)
                if 1 <= choix <= len(ennemis):
                    attaquer(joueur, ennemis[choix - 1], niveau, ennemis)
                    break
                else:
                    print(WHITE + "Choix invalide. Veuillez choisir un ennemi valide.")
            except ValueError:
                print(WHITE + "Veuillez entrer un nombre entier (ou 'non').")

        # Attaque de tous les ennemis restants sur le joueur
        for i in range(len(ennemis)):
            attaquer(ennemis[i], joueur, niveau, ennemis)
        # Si tous les ennemis ont été vaincus, en générer de nouveaux
        if len(ennemis) == 0:
            ennemis = generer_ennemis(niveau, ennemis)

    # Affichage des statistiques finales du joueur
    print(WHITE + joueur.nom + " a maintenant " + GREEN + str(joueur.pv) + " PV.")
    print("\nMerci d'avoir joué " + joueur.nom + " ! ")
    print("\nVotre score : " + str(joueur.points) + "\nVotre niveau : " + str(niveau) + RESET)
