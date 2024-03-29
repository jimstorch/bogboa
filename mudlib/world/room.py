# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/room.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Room Class, configuration, and registration.
"""

import sys
from random import choice

from mudlib import gvar
from mudlib.sys import THE_LOG
from mudlib.world.floor import Floor
from mudlib.scripting.bogscript import process_scripts
from mudlib import action

#from mudlib.scripting import SCRIPT_ENV

_CLEANERS = [
    'thieving mice scurry past',
    'a hole opens in time and space',
    'Ferengi flash mob',
    'oh look, magpies',
    'you gonna eat that?',
    'a grue fills his pockets',
    'this really belongs in Lost-n-Found',
    'these bits are needed elsewhere',
    'can I have your stuff?',
    'the world gets slightly lighter',
    "I'm not cleaning that up",
    'finders keepers',
    'is that Winona Ryder?',
    'lift your feet a sec',
    ]


class Room(object):

    def __init__(self):

        self.uuid = None
        self.filename = None
        self.name = None
        self.is_outside = False
        self.exits = {}
        self.scripts = {}
        self.actors = []
        self.floor = Floor()

    def item_search(self, client, ks, qty=1):
        """
        Given a keyset, look for matching item names.
        """
        found = self.floor.search(ks, qty)
        if found:
            for item in found:
                client.send('Matched item: %s' % item.name)
        else:
            client.alert('Not found.')

    def add_item_uuid(self, uuid, qty=1):
        """
        Adds the given item UUID and qty to the room's floor.
        """
        item = ITEMS[uuid]
        self.add_item(item, qty)


    def add_item(self, item, qty=1):
        """
        Adds the given item and qty to the room's floor.
        """

        if self.floor.can_hold(item, qty):
            prefix, noun = guestimate(item.name, qty)
            if qty == 1:
                verb = 'falls'
            else:
                verb = 'fall'

            self.tell_all('^g%s ^y%s^g %s to the ground.^w' % (prefix,
                noun, verb))
            self.floor.add(item, qty)
        else:
            THE_LOG.add('%s had no room to add %s x %d' % ( self.name,
                item.name, qty))

    def sweep(self):
        """
        Remove decayed items from the floor, if any.
        """
        if self.floor.clean():
            self.tell_all('^g... %s^w' % choice(_CLEANERS))


    def get_exit(self, direction):
        """
        If direction is a valid exit, return the corresponding room instance.
        """
        uuid = self.exits.get(direction, None)
        if uuid:
            return gvar.ROOMS[uuid]
        else:
            return None

#    def client_see(self, client):
#        """
#        Look at the current room. Also used by info.look()
#        """
#        room = client.body.room
#        client.send('^c== ^C%s^c, %s ==^w' % (room.name, time_msg()))
#        client.send(room.text)
#        bodies = room.bodies
#        if len(bodies) > 1:
#            client.send('Here with you are;')
#            for body in room.bodies:
#                if body != client.body:
#                    client.send('^G%s^w the ^W%s^w.' % (body.name, body.guild))
#        ## anything laying here?
#        contents = self.floor.contents()
#        if contents:
#            client.send('Laying here you find;')
#            client.send(contents)


    #--------------------------------------------------------------------Events
    ## TODO: docstrings

    def run_script(self, event_name):
        """
        Execute the script for a given event name.
        """
        if event_name in self.scripts:
            exec self.scripts[event_name]

    def on_enter(self, actor):
        self.actors.append(actor)

    def on_exit(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)

    def on_death(self, actor):
        self.run_script('on_death')

    def on_destroy(self):
        self.run_script('on_destroy')

    def on_detect_aura(self, actor):
        self.run_script('on_detect_aura')

    def on_detect_magic(self, actor):
        self.run_script('on_detect_magic')

    def on_detect_traps(self, actor):
        self.run_script('on_detect_traps')

    def on_drop(self, item):
        self.run_script('on_drop')

    def on_hear(self, actor, msg):

        print "on_hear fired"
        if 'on_hear' in self.scripts:

#            _local = {
#                'room':self,
#                'actor':actor,
#                'message':msg,
#                }

            #room = self
            exec self.scripts['on_hear'] #in SCRIPT_ENV, _local

    def on_identify(self, actor):
        self.run_script('on_identify')

    def on_init(self):
        self.run_script('on_init')

    def on_inspect(self, actor):
        self.run_script('on_inspect')

    def on_look(self, actor):
        self.run_script('on_look')

    def on_signal(self, signal):
        self.run_script('on_signal')


#----------------------------------------------------------------Configure Room

def configure_room(cfg):

    """
    Given a configuration dictionary, create a room and configure it.
    Returns the configured room.
    """

    room = Room()

    room.filename = cfg.pop('filename')

    if 'name' in cfg:
        room.name = cfg.pop('name')
    else:
        THE_LOG.add("!! Missing name in room config.")
        sys.exit(1)

    if 'uuid' in cfg:
        room.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("!! Missing UUID in config for room '%s'." % room.name)
        sys.exit(1)

    if 'text' in cfg:
        room.text = cfg.pop('text')
    else:
        room.text = None

#    if 'module' in cfg:
#        room.module = cfg.pop('module')
#    else:
#        room.module = None
#        THE_LOG.add("?? Missing 'module' value for room '%s'." %
#            room.name)

    if 'is_outside' in cfg:
        room.is_outside = cfg.pop('is_outside')

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

    ## For future use
    if 'version' in cfg:
        cfg.pop('version')

    #--------------------------------------------------------------------------
    #   All remaining mappings should be bogscript snippets
    #--------------------------------------------------------------------------

    remain = process_scripts(cfg, room)

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if remain:
        THE_LOG.add("!! Unrecognized key(s) in config for room '%s': %s"
            % ( room.name, cfg.keys()) )

    return room


#-----------------------------------------------------------------Register Room

def register_room(room):

    """
    Given a configured room, register it with the ROOMS dictionary.
    """

    if room.uuid in gvar.ROOMS:
        THE_LOG.add("!! Duplicate UUID (%s) found while registering "
            "room '%s' in module '%s'."  %
            (room.uuid, room.name, room.module))
        sys.exit(1)
    else:
        gvar.ROOMS[room.uuid] = room
