# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/movement.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib import lookup
from mudlib import parsers

#-------------------------------------------------------------------------North
@parsers.blank
def north(client):

    """Move north, if able."""

    room = client.body.room
   
    if 'north' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['north']]
        leaving.on_exit(client.body, 'the North')
        entering.on_enter(client.body, 'the South')
    
    else:
        client.send('The way North is obstructed.')



#-------------------------------------------------------------------------South
@parsers.blank
def south(client):

    """Move north, if able."""

    room = client.body.room
   
    if 'south' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['south']]
        leaving.on_exit(client.body, 'to the South')
        entering.on_enter(client.body, 'the North')
    
    else:
        client.send('The way South is obstructed.')


#--------------------------------------------------------------------------East
@parsers.blank
def east(client):

    """Move east, if able."""

    room = client.body.room
   
    if 'east' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['east']]
        leaving.on_exit(client.body, 'to the East')
        entering.on_enter(client.body, 'the West')
    
    else:
        client.send('The way East is obstructed.')


#--------------------------------------------------------------------------West
@parsers.blank
def west(client):

    """Move west, if able."""

    room = client.body.room
   
    if 'west' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['west']]
        leaving.on_exit(client.body, 'to the West')
        entering.on_enter(client.body, 'the East')
    
    else:
        client.send('The way West is obstructed.')

#----------------------------------------------------------------------------Up
@parsers.blank
def up(client):

    """Move up, if able."""

    room = client.body.room
   
    if 'up' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['up']]
        leaving.on_exit(client.body, 'upward')
        entering.on_enter(client.body, 'below')
    
    else:
        client.send('The way up is obstructed.')


#--------------------------------------------------------------------------Down
@parsers.blank
def down(client):

    """Move down, if able."""

    room = client.body.room
   
    if 'down' in room.exits:
        leaving = room
        entering = shared.ROOMS[room.exits['down']]
        leaving.on_exit(client.body, 'downward')
        entering.on_enter(client.body, 'above')
    
    else:
        client.send('The way down is obstructed.')

#-------------------------------------------------------------------------Enter

def enter(client):
    pass


#--------------------------------------------------------------------------Exit

def exit(client):
    pass


#------------------------------------------------------------------------Recall

def recall(client):
    pass


