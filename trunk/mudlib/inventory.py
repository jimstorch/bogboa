# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/inventory.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.error import BogCmdError
from mudlib import shared

## Old notes:
## pouch        = consumables and reagents
## satchel      = quest items
## kit          = tradeskill items
## backpack     = everything else
## bank         = anything


## Time for dropped items to vanish from floors
_ITEM_DECAY = 300

## Maximum permitted stack size for any item, including coins.
_MAX_STACK_SIZE = 99999999

## Defined wear slots for equipable weapons, armor, and jewelry.
_WEAR_SLOTS = set(['head', 'face', 'ears', 'neck', 'shoulders', 'back',
        'chest', 'arms', 'wrists', 'hands', 'fingers', 'primary', 'secondary',
        'waist', 'legs', 'feet'])


#======================================================================Wardrobe

class Wardrobe(object):

    """Paper-doll Class to manage worn items."""

    def __init__(self):
        self.slots = {}
        self.burden = 0.0

    def can_equip_uuid(self, uuid):
        item = find_item[uuid]
        return self.can_equip_item(item)

    def can_equip_item(self, item):
        return bool(item.slot in _WEAR_SLOTS)

    def equip_uuid(self, uuid):
        """Given a UUID, fill a slot with the corresponding item object."""
        item = find_item[uuid]
        self.equip_item(item)

    def equip_item(self, item, body):
        self.slots[slot] = item
        ## TODO: dbms update
        item.on_equip(body)
        self.burden += item.burden

    def in_slot(self, slotname):
        """Return the item in a given slotname, or None for empty."""
        return self.slots.get(slotname, None)

    def remove_uuid(self, uuid):
        item = find_item(uuid)
        self.remove_item(item)

    def remove_item(self, slot):
        self.slots[item.slot] = None
        ## Todo: dbms update
        item.on_remove(body)
        self.burden -= item.burden

    def cascade_event(self, event, body):
        """Apply an event to all worn items to fire custom scripts."""
        pass

    def describe(self):
        pass


#---------------------------------------------------------------------------Bag

class Bag(object):

    """Class for managing player carried items."""

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

    def _reduce(self, burden):
        """Apply the reduction percent to a value"""
        return burden - ( burden * self.reduction )

    def contents(self):
        """Return a string listing the contents."""
        s = ''
        for items in self.items.keys():
            qty = self.items[item]
            s+='%-40s,%d\n\n' % (item.name, qty)
        return s

    def search(self, keyset, qty=1):
        found = []
        for item in self.items:
            if item.trie.match(keyset):
                if self.has(item, qty):
                    found.append(item)
        return found

    def can_stack(self, item, qty=1):
        """Test if we're exceeding the maximum stack size for item."""
        return bool((self.count(item) + qty) > _MAX_STACK_SIZE)

    def can_hold(self, item, qty=1):
        """Test if we're exceeding the maximum burden for the bag."""
        total = self.burden + self._reduce(item.burden * qty)
        return bool( total <= self.limit )

    def count(self, item):
        """Return the quantity of Item."""
        return self.items.get(item, 0)

    def has(self, item, qty=1):
        """Test if container has given quantity of Item."""
        curr = self.count(item)
        return bool(qty <= curr)

    def add(self, item, qty=1):
        """Add given quantity of Item to container and increase burden."""
        curr = self.count(item)
        self.items[item] = curr + qty
        self.burden += _self.reduce( item.burden * qty )

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

    def search(self, keyset, qty=1):
        found = []
        for item in self.items:
            if item.trie.match_keyset(keyset):
                if self.has(item, qty):
                    found.append(item)
        return found

    def can_stack(self, item, qty=1):
        """Test if we're exceeding the maximum stack size for item."""
        return bool((self.count(item) + qty) > _MAX_STACK_SIZE)

    def can_hold(self, item, qty=1):
        """Test if container can hold qty number of item."""
        total = self.burden + (item.burden * qty)
        return bool( total <= self.limit )

    def clean(self):
        """Housekeeping. Sweep away items older than ITEM_DECAY"""
        now = shared.THE_TIME
        is_cleaner = False
        for item in self.items.keys():
            qty, age = self.items[item]
            ## Is the item tuple older than decay time?
            if ( now - age ) > _ITEM_DECAY:
                self.subtract(item, qty)
                is_cleaner = True
        return is_cleaner

    def contents(self):
        """
        Return a string describing the contents.
        Unlike bags, we're going to list the shorter nicks instead of full
        names.
        """
        s = ''
        for item in self.items.keys():
            qty, foo = self.items[item]
            s+='^Y%s^w (x%d)\n\n' % (item.name, qty)
        return s

    def has(self, item, qty=1):
        """Return True if we have quantity of item."""
        return bool(self.count(item) >= qty)

    def count(self, item):
        """Return the quantity item."""
        if item in self.items:
            qty, foo = self.items[item]
        else:
            qty = 0
        return qty

    def add(self, item, qty=1):
        """Add qty number of item to container and increase burden."""
        curr = self.count(item)
        ## Note that adding an existing item resets the timer for all
        self.items[item] = (curr + qty, shared.THE_TIME)
        self.burden += ( item.burden * qty )

    def subtract(self, item, qty=1):
        """Remove qty number of item from container and decrease burden."""
        curr = self.count(item)
        if curr == qty:
            del self.items[item]
        else:
            left = curr - qty
            self.items[item] = (left, shared.THE_TIME)
        self.burden -= (item.burden * qty)


#--------------------------------------------------------------------------Bank

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
