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

## Max encumbrance = str * 100

from mudlib.shared import ITEMS


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
        self.encumbrance = 0


    #----------------------------------------------------------------Equip UUID

    def equip_uuid(self, uuid):

        """Given a UUID, fill a slot with the corresponding item object."""        

        item = find_item[uuid]
        self.equip_item(item)

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

    #--------------------------------------------------------------------------

    def describe(self)

        pass



class Container(object):

    def __init__(self, max_stacks=20, max_height=2000):
        
        self.max_stacks = max_stacks    ## Maximum count of item stacks
        self.max_height = max_height    ## Maximum items in each stack
        self.items = {}

    def can_hold(self, item, qty=1):

        """Test if container can hold qty number of item."""

        curr= self.count(item)
        ## Do we have a stack begun and can it hold more?
        if curr > 0 and (curr + qty) < self.max_height:
            return = True
        ## Do we have room for a new item stack?
        elif len(self.items) < self.max_stacks and qty < self.max_height:
            return True
        else:
            return False   

    def count(self, item):

        """Return the quantity item.  Qty 0 = no stack yet."""

        foo, curr = self.items.get(item.uuid,0)
        return curr        

    def has(self, item, qty=1):

        """Check it container has qty number of item."""

        curr = self.count(item)
        return bool(qty <= curr)    

    def add(self, item, qty=1):

        """Add qty number of item to container."""

        curr = self.count(item)
        self.items[item.uuid] = (item, curr + count)

                        

    def subtract(self, item, qty=1):
        curr = self.count(item)
        ## if we take all, delete the stack.
        ## Otherwise, it will count against max_items even with a count of 0
        if curr = qty:
            del self.items[item.uuid]
        else:
            self.items[item.uuid] = (item, qty - curr)


    #----------------------------------------------------------------Get Weight

    def Get Weight(self):
        wt = 0.0
        for uuid in self.items.keys():
            item, qty = self.items[uuid]
            wt += (item.weight * qty)
        return wt     









##---------------------------------------------------------------------Container

#class Container(object):

#    def __init__(self, name, category, size):
#        self.name = name
#        self.category = category
#        self.size = size
#        self.contents = {}
#        self.encumbrance = 0

#    #----------------------------------------------------------------------Show

#    def peruse(self, item_uuid=None):
#        pass

#    #----------------------------------------------------------------------Stow

#    def stow(self, item_uuid, count=1):
#        """Add one or more of the same items to a container."""
#        current = self.contents.get(item_uuid, 0)
#        self.contents[item_uuid] = current + count
#        weight = ITEMS[item_uuid].weight * count
#        self.ecumbrance += weight

#    #--------------------------------------------------------------------Remove

#    def remove(self, item_uuid, count=1)
#        """Withdraw one or more of the same items from a container.""" 
#        current = self.contents.get(item_uuid, 0)
#        if count < current:
#            self.contents[item_uuid] = current - count
#            weight = ITEMS[item_uuid].weight * count
#            self.ecumbrance -= weight

#        else:
#            print("Oddness -- attempt to remove more items than exist in bag")

#    #------------------------------------------------------------------Can Stow

#    def can_stow(self, item_uuid):
#        """Boolean test whether item can go into this container."""        
#        item = ITEMS[item_uuid]
#        if self.category = 'any' or item.category == self.category:
#            return True
#        else:
#            return False

#    #------------------------------------------------------------------Too Many

#    def too_many(self, item_uuid, count=1):
#        """Boolean test whether too many of this item already held."""
#        return ( self.count_item(item_uuid) + count ) >  MAX_STACK
#           
#    #----------------------------------------------------------------Count Item

#    def count_item(self, item_uuid, count=1):
#        """Returns the number of a given item in a bag."""
#        return self.contents.get(item_uuid, 0)



##--------------------------------------------------------------------------Bank

#class Bank(object):
#    
#    def __init__(self):
#        pass

#    def inquire(self, item_uuid=None):
#        pass

#    def deposit(self, item_uuid, count=1):
#        pass

#    def withdraw(self, item_uuid, count=1):
#        pass



