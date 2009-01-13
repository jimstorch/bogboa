# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lookup.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mud import shared


#---------------------------------------------------------------------Is Online
     
def is_online(handle):

    """Check if a player with the given handle is currently playing."""
    
    if shared.HANDLE_DICT.has_key(handle):
        return True
    else:
        return False


#-------------------------------------------------------------------Find Player

def find_player(handle):

    """Given a handle, return the Player object."""

    if handle in shared.HANDLE_DICT:
        return shared.HANDLE_DICT[handle]

    else:
        return None


#---------------------------------------------------------------------Find Room

def find_room(handle):

    """Given a handle, return the Room object."""

    if handle in shared.ROOM_DICT:
        return shared.ROOM_DICT[handle]

    else:
        return None
