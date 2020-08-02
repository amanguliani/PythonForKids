from turtle import *
import getpass

def turtle(x, y, color):
  turtle = Turtle()
  turtle.shape("turtle")
  turtle.color(color)
  turtle.speed(10)
  turtle .pu()
  turtle.goto(x, y)
  turtle.pd()
  return turtle

def init(hangman):
  screen = Screen()
  screen.setup(804, 608)
  hangman.fd(50)
  hangman.bk(25)
  hangman.left(90)
  hangman.fd(200)
  hangman.right(90)
  hangman.fd(70)
  hangman.right(90)
  hangman.fd(20)

def take_word(turtle):
  word_dict = {}
  my_word = getpass.getpass(" Enter your word for the other person to guess  ")

  for char in my_word:
    word_dict[turtle.pos()] = char
    turtle.pu()
    turtle.write("_", True, align="center", font=("Arial", 30, "normal"))
    turtle.fd(30)
    turtle.pd()
  return word_dict

def incorrect(turtle, attempt):
  if (attempt == 0):
    turtle.pu()
    cu = turtle.pos()
    turtle.goto(cu[0]-30, cu[1]-30)
    turtle.pd()
    turtle.circle(30)
    turtle.pu()
    turtle.goto(cu[0], cu[1]-60)
    turtle.pd()
  
  if (attempt == 1):
    turtle.fd(80)

  if (attempt == 2):
    turtle.bk(40)
    turtle.right(90)
    turtle.fd(25)

  if (attempt == 3):
    turtle.bk(50)
    turtle.pu()
    turtle.fd(25)
    turtle.left(90)
    turtle.fd(40)
    turtle.pd()
  
  if (attempt == 4):
    turtle.right(45)
    turtle.fd(25)

  if (attempt == 5):
    turtle.bk(25)
    turtle.left(90)
    turtle.fd(25)

def correct(turtle, word_dict, guess):
  total_guessed = 0 
  for pos, c in word_dict.items():
    if (c == guess):
      turtle.pu()
      turtle.goto(pos[0], pos[1])
      turtle.write(c, True, align="center", font=("Arial", 30, "normal"))
      total_guessed+=1
  return total_guessed

print ("Welcome to Hangman !!")
hangman = turtle(-250, -50, "black")
word = turtle(50, -50, "green")
init(hangman)
word_dict = take_word(word)

incorrect_guesses = 0
correct_guess = 0
guesses = []
while(correct_guess < len(word_dict.keys()) and incorrect_guesses < 6):
  print(guesses)
  character = input("Enter a character to guess ")
  if (len(character) != 1):
    print ("Please enter only one character to guess")
    continue;
  
  if (character in guesses):
    print ("You already guessed that")
    continue;

  if (character in word_dict.values()):
    correct_guess += correct(word, word_dict, character)
  else:
    incorrect(hangman, incorrect_guesses)
    incorrect_guesses += 1
  
  guesses.append(character)

final = turtle(0, -200, "red")
final.pu()
if (correct_guess == len(word_dict.keys())):
  final.write("You guessed it !!", True, align="center", font=("Arial", 30, "normal"))
elif (incorrect_guesses == 6):
  final.write("Sorry Chances are up !!", True, align="center", font=("Arial", 30, "normal"))
  