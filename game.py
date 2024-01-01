from random import randint
from os import system, name

# list of possible options
play = ["rock", "paper", "scissors"]
# possible series lengths
possibleLen = [1, 3, 5, 7]


def main():
    # clearing the Screen
    clear()

    # get number of games to play
    series, victory = seriesLen()
    print(f"First to {victory} wins the game!")

    # set wins to 0
    human = int(0)
    opponent = int(0)

    # play the game(s) while nobody has won the series
    while human != victory and opponent != victory:
        
        # print how many games have been won
        print(f"Your Wins: {human}\nComputer's Wins: {opponent}")
        
        # get input from player
        player = playerInput()
        
        # computer sets random play
        computer = computerPlay()

        # show computer play
        print(f"Computer plays: {computer}")
        
        # play the game(s) while nobody has won the series
        if player == computer:
            print("Tie! Play again.")
        elif player != computer and player == "rock":
            if computer == "scissors":
                print("You win! Rock crushes scissors")
                human += 1
            elif computer == "paper":
                print("You lose! Paper covers rock")
                opponent += 1
        elif player != computer and player == "scissors":
            if computer == "paper":
                print("You win! Scissors cut paper.")
                human += 1
            elif computer == "rock":
                print("You lose! Rock crushes scissors")
                opponent += 1
        elif player != computer and player == "paper":
            if computer == "scissors":
                print("You lose! Scissors cuts paper")
                opponent += 1
            elif computer == "rock":
                print("You win! Paper covers rock")
                human += 1
    
    # print winner of series
    if human == victory:
        print(f"You won the {series} game series with {victory} wins! Congratulations!")
        return 0
    if opponent == victory:
        print(f"You lost the {series} game series with {victory} wins. Better luck next time.")
        return 0


def seriesLen():
    # how many games will be played?
    while True:
        try:
            noBracket = ", ".join(map(str, possibleLen))
            series = int(input(f"Would you like to play best of {noBracket}? "))
            if series in possibleLen:
                victory = int((series + 1) / 2)
                return series, victory
            # if ineligible input, repeat question
            else:
                print(f"Input must be {noBracket}")
                True
        except ValueError:
            print(f"Input must be {noBracket}")
            True


def computerPlay():
    # randomize what computer plays
    computer = play[randint(0, 2)]
    return computer


def playerInput():
    # get input from player
    while True:
        player = input("rock, paper, or scissors? ")
        if player in play:
            return player
        else:
            #if ineligible input, repeat question
            print('Input must be "rock", "paper", or "scissors"')
            True


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


main()
