#import time
#import random
#
#while(True):
#    print(random.randrange(0,4))
#    time.sleep(1)

# Functionising the dice

#import time
#import random

#def binary_dice(num_dice):
#    return random.randrange(0,num_dice+1)
#
#while(True):
#    print(binary_dice(3))
#    time.sleep(1)

# I suspect this is modelling a single four sided dice (faces 0-3) like a d4 instead of the intended three binary dice.
# Create three binary dice

#import time
#import random
#
#while(True):
#    dice = []
#    num_dice = 3
#    die_outcomes = 2
#
#    for die_num in range(0,num_dice):
#        dice.append(random.randrange(0,die_outcomes))
#        print("{} = [{}]".format(die_num, dice[die_num]))
#    print("{}\n".format(sum(dice)))
#    time.sleep(1)

# Functionising the dice

#import time
#import random
#
#def binary_dice(num_dice):
#    dice = []
#    for die_num in range(0,num_dice):
#        dice.append(random.randrange(0,2))
#        print("{} = [{}]".format(die_num, dice[die_num]))
#    print("{}\n".format(sum(dice)))
#
#while(True):
#    binary_dice(3)
#    time.sleep(1)

# Classifying the code

import time
import random

class Dice(object):
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.dice = [0] * num_dice
        self.sum = 0

    def roll_dice(self):
        for die_num in range(0, self.num_dice):
            self.dice[die_num] = random.randrange(0,2)
        self.sum = sum(self.dice)

#hand_of_dice = Dice(3)
#while(True):
#    hand_of_dice.roll_dice()
#    for die_num in range(0, hand_of_dice.num_dice):
#        print("{} = [{}]".format(die_num, hand_of_dice.dice[die_num]))
#    print("Sum = {}\n".format(hand_of_dice.sum))
#    time.sleep(1)

#sum_stats = [0] * 4
#hand_of_dice = Dice(3)
#while(True):
#    hand_of_dice.roll_dice()
#    print("Sum = {}".format(hand_of_dice.sum))
#    sum_stats[hand_of_dice.sum] += 1
#    for stat in range(0, len(sum_stats)):
#        print("{} = [{}]".format(stat, sum_stats[stat]))
#    print("\n")
#    time.sleep(1)


sum_stats = [0] * 4
hand_of_dice = Dice(3)
for i in range(0, 100000):
    hand_of_dice.roll_dice()
    sum_stats[hand_of_dice.sum] += 1

for stat in range(0, len(sum_stats)):
    print("{} = [{}]".format(stat, sum_stats[stat]))
