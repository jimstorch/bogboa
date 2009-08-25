# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/inventory.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared

## Old notes:
## pouch        = consumables and reagents
## satchel      = quest items 
## kit          = tradeskill items
## backpack     = everything else
## bank         = anything

## Max encumbrance = str * 100

## Time for dropped items to vanish from floors
ITEM_DECAY = 10


#----------------------------------------------------------------------Wardrobe

class Wardrobe(object):

    """Paper Doll Class to manage worn items."""    

    ## What slots do we want to manage?
    slot_names = set(['head', 'ears', 'neck', 'shoulders', 'back', 'chest',
        'arms', 'wrists', 'hands', 'fingers', 'primary', 'secondary', 'waist',
        'legs', 'feet'])


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

    def describe(self):

        pass



#---------------------------------------------------------------------------Bag


class Bag(object):

    """
    Class for managing player carried items.
    """    

    def __init__(self):
        
        ## Start out with some beginner settings
        ## A 'new bag' simply improves on these values
        self.name = 'Apprentice Sack'       ## Displayed name
        self.burden = 0.0                   ## Current weight/mass
        self.limit = 50.0                   ## maxium allowed
        self.reduction = 0.0                ## magical burden reduction %
        ## Dict of Contents
        ##   key = item, value = count
        self.items = {}                     

    #--------------------------------------------------------------------Reduce

    def _reduce(self, burden):
        """Apply the reduction percent to a value"""
        return burden - ( burden * self.reduction )

    #------------------------------------------------------------------Contents

    def contents(self):
        """Return a string listing the contents."""
        s = ''
        for items in self.items.keys():
            qty = self.items[item]
            s+='%-40s,%d\n\n' % (item.name, qty)
        return s 

    #------------------------------------------------------------------Can Hold

    def can_hold(self, item, qty=1):
        """Test if container can hold qty number of item."""
        total = self.burden + self._reduce(item.burden * qty)
        if total > 32000:
            return False
        else:
            return bool( total <= self.limit )

    #---------------------------------------------------------------------Count

    def count(self, item):
        """Return the quantity of Item."""
        return self.items.get(item, 0)
   
    #-----------------------------------------------------------------------Has    

    def has(self, item, qty=1):
        """Test if container has given quantity of Item."""
        curr = self.count(item)
        return bool(qty <= curr)    

    #-----------------------------------------------------------------------Add

    def add(self, item, qty=1):
        """Add given quantity of Item to container and increase burden."""
        curr = self.count(item)
        self.items[item] = curr + qty
        self.burden += _self.reduce( item.burden * qty )

    #------------------------------------------------------------------Subtract
                        
    def subtract(self, item, qty=1):
        """Remove given quantity of Item from container and reduce burden."""
        curr = self.count(item)
        if curr == qty:
            ## Don't maintain empty mappings
            del self.items[item]
        else:
            remaining = curr - qty
            self.items[item] = remaining
            self.burden -= _self.reduce( item.burden * qty)


#-------------------------------------------------------------------------Floor

class Floor(object):

    """Container where items vanish after DECAY_TIME seconds."""

    def __init__(self):
        self.burden = 0.0                   ## Current weight/mass        
        self.limit = 1000.0                 ## Maximum weight/mass

        ## Dictionary of contents
        ##  key = item, 
        ##  value = tuple(count, timestamp)
        self.items = {}           

    #------------------------------------------------------------------Can Hold

    def can_hold(self, item, qty=1):
        """Test if container can hold qty number of item."""
        total = self.burden + (item.burden * qty)
        return bool( total <= self.limit )


    #---------------------------------------------------------------------Clean

    def clean(self):
        """Housekeeping. Sweep away items older than ITEM_DECAY"""
        now = shared.THE_TIME
        is_cleaner = False
        for item in self.items.keys():
            qty, age = self.items[item]
            ## Is the item tuple older than decay time?
            if ( now - age ) > ITEM_DECAY:
                self.subtract(item, qty)
                is_cleaner = True
        return is_cleaner

    #------------------------------------------------------------------Contents

    def contents(self):
        """Return a string describing the contents."""
        s = ''
        for item in self.items.keys():
            qty, foo = self.items[item]
            s+='^Y%s^w (x%d)\n\n' % (item.name, qty)
        return s 

    #---------------------------------------------------------------------Count

    def count(self, item):
        """Return the quantity item."""
        if item in self.items:
            qty, foo = self.items[item]
        else:
            qty = 0
        return qty 

    #-----------------------------------------------------------------------Add

    def add(self, item, qty=1):
        """Add qty number of item to container and increase burden."""
        curr = self.count(item)
        ## Note that adding an existing item resets the timer for all
        self.items[item] = (curr + qty, shared.THE_TIME)
        self.burden += ( item.burden * qty )

    #------------------------------------------------------------------Subtract
                        
    def subtract(self, item, qty=1):
        """Remove qty number of item from container and decrease burden."""
        curr = self.count(item)
        if curr == qty:
            del self.items[item]
        else:
            left = curr - qty
            self.items[item] = (left, shared.THE_TIME)
        self.burden -= (item.burden * qty)


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



