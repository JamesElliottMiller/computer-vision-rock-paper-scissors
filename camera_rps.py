import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

import random

def get_computer_choice():
  valid_inputs = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(valid_inputs)
  print(computer_choice)
  return(computer_choice) 

def get_user_choice():
    user_choice = get_prediction()
    print(user_choice)
    return(user_choice)

def get_winner(computer_choice, user_choice):
 if user_choice == computer_choice:
    print("It is a tie!")
 elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
    print("You won!")
 else:
    print("You lost")

def play():
  get_winner(get_computer_choice(), get_user_choice())

def get_prediction():
  Model_Catergory_Order = ["Rock", "Paper", "Scissors", "Nothing"]
  max_value_of_array_index = np.argmax(prediction)
  return Model_Catergory_Order[max_value_of_array_index]

play()
