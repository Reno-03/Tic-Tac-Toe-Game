# tictactoe board using chessboard variables
import time
import random


def main():
    # setting board values using dictionary
    chessboard_dict = {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

    # game conditions for X and O players and returns X or O respectively
    def game_conditions():
        if chessboard_dict['top-L'] == "X" and chessboard_dict['top-M'] == "X" and chessboard_dict['top-R'] == "X":
            return "X"
        elif chessboard_dict['mid-L'] == "X" and chessboard_dict['mid-M'] == "X" and chessboard_dict['mid-R'] == "X":
            return "X"
        elif chessboard_dict['low-L'] == "X" and chessboard_dict['low-M'] == "X" and chessboard_dict['low-R'] == "X":
            return "X"
        elif chessboard_dict['top-L'] == "X" and chessboard_dict['mid-L'] == "X" and chessboard_dict['low-L'] == "X":
            return "X"
        elif chessboard_dict['top-M'] == "X" and chessboard_dict['mid-M'] == "X" and chessboard_dict['low-M'] == "X":
            return "X"
        elif chessboard_dict['top-R'] == "X" and chessboard_dict['mid-R'] == "X" and chessboard_dict['low-R'] == "X":
            return "X"
        elif chessboard_dict['top-L'] == "X" and chessboard_dict['mid-M'] == "X" and chessboard_dict['low-R'] == "X":
            return "X"
        elif chessboard_dict['top-R'] == "X" and chessboard_dict['mid-M'] == "X" and chessboard_dict['low-L'] == "X":
            return "X"

        elif chessboard_dict['top-L'] == "O" and chessboard_dict['top-M'] == "O" and chessboard_dict['top-R'] == "O":
            return "O"
        elif chessboard_dict['mid-L'] == "O" and chessboard_dict['mid-M'] == "O" and chessboard_dict['mid-R'] == "O":
            return "O"
        elif chessboard_dict['low-L'] == "O" and chessboard_dict['low-M'] == "O" and chessboard_dict['low-R'] == "O":
            return "O"
        elif chessboard_dict['top-L'] == "O" and chessboard_dict['mid-L'] == "O" and chessboard_dict['low-L'] == "O":
            return "O"
        elif chessboard_dict['top-M'] == "O" and chessboard_dict['mid-M'] == "O" and chessboard_dict['low-M'] == "O":
            return "O"
        elif chessboard_dict['top-R'] == "O" and chessboard_dict['mid-R'] == "O" and chessboard_dict['low-R'] == "O":
            return "O"
        elif chessboard_dict['top-L'] == "O" and chessboard_dict['mid-M'] == "O" and chessboard_dict['low-R'] == "O":
            return "O"
        elif chessboard_dict['top-R'] == "O" and chessboard_dict['mid-M'] == "O" and chessboard_dict['low-L'] == "O":
            return "O"

    # input validator to check whether the user-made input is valid
    # for the game
    def input_validator(data):
        if data not in chessboard_dict.keys():
            print('\ninvalid input...')
            time.sleep(0.6)
            return 1

        elif chessboard_dict[data] != ' ':
            print('\nthere\'s already a value...')
            time.sleep(0.6)
            return 1

    # a function to print the board using the dictionary-based key and values
    def print_board():
        print('')
        print(f"{chessboard_dict['top-L']} | {chessboard_dict['top-M']} | {chessboard_dict['top-R']}")
        print('--+---+--')
        print(f"{chessboard_dict['mid-L']} | {chessboard_dict['mid-M']} | {chessboard_dict['mid-R']}")
        print('--+---+--')
        print(f"{chessboard_dict['low-L']} | {chessboard_dict['low-M']} | {chessboard_dict['low-R']}")

    # a function to print the guide board
    def guideBoard():
        print('This is the guide for choosing a place: \n')
        print(f"'top-L'|'top-M'|'top-R'")
        print('-------+-------+-----')
        print(f"'mid-L'|'mid-M'|'mid-R'")
        print('-------+-------+-----')
        print(f"'low-L'|'low-M'|'low-R'")

    # asks the user to deal a computer or player-controlled enemy
    def enemyIsComputerOrPlayer():
        if enemyIsAI == 'y':
            return True
        elif enemyIsAI == 'n':
            return False

    # checks every space to increse efficiency in selecting available
    # spaces of enemy
    def ticPlaces():
        for key, value in chessboard_dict.items():
            if value == "X" or value == "O":
                ticPlace.remove(key)

    # X player will be first
    X = True

    # main program
    enemyIsAI = input("\nEnemy as AI? (y/n) ").lower()
    enemyIsComputerOrPlayer()
    guideBoard()

    while True:
        # this is for enemy; to check available spaces
        ticPlace = ['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']

        # updates the board every turn
        print_board()
        time.sleep(0.4)

        # inputs the player's and enemies' turn (X and O alternate)
        if X:
            turn_x = input("choose a place (top/mid/low)-(L/M/R) for X: ")

            if input_validator(turn_x) == 1:
                continue 

            chessboard_dict[turn_x] = "X"
            X = False
        
        elif not X:
            ticPlaces() 

            if enemyIsComputerOrPlayer():
                turn_o = random.choice(ticPlace)
                
                if input_validator(turn_o) == 1:
                    continue 

                chessboard_dict[turn_o] = "O"
                X = True

            else:  
                turn_o = input("choose a place ((top/mid/low)-(L/M/R) for O: ")

                if input_validator(turn_o) == 1:
                    continue 

                chessboard_dict[turn_o] = "O"
                X = True   

        # if there's a winner either X or O, the loop breaks
        if game_conditions() == "X" or game_conditions() == "O":
            break

        # breaks the loop if the board is completed with values and
        # it's a tie
        numberOfOccupants = 0
        for value in chessboard_dict.values():
            if value != ' ':
                numberOfOccupants += 1
        
        if numberOfOccupants == 9:
            break

    # Final Result Board is printed
    print("\n" * 4)
    print("The final result board".upper().center(40, "-"))

    if game_conditions() == "X":
        print(">> X player is the winner")

    elif game_conditions() == "O":  
        print(">> O player is the winner")

    else:
        print("It's a tie! Try again")

    print_board()


if __name__ == '__main__':
    main()

