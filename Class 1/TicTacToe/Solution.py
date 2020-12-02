from turtle import Turtle, Screen

screen = Screen()
screen.setup(804, 608)
t1 = Turtle()

tic_tac_toe_centers = {1: (-100, 100), 2: (0, 100), 3: (100, 100), 4: (-100, 0), 5: (0,0), 6: (100, 0), 7: (-100, -100), 8: (0, -100), 9: (100, -100)}

def draw_lines():
  #  Horizontal Line 1
  t1.pu()
  t1.goto(-150, 50)
  t1.pd()
  t1.fd(300)
  #  Horizontal Line 2
  t1.pu()
  t1.goto(-150, -50)
  t1.pd()
  t1.fd(300)
  #  Vertical Line 1
  t1.pu()
  t1.goto(-50, 150)
  t1.right(90)
  t1.pd()
  t1.fd(300)
  #  Vertical Line 2
  t1.pu()
  t1.goto(50, 150)
  t1.pd()
  t1.fd(300)
  t1.pu()
  t1.left(90)
  t1.goto(0,0)

def draw_circle(pos):
  t1.pu()
  p = tic_tac_toe_centers[pos]
  t1.goto(p[0], p[1]-40)
  t1.pd()
  t1.write("O", move=False, align="center", font=("Arial", 50, "normal"))
  t1.pu()

def draw_cross(pos):
  t1.pu()
  p = tic_tac_toe_centers[pos]
  t1.goto(p[0]-25, p[1]-40)
  t1.pd()
  t1.write("X", move=False, align="left", font=("Arial", 50, "normal"))
  t1.pu()

def check_rows(board):
  for row in board:
    if len(set(row)) == 1:
        return row[0]
  return -1

def check_columns(board):
  board2 = zip(*board)
  for row in board2:
    if len(set(row)) == 1:
        return row[0]
  return -1  

def check_diagnoals(board):
  if len(set([board[0][0], board[1][1], board[2][2]])) == 1 :
    print ("Main Diagonal")
    return board[0][0]
  elif len(set([board[0][2], board[1][1], board[2][0]])) == 1 :
    print ("Other Diagonal")
    return board[0][2]
  else: 
    return -1

def hasWon(board):
  r = check_rows(board)

  if r == -1:
    c = check_columns(board)
    if c == -1:
      return check_diagnoals(board)
    else:
      return c
  else:
    return r

values = [[-1,-1, -1],[-1,-1,-1],[-1,-1,-1]]

players = ["o", "x"]
turn = "p"

while(turn not in players):
  turn = input("Which one would you like to choose ? [x or o] :     ")
  turn = turn.lower()
  if (turn not in players):
    print("Not an accepted value, enter again")

draw_lines()

filled = 0
while filled < 9:
  position = int(input("{}'s turn, choose a number from 1-9 to play:  ".format(turn)))
  row = int((position-1) / 3)
  coloumn = int((position-1) % 3)
  if (position > 0 and position < 10 and values[row][coloumn] == -1):
    if (turn == "o"):
      draw_circle(position)
      values[row][coloumn] = 0
    else:
      draw_cross(position)
      values[row][coloumn] = 1
    
    won = hasWon(values)
    if (won == -1):
      turn = players [(players.index(turn) + 1) % 2]
      filled += 1
    else:
      print ("Game over {} won !".format(players[won]))
      break
  else:
    print ("invalid position for your turn")
    continue

if (filled == 9):
  print ("Game Draw !")