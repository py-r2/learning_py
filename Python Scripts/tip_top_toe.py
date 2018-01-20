''' Tip Top Toe game by Romeo Rauta '''
#from __future__ import print_function
#from ipython.display import clear_output
from random import randint

board = [' ']*10

def display_board(board):

#    clear_output()
    print '  | |'
    print ' ' + board[7] + '|' + board[8] + '|' + board[9]
    print '  | |'
    print "--------"
    print '  | |'
    print ' ' + board[4] + '|' + board[5] + '|' + board[6]
    print '  | |'
    print "--------"
    print '  | |'
    print ' ' + board[1] + '|' + board[2] + '|' + board[3]
    print '  | |'

# this function is randomly choosing which player is going to be first
def choose_first():
    if randint(0,1) == 0:
        return 'Player2'
    else:
        return 'Player1'

#this is where we assign a marker to each player
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input("Player1: Do you want to be X or O?").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#check the space at the specific position
def space_check(board,position):
    return board[position] == ' '

#verify if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#verify if the player has a win combination
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#placing marker on the right position
def place_marker(board, marker, position):
    board[position] = marker

#this is where we position players choice
def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position: (1-9)')
        return int(position)

#checking if the player wants to play again
def replay():
    return raw_input('Do you want to play again? Please answer with Y or N:').lower().startswith('y')


#here is where our main game code is running
print "Welcome to Tip Top Toe game."

while True:
#Reset the board.
    Player1_marker, Player2_marker = player_input()
    turn = choose_first()
    print turn + "will go first."
    game_on = True

    while game_on:
        #Player1's turn.
        if turn == 'Player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,Player1_marker,position)
            if win_check(board, Player1_marker):
                display_board(board)
                print "Congratulations! You have won the game!"
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print "The game is a draw!"
                else:
                    turn = 'Player2'

        else:
            #Player2's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board,Player2_marker,position)
            if win_check(board, Player2_marker):
                display_board(board)
                print "Congratulations! You have won the game!"
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print "The game is a draw!"
                else:
                    turn = 'Player1'

    if not replay():
        break
