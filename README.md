# Computer Vision RPS

## The Project

So in this project my goal is going to be to create a programme which allows you to play rock paper scissors using webcam. Utilising a teachable modelling programme, I'm going to train the model how to look at different hand positions to read what gesture the user is pulling. After that I'll incorporate multiple rounds of play and determine who the winner is of a game.

## First Steps

So as a part of this computer vision project I've firstused https://teachablemachine.withgoogle.com/train/image to make an image recognition model recognising 4 different states:

1. Rock (Hands in a balled up position)

2. Paper (Palm flat, fingers pointed out)

3. Scissors (index and middle fingers extender, else balled fist)

and
4. Nothing (no hands in shot)

I've exported this data into a labels and keras model h5 file.

## Next Step: Enviroment 

So in order to integrate the Keras model I've included a python file which can read the keras model data. When the code is run, given a web cam integration, a new window appears with web cam open and begins intepretting the data on the catergories previously stated in an array format. On this Array we get values between 0-1 for each of our catergories (in order) to represent a percentage confidennce that this image matches the catergories previous trained; the closer to zero being more unlikly to be within that catergory and with values closer to 1 being entirly likely to within the catergory.

To do this we had import numpy, opencv-python and tenderflow to be able to intrepet this data and make sure the version of python being used was able to integrate with these models. As a result we're currently using 3.9.16.

## Next Step: Setting up Rock-Paper-Scissors Concept

I've defined some basic functions to play a game of Rock Paper Scissors in a computer vs user format.

For the computer I've defined a list of basic valid inputs from which is can choose from and then used a randomiser to select one of these options when playing:

```
def get_computer_choice():
  valid_inputs = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(valid_inputs)
  return(computer_choice) 

```

For the user, I've taken their input but then additional had a check against that same list to make sure that the input is also from that list. If not they need to type it in again and a message is displayed asking them to consider capitalisation of the word as I assume this would be a common error. And as addition I've added it in a while loop so that the user is prompted to reinput until they have a correct selection. 

This will be easy to adjust later

```

def get_user_choice():
 valid_inputs = ["Rock", "Paper", "Scissors"]
 while True:
    user_choice = (input("player input "))
    if user_choice not in valid_inputs:
     print("invalid input. Make sure your first letter is capitalised")
    else: 
     return(user_choice)

```

Following this I've created a basic set up of the game, defining a win, tie and lose condition for the user playing.
I've encapuslated this in a get_winner function.

```

def get_winner(computer_choice, user_choice):
 if user_choice == computer_choice:
    print("It is a tie!")
 elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
    print("You won!")
 else:
    print("You lost")

```

Finally, I've added all this into a higher level function which takes all three functions into one group called play

`def play():
  get_winner(get_computer_choice(), get_user_choice())`
