# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/commands/movement.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib import lookup


#-------------------------------------------------------------------------North

def north(client):

    """Move north, if able."""

    room = shared.ROOMS[client.body.room_uuid]
   
    if 'north' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['north']]
        leaving.on_exit(client.body, 'North')
        entering.on_enter(client.body, 'South')
    
    else:
        client.send('The way North is obstructed.')



#-------------------------------------------------------------------------South

def south(client):

    """Move north, if able."""

    room = shared.ROOMS[client.body.room_uuid]
   
    if 'south' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['south']]
        leaving.on_exit(client.body, 'South')
        entering.on_enter(client.body, 'North')
    
    else:
        client.send('The way South is obstructed.')


#--------------------------------------------------------------------------East

def east(client):

    """Move east, if able."""

    room = shared.ROOMS[client.body.room_uuid]
   
    if 'east' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['east']]
        leaving.on_exit(client.body, 'East')
        entering.on_enter(client.body, 'West')
    
    else:
        client.send('The way East is obstructed.')


#--------------------------------------------------------------------------West

def west(client):

    """Move west, if able."""

    room = shared.ROOMS[client.body.room_uuid]
   
    if 'west' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['west']]
        leaving.on_exit(client.body, 'West')
        entering.on_enter(client.body, 'East')
    
    else:
        client.send('The way West is obstructed.')

#----------------------------------------------------------------------------Up

def up(client):
    """Move up, if able."""

    if 'up' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['up']]
        leaving.remove_player(client, ' headed upwards')
        entering.add_player(client, ' from below')
    
    else:
        client.send('^yThere is no way up here.')


#--------------------------------------------------------------------------Down

def down(client):
    """Move down, if able."""

    if 'down' in client.room.exits:
        leaving = client.room
        entering = shared.ROOM_DICT[client.room.exits['down']]
        leaving.remove_player(client, ' headed downward')
        entering.add_player(client, ' from above')
    
    else:
        client.send('^yThere is no way down here.')


#-------------------------------------------------------------------------Enter

def enter(client):
    pass


#--------------------------------------------------------------------------Exit

def exit(client):
    pass


#------------------------------------------------------------------------Recall

def recall(client):
    pass


