import random 
import time
num = random.randint(1, 101)
while True:
    print("Guess a number between 1 and 100")
    guess = input()
    i = int(guess)
    if i == num:
        print("You guessed right!")
        print("This window will close in 5 second now.")
        time.sleep(5)
        break
    elif i < num:
        print("Try Higher")
    elif i > num:
        print("Try lower")

