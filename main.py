```py
import random

low = 1
high = 100
playerResponse = ''
randomNum = random.randint(low, high)
print("Please enter h, l, or y. h means the guess was too high. l means the guess was too low. y means the guess was correct.")
while playerResponse != "y":
    print ("Is it", randomNum, "?")

    playerResponse = input("Please enter h, l, or y. ")
    if playerResponse == "h":
        high = randomNum + 1
        randomNum = random.randint(low, high)
    elif playerResponse == "l":
        low = randomNum - 1
        randomNum = random.randint(low, high)
    elif playerResponse == "y":
        print("Ya! I found your number.")
        break
    else:
        print("Please answer with only l, h, or y.")```