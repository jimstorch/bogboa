# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/room.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from lib.shared import ROOM
from driver.log import THE_LOG



#--------------------------------------------------------------------------Room

class Room(object):

    def __init__(self):

        self.uuid = None
        self.module = None
        self.name = None
        self.exit = {}

    #------------------------------------------------------------------On Enter

    def on_enter(self, mob):
        pass

    #-------------------------------------------------------------------On Exit

    def on_exit(self, mob):
        pass

    #-----------------------------------------------------------------On Death

    def on_death(self, mob):
        pass

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        pass

    #------------------------------------------------------------On Detect Aura

    def on_detect_aura(self, mob):
        pass

    #-----------------------------------------------------------On Detect Magic

    def on_detect_magic(self, mob):
        pass

    #------------------------------------------------------------On Detect Trap

    def on_detect_trap(self, mob):
        pass

    #-------------------------------------------------------------------On Drop

    def on_drop(self, item):
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, mob):
        pass

    #--------------------------------------------------------------On Indentify
    
    def on_indentify(self, mob):
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        pass

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, mob):
        pass

    #------------------------------------------------------------------On Look

    def on_look(self, mob):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass


#----------------------------------------------------------------Configure Room

def configure_room(cfg):

    """
    Given a configuration dictionary, create a room and configure it.
    Returns the configured room.
    """

    room = Room()

    if 'name' in cfg:
        room.name = cfg.pop('name')
    else:
        THE_LOG.add("ERROR! Missing name in room config.")
        sys.exit(1)

    if 'uuid' in cfg:
        room.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("ERROR! Missing UUID in config for room '%s'." % room.name)
        sys.exit(1)

    if 'desc' in cfg:
        room.desc = cfg.pop('desc')
    else:
        room.desc = None

    if 'module' in cfg:
        room.module = cfg.pop('module')
    else:
        room.module = None
        THE_LOG.add("WARNING: Missing 'module' value for room '%s'." % 
            room.name)       

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
        THE_LOG.add("WARNING! Unrecognized key(s) in config for room '%s': %s" 
            % ( room.name, cfg.keys()) ) 

    return room    


#-----------------------------------------------------------------Register Room

def register_room(room):

    """
    Given a configured room, register it with the shared ROOM dictionary.
    """

    if room.uuid in ROOM:
        THE_LOG.add("ERROR! Duplicate UUID (%s) found while registering "
            "room '%s' in module '%s'."  %
            (room.uuid, room.name, room.module))
        sys.exit(1)
    else:
        ROOM[room.uuid] = room

