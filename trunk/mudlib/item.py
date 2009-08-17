# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/item.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib.shared import ITEMS
from driver.log import THE_LOG

#--------------------------------------------------------------------------Item

class Item(object):

    def __init__(self):

        self.uuid = None
        self.name = None
        self.module = None
        self.weight = 0
    
    #-----------------------------------------------------------------On Attack

    def on_attack(self, body):
        pass

    #------------------------------------------------------------------On Equip

    def on_equip(self, body):
        pass

    #-------------------------------------------------------------------On Exit

    def on_depart(self, body):
        pass

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        pass    

    #------------------------------------------------------------On Detect Aura

    def on_detect_aura(self, body):
        pass

    #-----------------------------------------------------------On Detect Magic

    def on_detect_magic(self, body):
        pass

    #-----------------------------------------------------------On Detect Traps

    def on_detect_trap(self, body):
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, body):
        pass

    #---------------------------------------------------------------On Identify

    def on_identify(self, body):
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        pass

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, body):
        pass

    #-------------------------------------------------------------------On Look

    def on_look(self, body):
        pass

    #-----------------------------------------------------------------On Remove

    def on_remove(self, body):
        pass

    #------------------------------------------------------------On Remove Trap

    def on_remove_trap(self, body):
        pass

    #------------------------------------------------------------------On Enter

    def on_see(self, body):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass

    #-----------------------------------------------------------------On Strike

    def on_strike(self, body):
        pass

    #-----------------------------------------------------------------On Struck

    def on_struck(self, body):
        pass

    #--------------------------------------------------------------------On Use

    def on_use(self, body):
        pass

    #----------------------------------------------------------------------Poof

    def poof(self):
        pass

    #-----------------------------------------------------------------Set Alias

    def set_alias(self, alias):
        pass

    #-----------------------------------------------------------------Set Fixed

    def set_fixed(self, boolean):
        pass

    #-----------------------------------------------------------------Set Skill

    def set_skill(self, skill_uuid, value):
        pass

    #------------------------------------------------------------------Set Slot

    def set_slot(self, slot_uuid):
        pass


#----------------------------------------------------------------Configure Item

def configure_item(cfg):

    """
    Given a configuration dictionary, create an item and configure it.
    Returns the configured item.
    """

    item = Item()

    if 'name' in cfg:
        item.name = cfg.pop('name')
    else:
        THE_LOG.add("!! Missing name in item config.")
        sys.exit(1)

    if 'uuid' in cfg:
        item.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("!! Missing UUID in config for item '%s'." % item.name)
        sys.exit(1)

    if 'desc' in cfg:
        item.desc = cfg.pop('desc')
    else:
        item.desc = None

    if 'weight' in cfg:
        item.weight = cfg.pop('weight')
    else:
        item.weight = 0

    if 'value' in cfg:
        item.value = cfg.pop('value')
    else:
        item.value = 0        

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("!! Unrecognized key(s) in config for item '%s': %s" 
            % ( item.name, cfg.keys()) )

    return item    


#-----------------------------------------------------------------Register Item

def register_item(item):

    """
    Given a configured item, register it with the shared ITEM dictionary.
    """

    if item.uuid in ITEMS:
        THE_LOG.add("!! Duplicate UUID (%s) found while registering item"
            " '%s'."  % (item.uuid, item.name) )
        sys.exit(1)
    else:
        ITEMS[item.uuid] = item

