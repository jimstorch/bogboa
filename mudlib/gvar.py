# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/gvar.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Variables required across multiple modules
"""

## Boolean used by the main loop, False = stop the server

SERVER_RUN = True


## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: THE_TIME gets updates each cycle by
## driver.scheduler.THE_SCHEDULER.tick().

THE_TIME = 0.0


#--[ Client Connections ]------------------------------------------------------

LOBBY = {}          ## Key is Client object, value is Entrant object
PLAYERS = {}        ## Key is Client object, value is Player object
AVATARS = {}        ## key is player name, value is Avatar object


#--[ Reference Objects ]-------------------------------------------------------

GUILDS = {}         ## key is guild name
HELPS = {}          ## key is help name
RACES = {}          ## key is race name
ITEMS = {}          ## key is item UUID
SPAWNS = {}         ## key is npc UUID


#--[ Objects in the game world ]-----------------------------------------------

OBJECTS = {}        ## key is object UUID
ROOMS = {}          ## key is room UUID


def find_room(uuid):
    """
    Given a UUID, return the corresponding Room Instance.
    """
    return ROOMS.get(uuid, None)

def find_avatar(name):
    """
    Given a name, return the corresponding avatar.
    """
    return AVATARS.get(name.lower(), None)

def find_item(uuid):
    """
    Give a UUID, return the corresponding item.
    """
    return ITEMS.get(uuid, None)

    
