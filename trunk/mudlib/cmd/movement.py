# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/movement.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Handling Player Movement
"""

from mudlib import gvar
from mudlib.usr import parsers
from mudlib.sys.error import BogCmdError
from mudlib import action


@parsers.blank
def north(player):
    """
    Move North, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('north')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way North is obstructed.')


@parsers.blank
def east(player):
    """
    Move East, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('east')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way East is obstructed.')


@parsers.blank
def south(player):
    """
    Move South, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('south')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way South is obstructed.')


@parsers.blank
def west(player):
    """
    Move West, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('west')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way West is obstructed.')


@parsers.blank
def up(player):
    """
    Move up, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('up')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way up is obstructed.')


@parsers.blank
def down(player):
    """
    Move down, if able.
    """
    actor = player.avatar
    room = actor.get_room_obj()
    dest = room.get_exit('down')
    if dest:
        action.leave_north(actor, room)
        action.enter_south(actor, dest) 
    else:
        raise BogCmdError('The way down is obstructed.')


def enter(player):
    """
    Fix Me
    """
    raise BogCmdError('Not implemented')


def exit(player):
    """
    Fix Me
    """
    raise BogCmdError('Not implemented')

def recall(player):
    """
    Fix Me
    """
    raise BogCmdError('Not implemented')
