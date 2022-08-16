# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

PLAYER_BOARD = [[' '] * 8 for x in range(6)] 
CPU_BOARD = [[' '] * 8 for x in range(6)]

guessing_code = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

def print_board(board):
    print('  A B C D E F ')
    print('  -----------')
    row_number = 1
    for row in board:
        print(row_number)
        row_number += 1

def create_ship_locations():
    for ship in range (3):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0-,5), randint(0,5)
        board[ship_row][ship_column] = 'X'

def user_guesses():
    row = input('Enter a ship row 1-5')
    while row not in '12345':
        print('Enter a valid ship row')
        row = input('Enter a ship row 1-5')
    column = input('Enter a ship column A-F').upper()
    while column not in 'ABCDEF':
        print('Enter a valid ship column')
        column = input('Enter a ship column A-F')
    return int(row) - 1, guessing_code[column]


def game_tracker():
    pass

create_ship_locations()
turns = 6

