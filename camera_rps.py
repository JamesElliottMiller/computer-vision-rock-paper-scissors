import time #I need a count down of 7 seconds
import cv2
from keras.models import load_model
import numpy as np
import random

model = load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_computer_choice():
  valid_inputs = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(valid_inputs)
  print(computer_choice)
  return(computer_choice) 

def get_user_choice():
    user_choice = get_prediction()
    print(f'you chose {user_choice}')
    return(user_choice)

def get_winner(computer_choice, user_choice):
 if user_choice == computer_choice:
    print("It is a tie!")
    return "It is a tie"
 elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
    print("You won!")
    return "user_wins"
 else:
    print("You lost")
    return "computer_wins"

def play():
  user_wins = 0
  computer_wins = 0
  while user_wins < 3 or computer_wins < 3:
    if user_wins == 3:
        print("User has won overall")
        print(f"User Final Score {user_wins}")
        print(f"Computer Final Score {computer_wins}")
        break
    elif computer_wins == 3:
        print("Computer has won overall")
        print(f"User Final Score {user_wins}")
        print(f"Computer Final Score {computer_wins}")
        break
    result = get_winner(get_computer_choice(), get_user_choice())
    if result == "it is a tie":
        continue
    elif result == "user_wins":
         user_wins += 1
    else:
         computer_wins += 1
   

def get_prediction():
  Model_Catergory_Order = ["Rock", "Paper", "Scissors", "Nothing"]
  max_value_of_array_index = np.argmax(camera_read())
  return Model_Catergory_Order[max_value_of_array_index]

def camera_read():
    start = time.time()
    cap = cv2.VideoCapture(0)
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
        if cv2.waitKey(1) & 0xFF == ord('q') or time.time() > start+7:
         break      
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction

play()


