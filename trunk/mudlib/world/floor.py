# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/floor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Manage items inside rooms.
"""

from mudlib.sys import THE_TIME
from mudlib.sys.error import BogCmdError


## Time for dropped items to vanish from floors
_ITEM_DECAY = 300

## Maximum permitted stack size for any item, including coins.
_MAX_STACK_SIZE = 99999999


class Floor(object):
    """
    Container where items vanish after DECAY_TIME seconds.
    """
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
        """
        Test if we're exceeding the maximum stack size for item.
        """
        return bool((self.count(item) + qty) > _MAX_STACK_SIZE)

    def can_hold(self, item, qty=1):
        """
        Test if container can hold qty number of item.
        """
        total = self.burden + (item.burden * qty)
        return bool( total <= self.limit )

    def clean(self):
        """
        Housekeeping. Sweep away items older than ITEM_DECAY.
        """
        is_cleaner = False
        for item in self.items.keys():
            qty, age = self.items[item]
            ## Is the item tuple older than decay time?
            if ( THE_TIME - age ) > _ITEM_DECAY:
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
        """
        Return True if we have quantity of item.
        """
        return bool(self.count(item) >= qty)

    def count(self, item):
        """
        Return the quantity of Item.
        """
        if item in self.items:
            qty, foo = self.items[item]
        else:
            qty = 0
        return qty

    def add(self, item, qty=1):
        """
        Add quantity of item to container and increase burden.
        """
        curr = self.count(item)
        ## Note that adding an existing item resets the timer for all
        self.items[item] = (curr + qty, THE_TIME)
        self.burden += ( item.burden * qty )

    def subtract(self, item, qty=1):
        """
        Remove quantity of item from container and decrease burden.
        """
        curr = self.count(item)
        if curr == qty:
            del self.items[item]
        else:
            left = curr - qty
            self.items[item] = (left, THE_TIME)
        self.burden -= (item.burden * qty)

