from random import randint
import argparse


def game_one():
    nbr_essai = 0
    print(
        "Vous avez choisi le jeu : GuessTheNumber. Vous allez donc devoir trouver un nombre aléatoirement choisi par "
        "le programme.\n")
    minimum = input("Tout d'abord, veuillez entrer le nombre minimum :\n")
    maximum = input("Ensuite, veuillez entrer le nombre maximum :\n")
    random_number = randint(int(minimum), int(maximum))

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
    else:
        print("\n### Vous avez réussi avec un total de " + str(nbr_essai) + " essais. ###")


def game_two():
    print("Vous avez choisi le jeu Rock-Paper-Scissors (Pierre-Papier-Ciseau)\n")


def main():
    parser = argparse.ArgumentParser(
        description='Choisisser le jeu que vous désirez entre le GuessTheNumber et le Pierre/Feuille/Ciseau')
    parser.add_argument('game', metavar='game', type=int, help='Entrez 1 pour le premier jeu et 2 pour le deuxième')
    args = parser.parse_args()
    game_choice = args.game
    if game_choice == 1:
        game_one()
    elif game_choice == 2:
        game_two()
    else:
        print(
            "Vous n'avez pas rentré une lettre correspondant à un jeu existant. Faites 'py games_script.py -h' pour "
            "avoir plus d'informations.")


if __name__ == "__main__":
    main()
