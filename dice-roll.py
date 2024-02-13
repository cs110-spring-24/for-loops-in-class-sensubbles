### 2: Dice Roll

#In the `dice-roll.py` file, we will write some code to accomplish the following:

#1. Let’s simulate roll 100 dice and print out each dice value

import random

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

for roll in range(0, 100):
    dice = random.randint(1,6)
    if dice == 1:
        print("you rolled a 1")
        ones += 1
    elif dice == 2:
        print("you rolled a 2")
        twos += 1
    elif dice == 3:
        print("you rolled a 3")
        threes += 1
    elif dice == 4:
        print("you rolled a 4")
        fours += 1
    elif dice == 5:
        print("you rolled a 5")
        fives += 1
    elif dice == 6:
        print("you rolled a 6")
        sixes += 1

#2. Now, let’s count how many 1s, 2s, 3s, 4s, 5s, and 6s were rolled

print(f"After 100 dice rolls, we rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s")
