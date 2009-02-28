# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/commands/movement.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared

#---------------------------------------------------------------------

def north(client):
    """Move north, if able."""

    if 'north' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['north']]
        leaving.remove_player(client, ' to the North')
        entering.add_player(client, ' from the South')
    
    else:
        client.send('^yThe way North is obstructed.')

north.parser = None


#---[ North East]--------------------------------------------------------------

def northeast(client):
    """Move north-east, if able."""

    if 'northeast' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['northeast']]
        leaving.remove_player(client, ' to the Northeast')
        entering.add_player(client, ' from the Southwest')
    
    else:
        client.send('^yThe way Northeast is obstructed.')

northeast.parser = None 


#---[ East ]-------------------------------------------------------------------

def east(client):
    """Move east, if able."""

    if 'east' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['east']]
        leaving.remove_player(client, ' to the East')
        entering.add_player(client, ' from the West')
    
    else:
        client.send('^yThe way East is obstructed.')

east.parser = None


#---[ South East ]-------------------------------------------------------------

def southeast(client):
    """Move southeast, if able."""

    if 'southeast' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['southeast']]
        leaving.remove_player(client, ' to the Southeast')
        entering.add_player(client, ' from the Northwest')
    
    else:
        client.send('^yThe way Southeast is obstructed.')

southeast.parser = None


#---[ South ]------------------------------------------------------------------

def south(client):
    """Move south, if able."""

    if 'south' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['south']]
        leaving.remove_player(client, ' to the South')
        entering.add_player(client, ' from the North')
    
    else:
        client.send('^yThe way South is obstructed.')

south.parser = None


#---[ South West ]-------------------------------------------------------------

def southwest(client):
    """Move southwest, if able."""

    if 'southwest' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['southwest']]
        leaving.remove_player(client, ' to the Southwest')
        entering.add_player(client, ' from the Northeast')
    
    else:
        client.send('^yThe way Southwest is obstructed.')

southwest.parser = None


#---[ West ]-------------------------------------------------------------------

def west(client):
    """Move west, if able."""

    if 'west' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['west']]
        leaving.remove_player(client, ' to the West')
        entering.add_player(client, ' from the East')
    
    else:
        client.send('^yThe way West is obstructed.')
    
west.parser = None


#---[ North West ]-------------------------------------------------------------

def northwest(client):
    """Move northwest, if able."""

    if 'northwest' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['northwest']]
        leaving.remove_player(client, ' to the Northwest')
        entering.add_player(client, ' from the Southeast')
    
    else:
        client.send('^yThe way Northwest is obstructed.')

northwest.parser = None


#---[ Up ]---------------------------------------------------------------------

def up(client):
    """Move up, if able."""

    if 'up' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['up']]
        leaving.remove_player(client, ' headed upwards')
        entering.add_player(client, ' from below')
    
    else:
        client.send('^yThere is no way up here.')

up.parser = None

#---[ Down ]-------------------------------------------------------------------

def down(client):
    """Move down, if able."""

    if 'down' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['down']]
        leaving.remove_player(client, ' headed downward')
        entering.add_player(client, ' from above')
    
    else:
        client.send('^yThere is no way down here.')

down.parser = None


#---[ Enter ]------------------------------------------------------------------

def enter(client):
    pass

enter.parser = None


#---[ Exit ]-------------------------------------------------------------------

def exit(client):
    pass

exit.parser = None
 

#---[ Recall ]-----------------------------------------------------------------

def recall(client):
    pass

recall.parser = None


