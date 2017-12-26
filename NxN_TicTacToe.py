# Alim Momin
# Tic Tac Toe
# Instructions:

def fillBoard(dimension):
  board = []
  for x in range(dimension*dimension):
    board.append("_")
  return board
def displayBoard(board, dimension):
  cnt = 1
  for r in range(dimension):
    for c in range(dimension):
      if board[(r*dimension)+c] == '_':
        print("%2d" % cnt, end = ' | ')
      else:
        print("%2.2s" % board[(r*dimension)+c], end= " | ")
      cnt += 1
    print()
def makeMove(board, move, token, dimension):
  if (move < 1) or (move > (dimension*dimension)):
    print("Move is out of range!")
    return False
  if board[move-1] != '_':
    print("That position is filled! Try again!")
    return False
  else:
    board[move-1] = token
    return True
def winner(board, token, dimension):
  return fullRow(board, token, dimension) or fullCol(board, token, dimension) or fullDiag(board, token, dimension)
def fullDiag(board, token, dimension):
  return fullDiag1(board, token, dimension) or fullDiag2(board, token, dimension)
def fullDiag1(board, token, dimension):
  i = 0
  while i < len(board):
    if board[i] != token:
      return False
    i += dimension+1
  return True
def fullDiag2(board, token, dimension):
  i = dimension-1
  while i < len(board)-1:
    if board[i] != token:
      return False
    i += dimension-1
  return True
def fullCol(board, token, dimension):
  for i in range(0,dimension):
    count = 0
    for c in range(0, len(board), dimension):
      if board[c+i] == token:
        count += 1
      if count == dimension:
        return True
  return False
def fullRow(board, token, dimension):
  for r in range(dimension):
    count = 0
    for c in range(dimension):
      if board[(r*dimension)+c] == token:
        count += 1
        if count == dimension:
          return True
    count = 0
  return False
def filled(board, dimension):
  for x in board:
    if x == '_':
      return False
  return True

def move(board, dimension, token):
    gameOver = False
    displayBoard(board, dimension)
    move = int(input("Enter a move for " + token + " (1-" + str(dimension*dimension) +"): "))
    print(move)
    if (move < 1) or (move > (dimension*dimension)):
        print("Move is out of range; try again.")
    else:
        if makeMove(board, move, token, dimension):
            if winner(board, token, dimension):
               print(token + " wins!")
               gameOver = True
            else:
                if filled(board, dimension):
                     print("Board is full! No winner!")
                     gameOver = True
                else:
                  if token == 'X':
                     token = 'O'
                  else:
                     token = 'X'
    return token, gameOver

def main():
    print("Play Tic-Tac-Toe!")
    dimension = int(input("What is the dimension of the board (3-12)? "))
    print(dimension)
    if (dimension < 3) or (dimension > 12):
        print("The dimension is out of range")
    else:
        board = fillBoard(dimension)
        token = 'X'
        gameOver = False
        while not gameOver:
            token, gameOver = move(board, dimension, token)
        displayBoard(board, dimension)

if __name__ == "__main__":
    main()
