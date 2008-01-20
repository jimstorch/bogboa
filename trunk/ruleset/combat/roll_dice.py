#------------------------------------------------------------------------------
#   File:       dice_rolls.py
#   Purpose:
#   Author:     James Mynderse
#------------------------------------------------------------------------------

from random import randint

def d4():
    return roll_die(1,4)

def d6():
    return roll_die(1,6)

def d8():
    return roll_die(1,8)

def d10():
    return roll_die(1,10)

def d12():
    return roll_die(1,12)

def d20():
    return roll_die(1,20)

def roll_die(num_dice,num_sides):
    value = 0
    for die in range(0,num_dice):
        value = value + randint(1,num_sides)
    return value
