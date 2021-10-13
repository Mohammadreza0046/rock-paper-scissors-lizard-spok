# Import random to be able to play against the PC
import random
from color import color_print


def main():
    while True:
        actions = ["rock", "paper", "scissors", "spock", "lizard"]

        while True:
            user = input("please make a choice(rock, paper, scissors, spock, lizard): ").lower()
            if user.lower() in actions:
                break
            color_print('red', 'Invalid value. You must either pick rock, paper, scissors, spock or lizard')
        pc_choice = random.choice(actions)
        color_print("yellow", f"\nYou chose {user}, computer chose {pc_choice}.\n")

        if user == pc_choice:
            color_print("green", f"Both player have chosen {user}. It's a TIE! ")
        elif user == "rock":
            if pc_choice == "scissors":
                color_print("cyan", "Rock breaks scissors! VICTORY! ")
            elif pc_choice == "lizard":
                color_print("cyan", "Rock breaks lizard! VICTORY! ")
            elif pc_choice == "spock":
                color_print("red", "spock vaporizes covers rock! You lose! ")
            else:
                color_print("red", "Paper covers rock! You lose! ")
        elif user == "paper":
            if pc_choice == "rock":
                color_print("cyan", "Paper covers rock! VICTORY! ")
            elif pc_choice == "spock":
                color_print("cyan", "Paper disproves spock! VICTORY! ")
            elif pc_choice == "lizard":
                color_print("red", "lizard eats paper! You lose! ")
            else:
                color_print("red", "Scissors cuts paper! You lose! ")
        elif user == "scissors":
            if pc_choice == "paper":
                color_print("cyan", "Scissors cuts paper! VICTORY! ")
            elif pc_choice == "lizard":
                color_print("cyan", "Scissors decapitates lizard! VICTORY! ")
            elif pc_choice == "spock":
                color_print("red", "spock smashes scissors! You lose! ")
            else:
                color_print("red", "Rock breaks scissors! You lose! ")
        elif user == "spock":
            if pc_choice == "scissors":
                color_print("cyan", "spock smashes scissors! VICTORY! ")
            elif pc_choice == "rock":
                color_print("cyan", "spock vaporize rock! VICTORY! ")
            elif pc_choice == "paper":
                color_print("red", "paper disproves spock! You lose! ")
            else:
                color_print("red", "lizard poisons spock! You lose! ")
        elif user == "lizard":
            if pc_choice == "paper":
                color_print("cyan", "lizard eats paper! VICTORY! ")
            elif pc_choice == "spock":
                color_print("cyan", "lizard poisons spock! VICTORY! ")
            elif pc_choice == "scissors":
                color_print("red", "scissors decapitates lizard! You lose! ")
            else:
                color_print("red", "rock crushes lizard! You lose! ")

        while True:
            try_again = input("Another round? (y/n): ")
            if try_again.lower() in ['y', 'n']:
                break
            color_print('red', 'You must select either y or n')
        if try_again.lower() == "y":
            continue
        elif try_again.lower() == "n":
            color_print("white", "HA HA HA I thought so!")
            break


if __name__ == '__main__':
    main()
