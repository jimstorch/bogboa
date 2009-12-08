# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/shared.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.sys.log import Log
from mudlib.sys.scheduler import Scheduler


## Boolean used by the main loop, False = stop the server

SERVER_RUN = True

#--------------------------------------------------------------Shared Instances

LOG = Log('server.log', append=True)
SCHEDULER = Scheduler()


## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: THE_TIME gets updates each cycle by
## driver.scheduler.THE_SCHEDULER.tick().

THE_TIME = 0.0


#--[ Client Connections ]------------------------------------------------------

LOBBY_CLIENTS = {}  ## Key is Client object, value is Visitor object
PLAY_CLIENTS = {}   ## Key is Client object, value is Player object
BY_NAME = {}        ## key is player name, value is Player object

#--[ Reference Objects ]-------------------------------------------------------

GUILDS = {}         ## key is guild name
HELPS = {}          ## key is help name
RACES = {}          ## key is race name
ITEMS = {}          ## key is item UUID
SPAWNS = {}         ## key is npc UUID


#--[ Objects in the game world ]-----------------------------------------------

OBJECTS = {}        ## key is object UUID
ROOMS = {}          ## key is room UUID
BODIES = {}         ## key is body UUID
BRAINS = []         ## List of AI's


#-------------------------------------------------------------------Find Player

def find_player(name):

    """Given a player's name, return the client or None."""

    return BY_NAME.get(name.lower(), None)


#---------------------------------------------------------------------Find Room

def find_room(uuid):

    """Given a room UUID, return the room object or None."""

    return ROOMS.get(uuid, None)


#---------------------------------------------------------------------Find Item

def find_item(uuid):

    """Given an item UUID, return the item object or None."""

    return ITEMS.get(uuid, None)

#---------------------------------------------------------------------Is Online

def is_online(name):

    """Return True is the given name matches an online player."""

    return name in BY_NAME
