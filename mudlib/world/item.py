# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/item.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib import gvar
from mudlib.sys import THE_LOG
from mudlib.lang import NameTrie
from mudlib.scripting.bogscript import process_scripts


class Item(object):

    def __init__(self):

        self.uuid = None
        self.filename = None
        self.name = None        # Full Item Name
        self.nick = None        # short nickname
        self.trie = NameTrie()  # string matching object
        self.text = None        # description
        self.slot = None        # which wardrobe slot, if any, the item fits
        self.burden = 0.0       # the mass/weight for tracking encumbrance
        self.value = 0.0        # What a vendor will pay for it
        self.scripts = {}       # Builder defined event scripts


#    #-------------------------------------------------------------Body and Item

#    def body_and_item(method):

#        """
#        Decorator to pass self as 'item' for simpler scripting syntax.
#        """

#        def method_wrapper(self, body):
#            item = self
#            method(self, body, item)
#        return method_wrapper


#    #--------------------------------------------------------Body Item and Room

#    def body_item_and_room(method):

#        """
#        Decorator to pass self as 'item' and body.room as 'room' for simpler
#        scripting syntax.
#        """

#        def wrapped_method(self, body):
#            item = self
#            room = body.room
#            method(self, body, item, room)
#        return wrapped_method


    #-----------------------------------------------------------------On Attack

    def on_attack(self, body):
        item = self
        room = body.room
        pass

    #------------------------------------------------------------------On Equip

    def on_equip(self, body):
        item = self
        room = body.room
        pass

    #-------------------------------------------------------------------On Exit

    def on_depart(self, body):
        item = self
        room = body.room
        pass

    #----------------------------------------------------------------On Destroy

    def on_destroy(self, body):
        item = self
        room = body.room
        pass

    #------------------------------------------------------------On Detect Aura

    def on_detect_aura(self, body):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------On Detect Magic

    def on_detect_magic(self, body):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------On Detect Traps

    def on_detect_trap(self, body):
        item = self
        room = body.room
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, body):
        item = self
        room = body.room
        pass

    #---------------------------------------------------------------On Identify

    def on_identify(self, body):
        item = self
        room = body.room
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        item = self
        room = body.room
        pass

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, body):
        item = self
        room = body.room
        pass

    #-------------------------------------------------------------------On Look

    def on_look(self, body):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------On Remove

    def on_remove(self, body):
        item = self
        room = body.room
        pass

    #------------------------------------------------------------On Remove Trap

    def on_remove_trap(self, body):
        item = self
        room = body.room
        pass

    #------------------------------------------------------------------On Enter

    def on_see(self, body):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------On Strike

    def on_strike(self, body):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------On Struck

    def on_struck(self, body):
        item = self
        room = body.room
        pass

    #--------------------------------------------------------------------On Use

    def on_use(self, body):
        item = self
        room = body.room
        pass

    #----------------------------------------------------------------------Poof

    def poof(self):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------Set Alias

    def set_alias(self, alias):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------Set Fixed

    def set_fixed(self, boolean):
        item = self
        room = body.room
        pass

    #-----------------------------------------------------------------Set Skill

    def set_skill(self, skill_uuid, value):
        item = self
        room = body.room
        pass

    #------------------------------------------------------------------Set Slot

    def set_slot(self, slot_uuid):
        pass


def configure_item(cfg):
    """
    Given a configuration dictionary, create an item and configure it.
    Returns the configured item.
    """
    item = Item()

    item.filename = cfg.pop('filename')

    if 'uuid' in cfg:
        item.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("!! Missing UUID in config for item '%s'." % item.name)
        sys.exit(1)

#    if 'module' in cfg:
#        item.module = cfg.pop('module')
#    else:
#        item.module = None
#        THE_LOG.add("?? Missing 'module' value for item '%s'." %
#            item.name)

    if 'name' in cfg:
        item.name = cfg.pop('name')
        item.trie.feed(item.name)
    else:
        THE_LOG.add("!! Missing name in item config.")
        sys.exit(1)

    if 'nick' in cfg:
        item.nick = cfg.pop('nick')
#        item.trie.feed(item.nick)
    else:
        item.nick = item.name

    if 'hint' in cfg:
        hint = cfg.pop('hint')
        item.trie.feed(hint)

    if 'text' in cfg:
        item.text = cfg.pop('text')

    if 'slot' in cfg:
        item.slot = cfg.pop('slot')

    if 'burden' in cfg:
        item.burden = float(cfg.pop('burden'))

    if 'value' in cfg:
        item.value = float(cfg.pop('value'))

    ## For future use
    if 'version' in cfg:
        cfg.pop('version')

    #--------------------------------------------------------------------------
    #   All remaining mappings should be bogscript snippets
    #--------------------------------------------------------------------------

    remain = process_scripts(cfg, item)

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if remain:
        THE_LOG.add("!! Unrecognized key(s) in config for item '%s': %s"
            % ( item.name, cfg.keys()) )

    return item


def register_item(item):
    """
    Given a configured item, register it with the shared ITEM dictionary.
    """
    if item.uuid in gvar.ITEMS:
        THE_LOG.add("!! Duplicate UUID (%s) found while registering item"
            " '%s'."  % (item.uuid, item.name) )
        sys.exit(1)
    else:
        gvar.ITEMS[item.uuid] = item
