# Créé par Julien Pollart le 28 novembre 2022

from random import randint
import argparse


class Joueur:
    def __init__(self, pseudo: str, score: int = 0):
        self.__pseudo: str = pseudo
        self.__score: int = score

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def score(self):
        return self.__score

    @staticmethod
    def pseudo_in_list(list_player: list, pseudo: str):
        for joueur in list_player:
            if joueur.pseudo == pseudo:
                return joueur
        return None


url: str = "game_saved.txt"


def save_game(pseudo: str, score: int):
    """Cette fonction va recevoir en paramètre le nom du joueur et son score pour ensuite tout sauvegarder dans un
    fichier texte. Si le joueur est déjà inscrit, la fonction va juste écrasé le score par le nouveau si celui-ci est
    meilleur que le précédent. PRE: --pseudo: str(optionnel) score: int POST: écrit le pseudo et le score dans un
    fichier texte
    """
    try:
        with open(url, "rt") as file_read:
            lines: list = file_read.readlines()
        list_pseudo: list = []
        for line in lines:
            line: str
            joueur = Joueur(line.split()[0], int(line.split()[1]))
            list_pseudo.append(joueur)
        joueur: Joueur = Joueur.pseudo_in_list(list_pseudo, pseudo)
        if not joueur:
            with open(url, "at") as file_write:
                file_write.write(f"{pseudo} {score}\n")
        elif joueur.score > score:
            for i in range(len(lines)):
                if lines[i].split()[0] == joueur.pseudo:
                    lines[i] = f"{pseudo} {score}\n"
                    break
            with open(url, "wt") as file_write:
                for line in lines:
                    file_write.write(line)
        return None
    except FileNotFoundError:
        open(url, "x")
        save_game(pseudo, score)


def main():
    parser = argparse.ArgumentParser(
        description='Définir le minimum et le maximum de la plage où se trouvera le nombre.')
    parser.add_argument("--pseudo", metavar='pseudo', type=str, help='Entrez votre pseudo (optionnel)')
    parser.add_argument('minimum', metavar='min', type=int, help='Entre le minimum')
    parser.add_argument('maximum', metavar='max', type=int, help='Entrez le maximum')
    args = parser.parse_args()
    minimum = args.minimum
    maximum = args.maximum
    pseudo = args.pseudo
    nbr_essai = 0
    random_number = randint(minimum, maximum)

    nbr = input("\n>Devinez le nombre en un minimum d'essai. \n>Quel nombre choissisez vous ? : \n>> ")

    while int(nbr) != random_number:
        while int(nbr) > 50:
            nbr = input("\n> Veuillez entrer un nombre correct, vous avez rentré un nombre trop grand (>50)\n>> ")
            continue

        if int(nbr) == 0:
            break
        elif int(nbr) > random_number:
            nbr = input("\n> Votre nombre est plus grand que le nombre à trouver. Vous pouvez quitter en tapant : 0. "
                        "Veuillez réessayer : \n>> ")
            nbr_essai += 1
        elif int(nbr) < random_number:
            nbr = input("\n> Votre nombre est plus petit que le nombre à trouver. Vous pouvez quitter en tapant : 0. "
                        "Veuillez réessayer : \n>> ")
            nbr_essai += 1

    nbr_essai += 1
    if int(nbr) == 0:
        nbr_essai -= 1
        if nbr_essai <= 1:
            print("\n### Vous avez décidé d'arrêter, vous avez efectué " + str(nbr_essai) + " essai. ###")
        elif nbr_essai > 1:
            print("\n### Vous avez décidé d'arrêter, vous avez effectué " + str(nbr_essai) + " essais. ###")
    elif nbr_essai == 1:
        print("\n### Vous avez réussi avec un total de " + str(nbr_essai) + " essai. ###")
        save_game(pseudo, nbr_essai)
    else:
        print("\n### Vous avez réussi avec un total de " + str(nbr_essai) + " essais. ###")
        save_game(pseudo, nbr_essai)


if __name__ == "__main__":
    main()
