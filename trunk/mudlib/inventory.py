# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/inventory.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

## Each container is a dictionary with the item uuid as key and the
## item quantity as value. 

## pouch        = consumables and reagents
## satchel      = quest items 
## kit          = tradeskill items
## backpack     = everything else
## bank         = anything


## Equipt items are a dictionary of slot names and the uuid of the item
## in that slot, or None for empty slots
## equipment = {}

## Slots:
##  head, face, ear1, ear2
##  neck, shoulders, back, chest
##  arms, wrists, hands, finger1, finger2
##  waist, legs, feet
##  primary_hand, off_hand

MAX_STACK = 1000

#---------------------------------------------------------------------Container

class Container(object):

    def __init__(self, name, category, size):
        self.name = name
        self.category = category
        self.size = size
        self.contents = {}

    #------------------------------------------------------------------Can Stow

    def can_stow(self, item):
        """Boolean test whether item can go into this container."""        
        if self.category = 'any' or item.category == self.category:
            return True
        else:
            return False

    #------------------------------------------------------------------Too Many

    def too_many(self, item, count=1):
        """Boolean test whether too many of this item already held."""
        return ( self.count_item(item) + count ) >  MAX_STACK
           
    #----------------------------------------------------------------Count Item

    def count_item(self, item, count=1):
        """Returns the number of a given item in a bag."""
        return self.contents.get(item,0)

    #----------------------------------------------------------------------Stow

    def stow(self, item, count=1):
        """Add one or more of the same items to a container."""
        current = self.contents.get(item, 0)
        self.contents[item] = current + count

    #--------------------------------------------------------------------Remove

    def remove(self, item, count=1)
        """Withdraw one or more of the same items from a container.""" 
        current = self.contents.get(item, 0)
        if count < current:
            self.contents[item] = current - count

        else:
            print("Oddness -- attempt to remove more items than exist in bag")

    #----------------------------------------------------------------------Show

    def show(self):
        pass


#---------------------------------------------------------------------Equipment

class Equipment(object):

    def __init__(self):
                



#--------------------------------------------------------------------------Bank

class Bank(object):
    
    def __init__(self):
        pass



