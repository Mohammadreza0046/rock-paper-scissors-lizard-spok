# Import random to be able to play against the PC
import random
from color import color_print


def main():
    while True:
        actions = ["rock", "paper", "scissors"]

        while True:
            user = input("please make a choice(rock, paper, scissors): ").lower()
            if user.lower() in actions:
                break
            print('Invalid value. You must pick either rock, paper, or scissors')
        pc_choice = random.choice(actions)
        color_print("yellow", f"\nYou chose {user}, computer chose {pc_choice}.\n")

        if user == pc_choice:
            color_print("green", f"Both player have chosen {user}. It's a TIE! ")
        elif user == "rock":
            if pc_choice == "scissors":
                color_print("cyan", "Rck breaks scissors! VICTORY! ")
            else:
                color_print("red", "Paper covers rock! You lose! ")
        elif user == "paper":
            if pc_choice == "rock":
                color_print("cyan", "Paper covers rock! VICTORY! ")
            else:
                color_print("red", "Scissors cuts paper! You lose! ")
        elif user == "scissors":
            if pc_choice == "paper":
                color_print("cyan", "Scissors cuts paper! VICTORY! ")
            else:
                color_print("red", "Rock breaks scissors! You lose! ")

        while True:
            try_again = input("another round? (y/n): ")
            if try_again.lower() in ['y', 'n']:
                break
            print('You must select either y or n')
        if try_again.lower() == "y":
            continue
        elif try_again.lower() == "n":
            print("You are not worth of my time anyway!")
            break


if __name__ == '__main__':
    main()
