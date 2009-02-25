# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/room.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from mud.shared import ROOM
from driver.log import THE_LOG
from driver.bogscript import check_event_name
from driver.bogscript import compile_script


#--------------------------------------------------------------------------Room

class Room(object):

    def __init__(self):

        self.uuid = None
        self.module = None
        self.name = None
        self.exits = {}
        self.clients = {}
        self.npcs = {}
        self.items = {}
        self.scripts = {}

    #------------------------------------------------------------------On Enter

    def on_enter(self, mob):

        mob.send('You enter %s.\n' % self.name)
        mob.send(self.desc + '\n')
        mob.room = self

        if 'on_enter' in self.scripts:
            exec self.scripts['on_enter']

    #-------------------------------------------------------------------On Exit

    def on_exit(self, mob):
        if 'on_exit' in self.scripts:
            exec self.scripts['on_exit'] 

    #-----------------------------------------------------------------On Death

    def on_death(self, mob):
        if 'on_death' in self.scripts:
            exec self.scripts['on_death'] 

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        if 'on_destroy' in self.scripts:
            exec self.scripts['on_destroy'] 

    #------------------------------------------------------------On Detect Aura

    def on_detect_aura(self, mob):
        if 'on_detect_aura' in self.scripts:
            exec self.scripts['on_detect_aura'] 

    #-----------------------------------------------------------On Detect Magic

    def on_detect_magic(self, mob):
        if 'on_detect_magic' in self.scripts:
            exec self.scripts['on_detech_magic'] 

    #------------------------------------------------------------On Detect Trap

    def on_detect_traps(self, mob):
        if 'on_detect_traps' in self.scripts:
            exec self.scripts['on_detect_traps'] 

    #-------------------------------------------------------------------On Drop

    def on_drop(self, item):
        if 'on_drop' in self.scripts:
            exec self.scripts['on_drop'] 

    #-------------------------------------------------------------------On Hear

    def on_hear(self, mob):
        if 'on_hear' in self.scripts:
            exec self.scripts['on_hear'] 

    #--------------------------------------------------------------On Indentify
    
    def on_identify(self, mob):
        if 'on_identify' in self.scripts:
            exec self.scripts['on_identify'] 

    #-------------------------------------------------------------------On Init

    def on_init(self):
        if 'on_init' in self.scripts:
            exec self.scripts['on_init'] 

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, mob):
        if 'on_inspect' in self.scripts:
            exec self.scripts['on_inspect'] 

    #------------------------------------------------------------------On Look

    def on_look(self, mob):
        if 'on_look' in self.scripts:
            exec self.scripts['on_look'] 

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        if 'on_signal' in self.scripts:
            exec self.scripts['on_signal'] 


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
        room.exits['north'] = cfg.pop('north')
    if 'east' in cfg:
        room.exits['east'] = cfg.pop('east')
    if 'south' in cfg:
        room.exits['south'] = cfg.pop('south')
    if 'west' in cfg:
        room.exits['west'] = cfg.pop('west')
    if 'up' in cfg:
        room.exits['up'] = cfg.pop('up')
    if 'down' in cfg:
        room.exits['down'] = cfg.pop('down')

    ## Accept short-forms too
    if 'n' in cfg:
        room.exits['north'] = cfg.pop('n')
    if 'e' in cfg:
        room.exits['east'] = cfg.pop('e')
    if 's' in cfg:
        room.exits['south'] = cfg.pop('s')
    if 'w' in cfg:
        room.exits['west'] = cfg.pop('w')
    if 'u' in cfg:
        room.exits['up'] = cfg.pop('u')
    if 'd' in cfg:
        room.exits['down'] = cfg.pop('d')

    ## Scripting

    keys = cfg.keys()
    
    #--------------------------------------------------------------------------
    #   All remaining mappings should be bogscript snippets
    #--------------------------------------------------------------------------

    for key in keys:

        ## Look for script snippets that begin with 'on_'

        if key[:3] == 'on_':
            event_name = key
            ## Issue warnings for events that don't match class methods
            check_event_name(event_name, room)
            script = cfg.pop(event_name)
            (msg, code) = compile_script(script, event_name, room)

        if msg == '':
            ## Map the event name to the compiled bytecode
            room.scripts[event_name] = code

        else:
            ## Problem with a script
            print msg
            sys.exit(1)
               

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

