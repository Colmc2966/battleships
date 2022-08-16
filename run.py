# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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
    pass

def user_guesses():
    pass

def game_tracker():
    pass

create_ship_locations()
turns = 6

