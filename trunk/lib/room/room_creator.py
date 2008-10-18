##-----------------------------------------------------------------------------
##  File:       lib/room/room_creator.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.room.room import Room
from lib.shared import ROOM

#-----------------------------------------------------------------Register Room

def register_room(room):

    """
    Given a configured room, register it with the shared ROOM dictionary.
    """

    if room.uuid in ROOM:
        print ( "ERROR! Duplicate UUID (%s) found while registering "
            "room '%s' in module '%s'."  %
            (room.uuid, room.name, room.module))
        sys.exit(1)
    else:
        ROOM[room.uuid] = room


#----------------------------------------------------------------Configure Room

def configured_room(cfg):

    """
    Given a configuration dictionary, create a room and configure it.
    Returns the configured room.
    """

    room = Room()

    if 'name' in cfg:
        room.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in room config."
        sys.exit(1)

    if 'uuid' in cfg:
        room.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for room '%s'." % name
        sys.exit(1)

    if 'desc' in cfg:
        room.desc = cfg.pop('desc')
    else:
        room.desc = None

    if 'module' in cfg:
        room.module = cfg.pop('module')
    else:
        room.module = None
        print "WARNING: Missing 'module' value for room '%s'." % room.name       

    ## Connect hard-coded exits
    if 'north' in cfg:
        room.exit['north'] = cfg.pop('north')
    if 'east' in cfg:
        room.exit['east'] = cfg.pop('east')
    if 'south' in cfg:
        room.exit['south'] = cfg.pop('south')
    if 'west' in cfg:
        room.exit['west'] = cfg.pop('west')
    if 'up' in cfg:
        room.exit['up'] = cfg.pop('up')
    if 'down' in cfg:
        room.exit['down'] = cfg.pop('down')

    ## Accept short-forms too
    if 'n' in cfg:
        room.exit['north'] = cfg.pop('n')
    if 'e' in cfg:
        room.exit['east'] = cfg.pop('e')
    if 's' in cfg:
        room.exit['south'] = cfg.pop('s')
    if 'w' in cfg:
        room.exit['west'] = cfg.pop('w')
    if 'u' in cfg:
        room.exit['up'] = cfg.pop('u')
    if 'd' in cfg:
        room.exit['down'] = cfg.pop('d')


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        print ( "WARNING! Unrecognized key(s) in config for room '%s': %s" 
            % ( room.name, cfg.keys()) ) 

    return room    
