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
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ship_locations(board):
    for ship in range(6):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] = 'X'


def user_guesses():
    row = input('Enter a ship row 1-6')
    while row not in '12345':
        print('Enter a valid ship row')
        row = input('Enter a ship row 1-6')
    column = input('Enter a ship column A-F').upper()
    while column not in 'ABCDEF':
        print('Enter a valid ship column')
        column = input('Enter a ship column A-F')
    return int(row) - 1, guessing_code[column]


def game_tracker(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ship_locations(PLAYER_BOARD)
turns = 8
while turns > 0:
    print('Enjoy your game of Battleship')
    print_board(CPU_BOARD)
    row, column = user_guesses()
    if CPU_BOARD[row][column] == '-':
        print('Row or Column has already been guessed')
    elif PLAYER_BOARD[row][column] == 'X':
        print('You have hit a battleship')
        CPU_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You missed the battlehsips')
        CPU_BOARD[row][column] = '-'
        turns -= 1
    if game_tracker(CPU_BOARD) == 6:
        print('You sunk all the battleships! Well done')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('You have no turns remaining. The game is over')
        break
