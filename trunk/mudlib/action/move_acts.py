# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/move_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Movement Actions
"""

from mudlib.action.speech_acts import tell_all
from mudlib.world import calendar

#--------------------------------------------------------------common waypoints

def _arrive(actor, room):
    """Actor enters a room."""
    if actor.is_player:
        actor.send_wrapped('^C%s^., %s.\n^w' % (room.name,
            calendar.time_msg()))
        actor.send_wrapped(room.text)
    actor.profile['room'] = room.uuid
    room.on_enter(actor)

def _depart(actor, room):
    """Actor leaves a room."""
    room.on_exit(actor)

#----------------------------------------------------------------------entering

def enter(actor, room):
    """Actor enters room from nowhere."""
    tell_all(room, '\n%s appears from thin air.\n' % actor.get_name())
    _arrive(actor, room)

def enter_north(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s appears from the North.\n' % actor.get_name())
    _arrive(actor, room)

def enter_east(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s appears from the East.\n' % actor.get_name())
    _arrive(actor, room)

def enter_south(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s appears from the South.\n' % actor.get_name())
    _arrive(actor, room)

def enter_west(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s appears from the West.\n' % actor.get_name())
    _arrive(actor, room)

def enter_up(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s comes down from above.\n' % actor.get_name())
    _arrive(actor, room)

def enter_down(actor, room):
    """Directional enter."""
    tell_all(room, '\n%s comes up from below.\n' % actor.get_name())
    _arrive(actor, room)


#-----------------------------------------------------------------------leaving

def leave(actor, room):
    """Actor leaves room headed nowhere."""
    _depart(actor, room)
    tell_all(room, '\n%s vanishes.\n' % actor.get_name())

def leave_north(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves towards the North.\n' % actor.get_name())

def leave_east(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves towards the East.\n' % actor.get_name())

def leave_south(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves towards the South.\n' % actor.get_name())

def leave_west(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves towards the West.\n' % actor.get_name())

def leave_up(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves headed upward.\n' % actor.get_name())

def leave_down(actor, room):
    """Directional departure."""
    _depart(actor, room)
    tell_all(room, '\n%s leaves headed downward.\n' % actor.get_name())
