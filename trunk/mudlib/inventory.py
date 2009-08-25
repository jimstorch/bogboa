# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/inventory.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared

## Each container is a dictionary with the item uuid as key and the
## item quantity as value. 

## pouch        = consumables and reagents
## satchel      = quest items 
## kit          = tradeskill items
## backpack     = everything else
## bank         = anything

## Max encumbrance = str * 100

## Time for dropped items to vanish from floors
ITEM_DECAY = 30


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


#---------------------------------------------------------------------Container


class Container(object):

    """
    Then it occured to me, why am I worrying about stack sizes in a MUD?
    I should be counting mass.
    """    

    def __init__(self, name=None, limit= 500.0):
        
        self.name = name
        self.mass = 0.0
        self.limit = limit
        self.items = {}

    #------------------------------------------------------------------Contents

    def contents(self):
        s = ''
        for key in self.items.keys():
            item, qty = self.items[key]
            s+='%-40s,%d\n\n' % (item.name, qty)
        return s 


    #------------------------------------------------------------------Can Hold

    def can_hold(self, item, qty=1):

        """Test if container can hold qty number of item."""

        total = self.mass + (item.mass * qty)
        return bool( total <= self.limit )

    #---------------------------------------------------------------------Count

    def count(self, item):

        """Return the quantity item."""

        foo, qty = self.items.get(item.uuid, (None,0))
        return qty    

    #-----------------------------------------------------------------------Has    

    def has(self, item, qty=1):

        """Check it container has qty number of item."""

        curr = self.count(item)
        return bool(qty <= curr)    

    #-----------------------------------------------------------------------Add

    def add(self, item, qty=1):

        """Add qty number of item to container and adjust mass."""

        curr = self.count(item)
        self.items[item.uuid] = (item, curr + qty)
        self.mass += ( item.mass * qty )

    #------------------------------------------------------------------Subtract
                        
    def subtract(self, item, qty=1):

        """Remove qty number of item from container and adjust mass."""

        curr = self.count(item)
        if curr == qty:
            del self.items[item.uuid]
        else:
            left = curr - qty
            self.items[item.uuid] = (item, left)


#----------------------------------------------------------------TimedContainer   

class TimedContainer(Container):

    """Child Object of Container that has timed item decay, for rooms."""

    def init(self, name=None, limit=500.0):

        self.name = name
        self.mass = 0.0
        self.limit = limit
        self.items = {}           

    #---------------------------------------------------------------------Clean

    def clean(self):

        """Housekeeping.  Housekeeping.  I come in?"""

        uuids = self.items.keys()
        now = shared.THE_TIME
        for uuid in uuids:
            item, qty, age = self.items[uuid]
            ## Is the item tuple older than decay time?
            if ( now - age ) > ITEM_DECAY:
                self.subtract(item, qty)


    #------------------------------------------------------------------Contents

    def contents(self):
        self.clean()        
        s = ''
        for key in self.items.keys():
            item, qty, foo = self.items[key]
            s+='^Y%s^w (x%d)\n\n' % (item.name, qty)
        return s 

    #---------------------------------------------------------------------Count

    def count(self, item):

        """Return the quantity item."""

        foo, qty, bar = self.items.get(item.uuid, (None,0,None))
        return qty 

    #-----------------------------------------------------------------------Add


    def add(self, item, qty=1):

        """Add qty number of item to container and adjust mass."""

        curr = self.count(item)
        self.items[item.uuid] = (item, curr + qty, shared.THE_TIME)
        self.mass += ( item.mass * qty )
        print self.mass


    #------------------------------------------------------------------Subtract
                        
    def subtract(self, item, qty=1):

        """Remove qty number of item from container and adjust mass."""

        curr = self.count(item)
        if curr == qty:
            del self.items[item.uuid]
        else:
            left = curr - qty
            self.items[item.uuid] = (item, left, shared.THE_TIME)
        self.mass -= (item.mass * qty)
        print self.mass  

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



