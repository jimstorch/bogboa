# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/inventory.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from shared import find_item

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


from mudlib.shared import ITEMS

MAX_STACK = 100


#----------------------------------------------------------------------Wardrobe

class Wardrobe(object):

    """Paper Doll Class to manage worn items."""    

    ## What slots do we want to manage?
    slot_names = set('head', 'ears', 'neck', 'shoulders', 'back', 'chest',
        'arms', 'wrists', 'hands', 'fingers', 'primary', 'secondary', 'waist',
        'legs', 'feet')


    def __init__(self, body):

        self.body = body
        self.slots = {}

    #----------------------------------------------------------------Equip Item    

    def equip_item(self, item):
    
        """
        Given an item object, equip it in the proper slot.
        Also fires the on_equipt script.

        Returns None is slot is empty, the item replaced, or
        the origin item if not equipable.        
        """
        
        slot = item.slot
        if slot in self.slot_names:
                  
            replace = self.get_item(slot)
            self.slots[slot] = item
            ## TODO: dbms record
            return replace

        else:
            return item

    #------------------------------------------------------------------Get Item

    def get_item(self, slotname):
        
        """Return the item in a given slotname, or None for empty."""

        return self.slots.get(slotname, None)
        
    #----------------------------------------------------------------Equip UUID

    def equip_uuid(self, uuid):

        """Given a UUID, fill a slot with the corresponding item object."""        

        item = find_item[uuid]
        self.equip_item(item)

    #-------------------------------------------------------------Cascade Event

    def cascade_event(self, event, body):

        """Apply an event to all worn items to fire custom scripts."""
        
        pass

    #---------------------------------------------------------------Remove Item

    def remove_item(self, slot):

        pass

    #---------------------------------------------------------------Remove UUID

    def remove_uuid(self, uuid):
        
        pass   



#---------------------------------------------------------------------Container

class Container(object):

    def __init__(self, name, category, size):
        self.name = name
        self.category = category
        self.size = size
        self.contents = {}
        self.encumbrance = 0

    #----------------------------------------------------------------------Show

    def peruse(self, item_uuid=None):
        pass

    #----------------------------------------------------------------------Stow

    def stow(self, item_uuid, count=1):
        """Add one or more of the same items to a container."""
        current = self.contents.get(item_uuid, 0)
        self.contents[item_uuid] = current + count
        weight = ITEMS[item_uuid].weight * count
        self.ecumbrance += weight

    #--------------------------------------------------------------------Remove

    def remove(self, item_uuid, count=1)
        """Withdraw one or more of the same items from a container.""" 
        current = self.contents.get(item_uuid, 0)
        if count < current:
            self.contents[item_uuid] = current - count
            weight = ITEMS[item_uuid].weight * count
            self.ecumbrance -= weight

        else:
            print("Oddness -- attempt to remove more items than exist in bag")

    #------------------------------------------------------------------Can Stow

    def can_stow(self, item_uuid):
        """Boolean test whether item can go into this container."""        
        item = ITEMS[item_uuid]
        if self.category = 'any' or item.category == self.category:
            return True
        else:
            return False

    #------------------------------------------------------------------Too Many

    def too_many(self, item_uuid, count=1):
        """Boolean test whether too many of this item already held."""
        return ( self.count_item(item_uuid) + count ) >  MAX_STACK
           
    #----------------------------------------------------------------Count Item

    def count_item(self, item_uuid, count=1):
        """Returns the number of a given item in a bag."""
        return self.contents.get(item_uuid, 0)



#---------------------------------------------------------------------Equipment

class Equipment(object):

    def __init__(self):
        self.encumbrance = 0                

    def inspect(self, item_uuid=None):
        pass
    
    def wear(self, item_uuid):
        pass

    def remove(self, item_uuid):
        pass



#--------------------------------------------------------------------------Bank

class Bank(object):
    
    def __init__(self):
        pass

    def inquire(self, item_uuid=None):
        pass

    def deposit(self, item_uuid, count=1):
        pass

    def withdraw(self, item_uuid, count=1):
        pass



