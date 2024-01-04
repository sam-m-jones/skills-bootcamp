
import random

# displayed the rules of the game
print ("""Welcome to the game of 'Rock, Paper, Scissors!"

Rules of play - scissors cuts paper, paper covers rock, and rock crushes scissors
""")

# requesting user input and generating random integer to represent opponent.
player = input("Please enter 'rock', 'paper', or 'scissors': ").upper().lower()
opponent = random.randint(1, 3)

# defined opponent options as variables.
num1 = "rock"
num2 = "scissors"
num3 = "paper"

# defined potential outcomes as variables.
win = "You win! Congratulations!"
draw = "It's a tie..."
lose = "You lose.  Comiserations."

while player == num1:
    if opponent == 1:
        print (f"{num1} cancels {num1} - {draw}")
    elif opponent == 2:
        print (f"{num2} covers {num1} - {lose}")
    elif opponent == 3:
        print (f"{num1} crushes {num3} - {win}")
    break

while player == num2:
    if opponent == 1:
        print (f"{num2} covers {num1} - {win}")
    elif opponent == 2:
        print (f"{num2} cancels {num2} - {draw}")
    elif opponent == 3:
        print (f"{num3} cuts {num2} - {lose}")
    break

while player == num3:
    if opponent == 1:
        print (f"{num1} crushes {num3} - {lose}")
    elif opponent == 2:
        print (f"{num3} cuts {num2} - {win}")
    elif opponent == 3:
        print (f"{num3} cancels {num3} - {draw}")
    break

# Logic Error - num2 and num3 need to be defined correctly
