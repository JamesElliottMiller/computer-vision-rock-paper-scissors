
#This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
#Create another file called manual_rps.py that will be used to play the game without the camera.
#You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
#Create two functions: get_computer_choice and get_user_choice.
#The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.
#The second function will ask the user for an input and return it.

#Using if-elif-else statements, 
#the script should now choose a winner based on the classic rules of Rock-Paper-Scissors.
#For example, if the computer chooses rock and the user chooses scissors, the computer wins.
#Wrap the code in a function called get_winner and return the winner.
#This function takes two arguments: computer_choice and user_choice.
#If the computer wins, the function should print "You lost", 
#if the user wins, the function should print "You won!", 
#and if it's a tie, the function should print "It is a tie!".

import random

def get_computer_choice():
  valid_inputs = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(valid_inputs)
  return(computer_choice) 

def get_user_choice():
 valid_inputs = ["Rock", "Paper", "Scissors"]
 while True:
    user_choice = (input("player input "))
    if user_choice not in valid_inputs:
     print("invalid input. Make sure your first letter is capitalised")
    else: 
     return(user_choice)

def get_winner(computer_choice, user_choice):
 if user_choice == computer_choice:
    print("It is a tie!")
 elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
    print("You won!")
 else:
    print("You lost")

get_winner(get_computer_choice(), get_user_choice())