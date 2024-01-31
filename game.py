import random
from colorama import init, Fore, Style

init()

RESET = Style.RESET_ALL
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE


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


def initialiser_personnages():
    nom = input("Entrez le nom de votre personnage : ")
    joueur = Personnage(nom=nom, attaque=20, pv=100, defense=20, esquive=15, experience=0, points=0, vivant=True)
    gobelin = Personnage(nom="gobelin", attaque=10, pv=50, defense=5, esquive=25, experience=20, points=10, vivant=True)
    troll = Personnage(nom="troll", attaque=25, pv=100, defense=10, esquive=0, experience=40, points=20, vivant=True)
    return joueur, gobelin, troll


def attaquer(attaquant, cible, ennemis):
    precision = random.randint(1, 100)
    print(f"\n{WHITE}Précision :{RESET} {precision}")
    print(f"{YELLOW}{attaquant.nom} attaque {cible.nom}")
    degats_aleatoire = random.randint(1, 10)
    print(f"{WHITE}Le monde décide que l'attaque effectue {YELLOW}{degats_aleatoire} degats supplémentaires !")

    if precision > cible.esquive and attaquant.vivant:
        degats = attaquant.attaque - cible.defense + degats_aleatoire
        if degats <= 0:
            print(f"{YELLOW}L'attaque n'a pas causé de dégâts !")
        elif precision >= 90:
            degats *= 2
            cible.pv -= degats
            print(f"{RED}{cible.nom} subit un coup critique de {degats} dégâts.")
        else:
            cible.pv -= degats
            print(f"{WHITE}{cible.nom} subit {RED}{degats} dégâts.")

        if cible.pv <= 0:
            cible.vivant = False
            if cible in ennemis:
                ennemis.remove(cible)
                print(f"{GREEN}\nL'attaque a achevé {cible.nom} !")
                print(f"{WHITE}Votre expérience a augmenté de {BLUE}{cible.experience} points")
                print(f"{WHITE}Votre score a augmenté de {BLUE}{cible.points} points")
                attaquant.experience += cible.experience
                attaquant.points += cible.points
        else:
            print(f"{WHITE}{cible.nom} a maintenant {GREEN}{cible.pv} PV." + RESET)
    else:
        print(f"{YELLOW}{cible.nom} n'a pas été touché" + RESET)


def augmenter_niveau(niveau):
    if joueur.experience >= niveau * 20:
        niveau += 1
        print(f"{MAGENTA}\nVous êtes monté de niveau ! \nVous êtes niveau {niveau} !")
        joueur.experience -= niveau * 20
        print(f"{WHITE}Il vous manque {niveau * 20} XP jusqu'au prochain niveau !")
        print(f"{CYAN}Vos statistiques avant le gain de niveau :\nAttaque : {joueur.attaque}\n" +
              f"Défense : {joueur.defense}\nPV : {joueur.pv}\nTaux d'esquive : {joueur.esquive}%")

        joueur.attaque = niveau * 5 + 15
        joueur.defense = niveau * 4 + 11
        joueur.pv = niveau * 20 + 80
        joueur.esquive = niveau * 2 + 13
        if joueur.esquive > 60:
            print(f"{CYAN} Vous avez atteint l'esquive maximale (60 %)")
            joueur.esquive = 60
        print(f"{CYAN}\nVos statistiques après le gain de niveau :\nAttaque : {joueur.attaque}\n" +
              f"Défense : {joueur.defense}\nPV : {joueur.pv}\nTaux d'esquive : {joueur.esquive}%\n" + RESET)
        return niveau, joueur


