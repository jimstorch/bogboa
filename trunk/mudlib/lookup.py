# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/lookup.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared


#---------------------------------------------------------------------Is Online
     
#def is_online(handle):

#    """Check if a player with the given handle is currently playing."""
#    
#    if shared.HANDLE_DICT.has_key(handle):
#        return True
#    else:
#        return False


#-------------------------------------------------------------------Find Player

#def find_player(handle):

#    """Given a handle, return the Player object."""

#    if handle in shared.HANDLE_DICT:
#        return shared.HANDLE_DICT[handle]

#    else:
#        return None


#---------------------------------------------------------------------Find Room

def room(uuid):

    """Given a uuid, return the Room object."""

    return shared.ROOMS.get(uuid, None)

#----------------------------------------------------------------------Find Mob

def find_body(index):

    """Lookup a mob by index key.  Can be a player avatar or npc."""

    return shared.BODIES.get(index, None)

#---------------------------------------------------------------Next Body Index

def next_body_index():
    
    """Increments and returns the mob index key value."""

    shared.INDEX += 1
    return shared.INDEX    



