import random
from color import color_print
from class_project import Game
from class_project import Actions
from class_project import Player2
from class_project import PlayAgain


def main():
    options = ['paper', 'rock', 'spock', 'scissors', 'lizard']
    game = Game()
    if game.player1 == "1":
        Player2()
    else:
        computer = Actions((random.choice(options)))

        user_action = input("Your pick: ")
        if user_action.lower() in computer.lose:
            print(f"You chose ({user_action}) computer chose ({computer}) YOU ARE VICTORIOUS! ")
        elif user_action in computer.win:
            print(f"You chose ({user_action}) computer chose ({computer}) YOU LOST! ")
        else:
            color_print(f"You both chose {user_action} It's a draw")
    PlayAgain()


if __name__ == '__main__':
    main()
