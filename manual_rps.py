
#This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
#Create another file called manual_rps.py that will be used to play the game without the camera.
#You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
#Create two functions: get_computer_choice and get_user_choice.
#The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
#The second function will ask the user for an input and return it.

import random

def get_computer_choice():
  valid_inputs = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(valid_inputs)
  return(computer_choice) 

def get_user_choice():
  user_choice = (input("player input"))
  return(user_choice)
