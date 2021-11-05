import random
from getpass import getpass

from color import color_print


class Game:
    def __init__(self):
        color_print('magenta', '*** Welcome to the rock, paper, scissors, spock and lizard game. ***')
        self.player1 = None
        self.player2 = None
        self.chose_player()

    def chose_player(self):
        while True:
            self.player1 = input('Who do you wanna play against?player2: [1] Computer:[2]\n')
            if self.player1 == '1':
                return color_print('cyan', '* You are playing against another player')
            elif self.player1 == '2':
                return color_print('yellow', '* You are playing against the computer!')
            else:
                color_print('red', 'Not an option')


class Actions:

    def __init__(self, action_name):

        self.action_name = action_name
        self.win, self.lose = self.set_win_lose()

    def set_win_lose(self):
        if self.action_name == 'paper':
            return ['rock', 'spock'], ['scissors', 'lizard']
        if self.action_name == 'rock':
            return ['scissors', 'lizard'], ['paper', 'spock']
        if self.action_name == 'scissors':
            return ['paper', 'lizard'], ['rock', 'spock']
        if self.action_name == 'spock':
            return ['rock', 'scissors'], ['paper', 'lizard']
        if self.action_name == 'lizard':
            return ['spock', 'paper'], ['rock', 'scissors']

    def out_of_range(self):
        if self.tie != ['paper', 'rock', 'spock', 'scissors', 'lizard']:
            print("you must chose between 'paper', 'rock', 'spock', 'scissors', 'lizard'")

    def __str__(self):
        return self.action_name


class Player2:
    def __init__(self):
        self.player2()

    def player2(self):

        user_action = input('player ones pick: ')
        user_action2 = input('player 2s pick: ')
        player1 = Actions(user_action)
        if user_action2.lower() in player1.win:
            color_print('yellow', f'* You chose ({user_action}) player2 chose ({user_action2}) YOU ARE VICTORIOUS! ')
        elif user_action2.lower() in player1.lose:
            color_print('blue', f'* You chose ({user_action}) player2 chose ({user_action2}) YOU LOST! ')
        else:
            color_print("green", f"* You both chose {user_action, user_action2} It's a draw ")


class PlayAgain:
    def __init__(self):
        self.play_again()

    def play_again(self):
        while True:
            user = input('do you wish to play again? [y] [n]\n ').lower()
            if user in 'y':
                print('Lets go!')
                main()
            elif user in 'n':
                print('What a shame. Bye then! ')
                break
            else:
                color_print('red', 'Not an option, try again.')


def main():
    game = Game()
    options = ['paper', 'rock', 'spock', 'scissors', 'lizard']
    if game.player1 == '1':
        Player2()
    else:
        if game.player1 == '2':
            computer = Actions((random.choice(options)))
        user_action = input("Your pick: ")
        if user_action.lower() in computer.lose:
            color_print('yellow', f'* You chose ({user_action}) player2 chose ({computer}) YOU ARE VICTORIOUS! ')
        elif user_action in computer.win:
            color_print('blue', f'* You chose ({user_action}) player2 chose ({computer}) YOU LOST! ')
        else:
            color_print("green", f"* You both chose {user_action} It's a draw")
    PlayAgain()


if __name__ == '__main__':
    main()
