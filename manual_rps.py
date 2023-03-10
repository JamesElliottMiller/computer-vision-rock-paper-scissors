
#This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
#Create another file called manual_rps.py that will be used to play the game without the camera.
#You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
#Create two functions: get_computer_choice and get_user_choice.
#The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
#The second function will ask the user for an input and return it.

import random

valid_inputs = ["Rock", "Paper", "Scissors"]
num_player_one_wins = 0
num_player_two_wins = 0

def get_computer_choice():
  computer_choice = random.choice(valid_inputs)
  return(computer_choice) 

def get_user_choice():
  user_choice = (input("player input"))
  return(user_choice)

while num_player_one_wins < 3 or num_player_two_wins < 3:
  x = (input("player 1 input"))
  y = (input("player 2 input"))
  if num_player_one_wins >= 3:
    print("Player 1 has won overall")
    break
  elif num_player_two_wins >= 3:
    print("Player 2 has won overall")
    break
  elif x not in valid_inputs or y not in valid_inputs:
    print("invalid input")
  elif x == y:
    print("it's a tie")
  elif (x == "Rock" and y == "Paper") or (x == "Paper" and y == "Scissors") or (x == "Scissors" and y == "Rock"):
    num_player_two_wins += 1
    print("Player 2 wins")
  else:
    num_player_one_wins += 1
    print("Player 1 wins")


print(f"Player One Final Score {num_player_one_wins}")
print(f"Player Two Final Score {num_player_two_wins}")