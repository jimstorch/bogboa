# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/room.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib import shared
from driver.log import THE_LOG
from driver.bogscript import check_event_name
from driver.bogscript import compile_script
from mudlib.calendar import time_msg
from inventory import TimedContainer
from mudlib.lang import numerate


#--------------------------------------------------------------------------Room

class Room(object):

    def __init__(self):

        self.uuid = None
        self.module = None
        self.name = None
        self.is_outside = False
        self.exits = {}
        self.scripts = {}
        self.bodies = []
        self.stuff = TimedContainer()


    #-------------------------------------------------------------Body and Room

    def body_and_room(method):

        """
        Decorator to pass self as 'room' for simpler scripting syntax.
        """ 

        def method_wrapper(self, body):
            room = self
            method(self, body, room)
        return method_wrapper


    #-------------------------------------------------------------Add Item UUID

    def add_item_uuid(self, uuid, qty=1):


        item = shared.ITEMS[uuid]
        self.add_item(item, qty)

    #------------------------------------------------------------------Add Item

    def add_item(self, item, qty=1):

        if self.stuff.can_hold(item, qty):

            prefix, noun = numerate(item.name, qty)
            if qty == 1:
                verb = 'falls'
            else:
                verb = 'fall'

            self.tell_all('^g%s ^y%s^g %s to the ground.^w' % (prefix, noun, verb))
            self.stuff.add(item, qty)
        else:
            THE_LOG.add('%s had no room to add %s x %d' % ( self.name,
                item.name, qty))


    #------------------------------------------------------------------Tell All

    def tell_all(self, msg):
        
        """Send a message to every player in the room."""

        for body in self.bodies:
            if body.is_player:
                body.mind.send(msg)


    #--------------------------------------------------------------Tell All But

    def tell_all_but(self, body, msg):
        
        """Send a message to every player in the room except body."""

        for a_body in self.bodies:
            if a_body.is_player and a_body != body:
                a_body.send(msg)

    #----------------------------------------------------------------Client See

    def client_see(self, client):

        """Look at the current room. Also used by info.look()"""

        room = client.body.room
        client.send('^c== ^C%s^c, %s ==^w' % (room.name, time_msg()))
        client.send(room.text)
        bodies = room.bodies
        if len(bodies) > 1:
            client.send('Here with you are;')
            for body in room.bodies:
                if body != client.body:
                    client.send('^G%s^w the ^W%s^w.' % (body.name, body.guild))
        ## anything laying here?        
        contents = self.stuff.contents()
        if contents:
            client.send('Laying here you find;')
            client.send(contents)


    #------------------------------------------------------------------On Enter

    def on_enter(self, body, direction=None):

        body.room = self

        if body.uuid: 

            if direction:
                self.tell_all('^g%s enters from %s.^w' % 
                    (body.name, direction))          
            else:
                self.tell_all("^g%s appears.^w" % body.name )       
            
            if body.is_player:
                self.client_see(body.mind)

        self.bodies.append(body)

        if 'on_enter' in self.scripts:
            exec self.scripts['on_enter']

    #-------------------------------------------------------------------On Exit

    def on_exit(self, body, direction=None):

        self.bodies.remove(body)             

        if body.uuid:

            if direction:
                self.tell_all('^g%s exits %s.^w' % 
                    (body.name, direction))          
            else:
                self.tell_all('^g%s vanishes.^w' % body.name)          

        if 'on_exit' in self.scripts:
            exec self.scripts['on_exit']

    #-----------------------------------------------------------------On Death

    def on_death(self, body):
        if 'on_death' in self.scripts:
            exec self.scripts['on_death'] 

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        if 'on_destroy' in self.scripts:
            exec self.scripts['on_destroy'] 

    #------------------------------------------------------------On Detect Aura

    def on_detect_aura(self, body):
        if 'on_detect_aura' in self.scripts:
            exec self.scripts['on_detect_aura'] 

    #-----------------------------------------------------------On Detect Magic

    def on_detect_magic(self, body):
        if 'on_detect_magic' in self.scripts:
            exec self.scripts['on_detech_magic'] 

    #------------------------------------------------------------On Detect Trap

    def on_detect_traps(self, body):
        if 'on_detect_traps' in self.scripts:
            exec self.scripts['on_detect_traps'] 

    #-------------------------------------------------------------------On Drop

    def on_drop(self, item):
        if 'on_drop' in self.scripts:
            exec self.scripts['on_drop'] 

    #-------------------------------------------------------------------On Hear

    def on_hear(self, body, msg):
        
        print "on_hear fired"
        if 'on_hear' in self.scripts:
            room = self
            exec self.scripts['on_hear'] 

    #--------------------------------------------------------------On Indentify
    
    def on_identify(self, body):
        if 'on_identify' in self.scripts:
            exec self.scripts['on_identify'] 

    #-------------------------------------------------------------------On Init

    def on_init(self):
        if 'on_init' in self.scripts:
            exec self.scripts['on_init'] 

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, body):
        if 'on_inspect' in self.scripts:
            exec self.scripts['on_inspect'] 

    #------------------------------------------------------------------On Look

    def on_look(self, body):
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

    if 'module' in cfg:
        room.module = cfg.pop('module')
    else:
        room.module = None
        THE_LOG.add("?? Missing 'module' value for room '%s'." % 
            room.name)       

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
        THE_LOG.add("!! Unrecognized key(s) in config for room '%s': %s" 
            % ( room.name, cfg.keys()) ) 

    return room    


#-----------------------------------------------------------------Register Room

def register_room(room):

    """
    Given a configured room, register it with the shared ROOM dictionary.
    """

    if room.uuid in shared.ROOMS:
        THE_LOG.add("!! Duplicate UUID (%s) found while registering "
            "room '%s' in module '%s'."  %
            (room.uuid, room.name, room.module))
        sys.exit(1)
    else:
        shared.ROOMS[room.uuid] = room

