# tictactoe board using chessboard variables
import time
import random


def main():
    # setting board values using dictionary
    board = {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

    # game conditions for X and O players and returns X or O respectively
    def game_conditions():
        if board['top-L'] == "X" and board['top-M'] == "X" and board['top-R'] == "X":
            return "X"
        elif board['mid-L'] == "X" and board['mid-M'] == "X" and board['mid-R'] == "X":
            return "X"
        elif board['low-L'] == "X" and board['low-M'] == "X" and board['low-R'] == "X":
            return "X"
        elif board['top-L'] == "X" and board['mid-L'] == "X" and board['low-L'] == "X":
            return "X"
        elif board['top-M'] == "X" and board['mid-M'] == "X" and board['low-M'] == "X":
            return "X"
        elif board['top-R'] == "X" and board['mid-R'] == "X" and board['low-R'] == "X":
            return "X"
        elif board['top-L'] == "X" and board['mid-M'] == "X" and board['low-R'] == "X":
            return "X"
        elif board['top-R'] == "X" and board['mid-M'] == "X" and board['low-L'] == "X":
            return "X"

        elif board['top-L'] == "O" and board['top-M'] == "O" and board['top-R'] == "O":
            return "O"
        elif board['mid-L'] == "O" and board['mid-M'] == "O" and board['mid-R'] == "O":
            return "O"
        elif board['low-L'] == "O" and board['low-M'] == "O" and board['low-R'] == "O":
            return "O"
        elif board['top-L'] == "O" and board['mid-L'] == "O" and board['low-L'] == "O":
            return "O"
        elif board['top-M'] == "O" and board['mid-M'] == "O" and board['low-M'] == "O":
            return "O"
        elif board['top-R'] == "O" and board['mid-R'] == "O" and board['low-R'] == "O":
            return "O"
        elif board['top-L'] == "O" and board['mid-M'] == "O" and board['low-R'] == "O":
            return "O"
        elif board['top-R'] == "O" and board['mid-M'] == "O" and board['low-L'] == "O":
            return "O"

    # input validator to check whether the user-made input is valid
    # for the game
    def input_validator(data):
        if data not in board.keys():
            print('\ninvalid input...')
            time.sleep(0.6)
            return 1

        elif board[data] != ' ':
            print('\nthere\'s already a value...')
            time.sleep(0.6)
            return 1

    # a function to print the board using the dictionary-based key and values
    def print_board():
        print('')
        print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
        print('--+---+--')
        print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
        print('--+---+--')
        print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")

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
        for key, value in board.items():
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

            board[turn_x] = "X"
            X = False
        
        elif not X:
            ticPlaces() 

            if enemyIsComputerOrPlayer():
                turn_o = random.choice(ticPlace)
                
                if input_validator(turn_o) == 1:
                    continue 

                board[turn_o] = "O"
                X = True

            else:  
                turn_o = input("choose a place ((top/mid/low)-(L/M/R) for O: ")

                if input_validator(turn_o) == 1:
                    continue 

                board[turn_o] = "O"
                X = True   

        # if there's a winner either X or O, the loop breaks
        if game_conditions() == "X" or game_conditions() == "O":
            break

        # breaks the loop if the board is completed with values and
        # it's a tie
        numberOfOccupants = 0
        for value in board.values():
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

