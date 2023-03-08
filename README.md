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