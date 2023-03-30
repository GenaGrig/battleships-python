import random
from random import randint

class GameBoard:
    def __init__(self, board):
        self.board = board

    def letters_to_numbers():
        letters_to_numbers = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E F G H")
        #print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

#computer create 5 ships
    def create_ships(self):
        for ship in range(5):
            self.x_row, self.y_column = random.randint(0,7), random.randint(0,7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0,7), random.randint(0,7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in "12345678":
                print('Not an appropriate choice, please select a valid row')
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('Not an appropriate choice, please select a valid column')
                y_column = input("Enter the column of the ship: ").upper()
            return int(x_row) - 1, GameBoard.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

#check if all ships are hit
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def RunGame():
    #Board for holding ship locations
    computer_board = GameBoard([[" "] * 8 for x in range(8)])
    # Board for displaying hits and misses
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    turns = 10
    while turns > 0:
        print('Welcome to Battleship game')
        print('Guess a battleship location')
        GameBoard.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.get_user_input(object)
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You guessed that one already.")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk one of my battleships!")
            user_guess_board.board[user_x_row][user_y_column] = "X"  
        else:
            print("MISS!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose    
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all 5 battleships and win!")
            break
        else:
            turns -= 1
        print(f"You have {turns} turns left")
        if turns == 0:
            print("Sorry!You ran out of turns!")
            print("Here are all battleships!")
            GameBoard.print_board(computer_board)
            break

if __name__ == '__main__':
    RunGame()