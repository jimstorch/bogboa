# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/inventory.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Classes for managing Item storage.
"""

from mudlib.sys.error import BogCmdError

## Maximum permitted stack size for any item, including coins.
_MAX_STACK_SIZE = 99999999

### Defined wear slots for equipable weapons, armor, and jewelry.
#WEAR_SLOTS = set(['head', 'face', 'ears', 'neck', 'shoulders', 'back',
#        'chest', 'arms', 'wrists', 'hands', 'fingers',
#        'main hand', 'off hand', 'both hands','waist', 'legs', 'feet'])


class Outfit(object):
    """
    Paper-doll Class to manage worn items.
    """

    def __init__(self):
        self.slots = {}
        self.burden = 0.0

    def equip_item(self, item):
        self.slots[item.slot] = item
        self.burden += item.burden

    def remove_item(self, slot):
        self.slots[item.slot] = None
        self.burden -= item.burden

#    def can_equip_uuid(self, uuid):
#        item = find_item[uuid]
#        return self.can_equip_item(item)

#    def can_equip_item(self, item):
#        return bool(item.slot in WEAR_SLOTS)

#    def equip_uuid(self, uuid):
#        """
#        Given a UUID, fill a slot with the corresponding item object.
#        """
#        item = find_item[uuid]
#        self.equip_item(item)

#    def in_slot(self, slot):
#        """
#        Return the item in a given slot, or None for empty.
#        """
#        return self.slots.get(slot, None)

#    def remove_uuid(self, uuid):
#        item = find_item(uuid)
#        self.remove_item(item)

#    def cascade_event(self, event, body):
#        """
#        Apply an event to all worn items to fire custom scripts.
#        """
#        pass

#    def describe(self):
#        pass

#    def db_save(self, uuid):
#        pass

#    def db_load(self, uuid):
#        pass

#---------------------------------------------------------------------------Bag

class Bag(object):
    """
    Class for managing actor carried items.
    """

    def __init__(self):
        ## Start out with some beginner settings
        ## A 'new bag' simply improves on these values
        self.name = 'bag'       ## Displayed name
        self.burden = 0.0       ## Current weight/mass
        self.limit = 50.0       ## maxium allowed
        self.reduction = 0.0    ## magical burden reduction %
        ## Dict of Contents
        ##   key = item, value = count
        self.items = {}

    def _reduce(self, burden):
        """
        Apply the reduction percent to a value.
        """
        return burden - ( burden * self.reduction )

#    def contents(self):
#        """
#        Return a string listing the contents.
#        """
#        s = ''
#        for items in self.items.keys():
#            qty = self.items[item]
#            s+='%-40s,%d\n\n' % (item.name, qty)
#        return s

    def search(self, keyset, qty=1):
        found = []
        for item in self.items:
            if item.trie.match(keyset):
                if self.has(item, qty):
                    found.append(item)
        return found

    def can_stack(self, item, qty=1):
        """
        Test if we're exceeding the maximum stack size for item.
        """
        return bool((self.count(item) + qty) > _MAX_STACK_SIZE)

    def can_hold(self, item, qty=1):
        """
        Test if we're exceeding the maximum burden for the bag.
        """
        total = self.burden + self._reduce(item.burden * qty)
        return bool( total <= self.limit )

    def count(self, item):
        """
        Return the quantity of Item.
        """
        return self.items.get(item, 0)

    def has(self, item, qty=1):
        """Test if container has given quantity of Item."""
        curr = self.count(item)
        return bool(qty <= curr)

    def add(self, item, qty=1):
        """
        Add given quantity of Item to container and increase burden.
        """
        curr = self.count(item)
        self.items[item] = curr + qty
        self.burden += self._reduce( item.burden * qty )

    def subtract(self, item, qty=1):
        """
        Remove given quantity of Item from container and reduce burden.
        """
        curr = self.count(item)
        if curr == qty:
            ## Don't maintain empty mappings
            del self.items[item]
        else:
            remaining = curr - qty
            self.items[item] = remaining
            self.burden -= _self.reduce( item.burden * qty)

    def db_save(self, uuid):
        pass

    def db_load(self, uuid):
        pass

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
