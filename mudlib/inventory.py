# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/inventory.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


## Each container is a dictionary with the item uuid as key and the
## item quantity as value. 

## knapsack     = consumables and reagents
## satchel      = quest items 
## tradekit     = tradeskill items
## backpack     = everything else


## Equipt items are a dictionary of slot names and the uuid of the item
## in that slot, or None for empty slots
## equipment = {}

## Slots:
## head, face, neck, chest, arms, wrists, hands, legs, feet
## ring1, ring2, ear1, ear2
## primary_hand, off_hand

#-------------------------------------------------------------------------Count

def count(bag, item):

    """
    Returns the number of a given item in a bag.
    """

    return bag.get(item,0)


#--------------------------------------------------------------------------Stow

def stow(bag, item, count=1):

    """
    Add one or more of the same items to a container.
    """

    current = bag.get(item, 0)
    bag[item] = current + count


#------------------------------------------------------------------------Remove

def unload(bag, item, count=1):

    """
    Withdraw one or more of the same items from a container.
    
    """ 

    current = bag.get(item, 0)
    if count < current:
        bag[item] = current - count

    else:
        print("Oddness -- attempt to remove more items than exist in bag")

