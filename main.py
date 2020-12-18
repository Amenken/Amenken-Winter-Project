
import random
import time

debug = 0

def playerReset():

    global low
    global high
    global playerResponse
    global randomNum
    
    low = 1
    high = 100
    playerResponse = ''
    randomNum = random.randint(low, high)

def startNow():
    
    global low
    global high
    global playerResponse
    global randomNum
    
    print("Please enter h, l, or y. h means the guess was too high. l means the guess was too low. y means the guess was correct.")
    print("-----")
    if debug == 1:
        print(playerResponse)
        print(low)
        print(high)
        print(randomNum)
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
            time.sleep(0.5)
            playAgain = input("Would you like to play again? y / n ")
            if playAgain == "y":
                print("-----")
                time.sleep(0.1)
                playerReset()
                startNow()
            else:
                print("Goodbye")
        else:
            print("Please answer with only l, h, or y.")
            
playerReset()
startNow()
