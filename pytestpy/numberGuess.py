#from random import random


import random

tries = 0
try:
    maxnum = int(input("Please input the number (where the randomizer should stop) : "))
    guess = int(input("Whats your guess?\n:"))
except:
    try:
        maxnum = int(input("Your input was not a number, please input again: "))
        guess = int(input("Whats your guess?\n:"))
    except:
        print("qwwesdrftvygbujmok,l")
randnum = random.randrange(1, maxnum+1)

while True:
    tries+=1
    try:
        try:
            if maxnum < guess:
                guess = int(input("what is that number you idiot. try again: "))
        except:
            print("gtfo")
            break
        if guess > randnum:
            guess = int(input("Try Lower...\n:"))
        elif guess < randnum:
            guess = int(input("Try Higher...\n:"))
        elif guess == randnum:
            print(f"Congratulations,{tries} was your try count")
            break
    except:
        try:
            guess = int(input("what is that number you idiot. try again: "))
        except:
            print("fuk u!")