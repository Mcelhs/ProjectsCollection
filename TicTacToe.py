# Tic-Tac-Toe version 2
# by Sean
# Created: July 12, 2021

# What we finished so far:
# - Display the game board
# - Logic and winning conditions (except tie)
# - Main game loop

# What we need to-do:
# - Tie

import sys

# Create game cells
list = [' ' for n in range(10)]

def displayBoard():
    # Printing the game board
    print()
    print(f'\t {list[1]} | {list[2]} | {list[3]}')
    print('\t-----------')
    print(f'\t {list[4]} | {list[5]} | {list[6]}')
    print('\t-----------')
    print(f'\t {list[7]} | {list[8]} | {list[9]}')
    print()

def playBoard(pos, pl):
    # Position the play in the cell and check for already-placed cells
    try:
        if list[pos] != 'X' and list[pos] != 'O':
            list[pos] = pl.upper()
    except IndexError:
        print('Try again. Space out of board range 1 to 9.')

def scoreGame():
    # Coniditions for winning
    O_ROW = (
        (list[1] == 'O' and list[2] == 'O' and list[3] == 'O') or
        (list[4] == 'O' and list[5] == 'O' and list[6] == 'O') or
        (list[7] == 'O' and list[8] == 'O' and list[9] == 'O')
    )
    O_COL = (
        (list[1] == 'O' and list[4] == 'O' and list[7] == 'O') or
        (list[2] == 'O' and list[5] == 'O' and list[8] == 'O') or
        (list[3] == 'O' and list[6] == 'O' and list[9] == 'O')
    )
    X_ROW = (
        (list[1] == 'X' and list[2] == 'X' and list[3] == 'X') or
        (list[4] == 'X' and list[5] == 'X' and list[6] == 'X') or
        (list[7] == 'X' and list[8] == 'X' and list[9] == 'X')
    )
    X_COL = (
        (list[1] == 'X' and list[4] == 'X' and list[7] == 'X') or
        (list[2] == 'X' and list[5] == 'X' and list[8] == 'X') or
        (list[3] == 'X' and list[6] == 'X' and list[9] == 'X')
    )
    O_DIAG = (
        (list[1] == 'O' and list[5] == 'O' and list[9] == 'O') or
        (list[3] == 'O' and list[5] == 'O' and list[7] == 'O')
    )
    X_DIAG = (
        (list[1] == 'X' and list[5] == 'X' and list[9] == 'X') or
        (list[3] == 'X' and list[5] == 'X' and list[7] == 'X')
    )

    if O_ROW or O_COL or O_DIAG:
        print('O Wins!')
        sys.exit()
    elif X_ROW or X_COL or X_DIAG:
        print('X Wins!')
        sys.exit()


print('''Welcome to the game of Tic-Tac-Toe.
You will pick a play (X or O) and then pick from a place of 1 to 9 on
the board. Let's begin
''')

# Game loop
while True:
    plays = input('Play X or O? ')

    if plays.lower() != 'x' and plays.lower() != 'o' and plays.lower() != 'q':
        print('We want an X or O')
        continue
    elif plays.lower() == 'q':
        sys.exit()

    pos = int(input('Letter position (1-9): '))

    playBoard(pos, plays)
    displayBoard()
    scoreGame()
