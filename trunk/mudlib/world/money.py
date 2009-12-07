# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/money.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

#from mudlib.hardwired import COPPER_COIN
#from mudlib.hardwired import SILVER_COIN
#from mudlib.hardwired import GOLD_COIN

## 100 copper = 1 silver
## 10,000 copper = 100 silver = 1 gold
## In other words; 1 copper = 1 cent, 1 silver = 1 dollar, 1 gold = $100 bill


SILVER  = 100
GOLD    = 10000

def money_str(amount):
    """
    Given an INT value, returns a string describing the amount of
    gold, silver, and copper therein.  Empty units are not displayed,
    unless they are all empty, in which case you get '0 coppers'.
    """

    copper = int(amount % SILVER)
    silver = int((amount % GOLD) / SILVER)
    gold = int(amount / GOLD)
    if gold:
        retval = '%d gold' % gold
    if silver and not gold:
        retval = '%d silver' % silver
    elif silver:
        retval += ', %d silver' % silver
    if not silver and not gold:
        retval = '%d coppers' % copper
    elif copper:
        retval += ', %d coppers' % copper
    return retval
