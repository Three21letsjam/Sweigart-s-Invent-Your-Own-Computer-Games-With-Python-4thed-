#Tic Tac Toe

import random

def drawBoard(board):
    #prints out the board,

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    #Lets player choose their letter
    #returns list with the player's letter as the first and the computer's as the second

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
     # The first element in the list is the player's letter; the second if the cpu's
        if letter == 'X':
            return ['X','O']
        else:
            return['O','X']


def whoGoesFirst():
    # randomly choose which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
        board[move] = letter

def isWinner(bo, le):
    # given the board and player's letter, this returns true if player has won
    # bo == board le == letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):
     #makes a copy of the board and returns it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    #return true if the passed move is free on the board
    return board[move] == ' '

def getPlayerMove(board):
    #lets player enter move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #returns a valid move from the passed list on the passed board
    #returns none if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board, computerLetter):
    #given the board and computer's letter, determine where to move and return said move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Tic Tac Toe AI
    #checks to see if AI can win in next move
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i ):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    #checks to see if AI can block player from winning
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    #checks for AI to occupy a corner if able
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # checks for AI to occupy center if able
    if isSpaceFree(board, 5):
        return 5

    #Else move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #return true if the board is filled up, otherwise return false
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    #resets board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you. You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
                
