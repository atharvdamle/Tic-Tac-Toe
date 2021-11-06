# -------------------------------------------------------------------------------
### Tic Tac Toe ###
# -------------------------------------------------------------------------------
# A simple 2D array implementation of one of the most popular games, Tic Tac Toe.
# -------------------------------------------------------------------------------

board = [[0 for i in range(3)] for j in range(3)]
gamerunning = 1
turn = 'X'

def checkDiag(board):
    if board[0][0]=='X' and board[1][1]=='X' and board[2][2] == 'X':
        return 1
    elif board[0][2]=='X' and board[1][1]=='X' and board[2][0] == 'X':
        return 1
    elif board[0][2]=='O' and board[1][1]=='O' and board[2][0] == 'O':
        return -1
    elif board[0][0]=='O' and board[1][1]=='O' and board[2][2] == 'O':
        return -1
    else:
        return 0

def checkVert(board):
    if board[0][0]=='X' and board[1][0]=='X' and board[2][0] == 'X':
        return 1
    elif board[1][0]=='X' and board[1][1]=='X' and board[1][2] == 'X':
        return 1
    elif board[2][0]=='X' and board[2][1]=='X' and board[2][2] == 'X':
        return 1
    elif board[0][0]=='O' and board[1][0]=='O' and board[2][0] == 'O':
        return -1
    elif board[1][0]=='O' and board[1][1]=='O' and board[1][2] == 'O':
        return -1
    elif board[2][0]=='O' and board[2][1]=='O' and board[2][2] == 'O':
        return -1
    else:
        return 0

def checkHorz(board):
    if board[0][0]=='X' and board[0][1]=='X' and board[0][2] == 'X':
        return 1
    elif board[1][0]=='X' and board[1][1]=='X' and board[1][2] == 'X':
        return 1
    elif board[2][0]=='X' and board[2][1]=='X' and board[2][2] == 'X':
        return 1
    elif board[0][0]=='O' and board[0][1]=='O' and board[0][2] == 'O':
        return -1
    elif board[1][0]=='O' and board[1][1]=='O' and board[1][2] == 'O':
        return -1
    elif board[2][0]=='O' and board[2][1]=='O' and board[2][2] == 'O':
        return -1
    else:
        return 0

initial = int(input('Welcome! Do you wish to play?\n1.Yes!\n2.No..\n\n'))
if initial == 1:
    print(*board, sep='\n')
    while gamerunning == 1:
        row, col = map(int, input('Type row(space)col of the spot to put your mark on!\n').split())
        if board[row][col] != 0:
            print('Wrong input! Try Again.')
            continue
        elif turn == 'X':
            board[row][col] = 'X'
            turn = 'O'
        else:
            board[row][col] = 'O'
            turn = 'X'

        print(*board, sep='\n')

        if checkVert(board) == 1 or checkHorz(board) == 1 or checkDiag(board) == 1:
            print('X has won!\n\n')
            gamerunning = 0
        elif checkVert(board) == -1 or checkHorz(board) == -1 or checkDiag(board) == -1:
            print('O has won\n\n')
            gamerunning = 0
else:
    print('Goodbye!')
    exit()

