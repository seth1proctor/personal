import turtle
# Tic Tac Toe Board
turtle.speed(10)
turtle.left(90)
turtle.forward(300)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.forward(300)
turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.setheading(180)
turtle.forward(300)
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.setheading(180)
turtle.forward(300)
turtle.penup()
turtle.goto(0,0)


global gameIsStillGoing 

Winner = None

playerOne = "X"

playerTwo = "O"

currPlayer = None


# Start of the Game
# Ask if they want x or o

# Make functions for making x's and o's
def drawX(x,y):

  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.setheading(60)

  for i in range(2):
    turtle.forward(50)
    turtle.backward(100)
    turtle.forward(50)
    turtle.left(60)

def drawO(x,y):

  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.setheading(0)
  turtle.circle(45)



def printBoard(board):
  
  for i in range(len(board)):
    line = ""
    if i == 1 or i == 2:
      print("-"*10)

    for j in range(len(board[i])):
      if j == 0 or j == 1:
        line += str(board[i][j]) + " | "
      else:
        line += str(board[i][j]) + " "

    print(line)
  return

board= [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  ]

def playGame():
  printBoard(board)

  display_board()
  checkIfGameOver()
  5

  while gameIsStillGoing:

    playerOneTurn(playerOne)

    checkIfGameOver()

    if gameIsStillGoing:
        playerTwoTurn(playerTwo)

    checkIfGameOver()

   
boardTwo = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
  print('')
  print(boardTwo[0:3])
  print(boardTwo[3:6])
  print(boardTwo[6:9])
  positions = [1,2,3,4,5,6,7,8,9]

  return 


def playerOneTurn(player):
  global currPlayer
  currPlayer = 'X'
  print("")

  print(" X's turn.")
  
  print("")

  userInput = giveValidInput('0')

  userInput = int(userInput) - 1
  boardTwo[userInput] = player
  display_board()
  




def playerTwoTurn(player):
  global currPlayer
  currPlayer = 'O'

  print("")

  print(" O's turn.")
  
  print("")

  userInput = giveValidInput('1')

  userInput = int(userInput) - 1
  boardTwo[userInput] = player
  display_board()




def checkIfGameOver():
  checkForWinner()

  if gameIsStillGoing == False: 

    if currPlayer == 'X':
      print("X Won!")
    elif currPlayer == 'O':
      print("O Won!")
    
    print("Game Over")
      

def checkForWinner():
    global gameIsStillGoing
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonals()
    
    if rowWinner:
        Winner = rowWinner
    elif columnWinner:
        Winner = columnWinner
    elif diagonalWinner:
        Winner = diagonalWinner
    else:
        gameIsStillGoing = True
        Winner = None

    return Winner
  
def checkRows():

    global gameIsStillGoing

    if boardTwo[0] == boardTwo[1] == boardTwo[2] != '-':
        gameIsStillGoing = False
        return boardTwo[0]
    elif boardTwo[3] == boardTwo[4] == boardTwo[5] != '-':
        gameIsStillGoing = False
        return boardTwo[3]
    elif boardTwo[6] == boardTwo[7] == boardTwo[8] != '-':
        gameIsStillGoing = False
        return boardTwo[6]
    else:
        return None

def checkColumns():
  
  global gameIsStillGoing
  if boardTwo[0] == boardTwo[3] == boardTwo[6] != '-':
    gameIsStillGoing = False
    return boardTwo[0]
  elif boardTwo[1] == boardTwo[4] == boardTwo[7] != '-':
    gameIsStillGoing = False
    return boardTwo[1]
  elif boardTwo[2] == boardTwo[5] == boardTwo[8] != '-':
    gameIsStillGoing = False
    return boardTwo[2]
  else:
    return None

def checkDiagonals():
  
  global gameIsStillGoing
  if boardTwo[0] == boardTwo[4] == boardTwo[8] != '-':
    gameIsStillGoing = False
    return boardTwo[0]
  elif boardTwo[6] == boardTwo[4] == boardTwo[2] != '-':
    gameIsStillGoing = False
    return boardTwo[6]
  else:
    return None
  
def giveValidInput(player):
    
    if(player == '1'):
       turn = 'O'
    else:
        turn = 'X'

    userInput = input("Where would you like to place the " + turn +  ". Choose 1-9. ")

    while not userInput.isnumeric() or checkForSameLoc(userInput):
        print("Please choose a number between that has not been picked")
        userInput = (input("Where would you like to place the " + turn +  ". Choose 1-9. "))

    intInput = int(userInput)

    if turn == 'X':
        if intInput == 1:
            drawX(-50,250)
        elif intInput == 2:
            drawX(50,250)
        elif intInput == 3:
            drawX(150,250)
        elif intInput == 4:
            drawX(-50,150)
        elif intInput == 5:
            drawX(50,150)
        elif intInput == 6:
            drawX(150,150)
        elif intInput == 7:
            drawX(-50,50)
        elif intInput == 8:
            drawX(50,50)
        elif intInput == 9:
            drawX(150,50)
    elif turn == 'O':
        if intInput == 1:
            drawO(-50,200)
        elif intInput == 2:
            drawO(50,200)
        elif intInput == 3:
            drawO(150,200)
        elif intInput == 4:
            drawO(-50,100)
        elif intInput == 5:
            drawO(50,100)
        elif intInput == 6:
            drawO(150,100)
        elif intInput == 7:
            drawO(-50,0)
        elif intInput == 8:
            drawO(50,0)
        elif intInput == 9:
            drawO(150,0)

    return userInput

def checkForSameLoc(input):
        actInput = int(input) - 1
        if (boardTwo[actInput] != '-'):
            return True
        else:
            return False



playGame()