def creer_ennemi(nom, compteur, niveau):
    attaque_random = random.randint(-2, 2)  # Ajout d'une petite variabilité
    pv_random = random.randint(-5, 5)
    defense_random = random.randint(-1, 1)
    esquive_random = random.randint(-2, 2)

    if nom == "gobelin":
        attaque = attaque_random + 8 + niveau * 2
        pv = pv_random + 40 + niveau * 10
        defense = defense_random + 4 + niveau * 1
        esquive = esquive_random + 23 + niveau * 2
        points = 10
        experience = 20

    elif nom == "troll":
        attaque = attaque_random + 8 + niveau * 2
        pv = pv_random + 40 + niveau * 10
        defense = defense_random + 4 + niveau * 1
        esquive = esquive_random + 23 + niveau * 2
        points = 20
        experience = 40

    else:
        attaque = 0
        pv = 0
        defense = 0
        esquive = 0
        points = 0
        experience = 0

    return Personnage(nom=f"{nom} {compteur} niveau {niveau}", attaque=attaque, pv=pv, defense=defense, esquive=esquive,
                      experience=experience, points=points, vivant=True)


def generer_ennemis(niveau, ennemis, compteur_goblin=0, compteur_troll=0):
    if len(ennemis) <= niveau:
        for i in range(0, niveau):
            choix = random.randint(1, 2)
            if choix == 1:
                compteur_goblin += 1
                gobelin = creer_ennemi(f"gobelin", compteur_goblin, niveau)
                ennemis.append(gobelin)
                print(f"{RESET}Les statistiques de {gobelin.nom} :\n" +
                      f"Attaque : {gobelin.attaque}\nDéfense : {gobelin.defense}\n" +
                      f"PV Max : {gobelin.pv}\nTaux d'esquive : {gobelin.esquive}%{WHITE}")
            if choix == 2:
                compteur_troll += 1
                troll = creer_ennemi(f"troll", compteur_troll, niveau)
                ennemis.append(troll)
                print(f"{RESET}Les statistiques de {troll.nom} :\n" +
                      f"Attaque : {troll.attaque}\nDéfense : {troll.defense}\n" +
                      f"PV Max : {troll.pv}\nTaux d'esquive : {troll.esquive}%{WHITE}")
            print(f"{RESET}Vous avez {len(ennemis)} ennemi !{WHITE}")
    return ennemis


if __name__ == "__main__":
    joueur, gobelin, troll = initialiser_personnages()
    niveau = 1
    experience = 0
    score = 0
    ennemis = []
    print("Bienvenue dans ce jeu ! \nL'objectif est de survivre aussi longtemps que possible face aux monstres qui"
          "seront de plus en plus nombreux !\nMais pas d'inquiétude en vaiquant des énemis vous gagnerez en expérince"
          "ainsi qu'en niveaux.\nMalheuresement les monstres se renforce et suivent également votre progression !"
          f"\n Bonne chance {GREEN}{joueur.nom} !\n")
    print(f"{CYAN}Vos statistiques de départ :\nAttaque : {joueur.attaque}\n" +
          f"Défense : {joueur.defense}\nPV Max : {joueur.pv}\n" +
          f"Taux d'esquive : {joueur.esquive}%\n" + RESET)
    ennemis = generer_ennemis(niveau, ennemis)

    while joueur.vivant:
        choix = True
        while choix:
            choix = input(f"{RESET}Choisissez un ennemi à attaquer entre 1 et {len(ennemis)} "
                          f"(ou tapez 'quitter' pour quitter) : \n{WHITE}")

            if choix.lower() == "quitter":
                joueur.vivant = False
                break

            try:
                choix = int(choix)
                if 1 <= choix <= len(ennemis):
                    attaquer(joueur, ennemis[choix - 1], ennemis)
                    break
                else:
                    print(f"{WHITE}Choix invalide. Veuillez choisir un ennemi valide.")
            except ValueError:
                print(f"{WHITE}Veuillez entrer un nombre entier (ou 'quitter').")

        for i in range(len(ennemis)):
            attaquer(ennemis[i], joueur, ennemis)

        if len(ennemis) == 0:
            niveau, joueur = augmenter_niveau(niveau)
            ennemis = generer_ennemis(niveau, ennemis)

    print(f"{WHITE}{joueur.nom} a maintenant {GREEN}{joueur.pv} PV.")
    print(f"\nMerci d'avoir joué {joueur.nom} ! ")
    print(f"\nVotre score : {joueur.points}\nVotre niveau : {niveau} {joueur.experience}" + RESET)
    continuer = input("Souhiatez vous continuer ? (oui)")
    if continuer == "oui":
        joueur.vivant = True
