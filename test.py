import random
from color import color_print


def main():
    while True:
        actions = ["rock", "paper", "scissors",  "lizard"]

        while True:
            user = input("please make a choice(rock, paper, scissors, spock, lizard): ").lower()
            if user.lower() in actions:
                break
            print('Invalid value. You must pick either rock, paper, or scissors')
        pc_choice = random.choice(actions)
        color_print("yellow", f"\nYou chose {user}, computer chose {pc_choice}.\n")

        if user == pc_choice:
            color_print("green", f"Both player have chosen {user}. It's a TIE! ")
        elif user == "rock":
            if pc_choice == "scissors":
                color_print("cyan", "Rock breaks scissors! VICTORY! ")
            elif pc_choice == "lizard":
                color_print("cyan", "Rock breaks lizard! VICTORY! ")
                break


if __name__ == '__main__':
    main()
