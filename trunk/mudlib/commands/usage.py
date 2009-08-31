# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/usage.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import parsers
from mudlib.lang import keyset

#----------------------------------------------------------------------------Do

def do(client):
    pass


#--------------------------------------------------------------------------Drop

def drop(client, keyset, qty=0, idx=0):
    pass

#------------------------------------------------------------------------Remove

def remove(client):

    """Fix Me"""

    pass

@parsers.name_and_qty
#--------------------------------------------------------------------------Take

def take(client, phrase, qty=1):
    print phrase, qty
    room = client.get_room()
    ks = keyset(phrase)
    room.item_search(client, ks, qty)
    

#--------------------------------------------------------------------------Wear

def wear(client):
    pass
