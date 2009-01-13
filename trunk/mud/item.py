# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/item.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from lib.shared import ITEM
from driver.log import THE_LOG

#--------------------------------------------------------------------------Item

class Item(object):

    def __init__(self):

        self.uuid = None
        self.name = None
        self.module = None
    
    #-----------------------------------------------------------------On Attack

    def on_attack(self, mob):
        pass

    #------------------------------------------------------------------On Equip

    def on_equip(self, mob):
        pass

    #-------------------------------------------------------------------On Exit

    def on_depart(self, mob):
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

    #-----------------------------------------------------------On Detect Traps

    def on_detect_trap(self, mob):
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, mob):
        pass

    #---------------------------------------------------------------On Identify

    def on_identify(self, mob):
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        pass

    #----------------------------------------------------------------On Inspect

    def on_inspect(self, mob):
        pass

    #-------------------------------------------------------------------On Look

    def on_look(self, mob):
        pass

    #-----------------------------------------------------------------On Remove

    def on_remove(self, mob):
        pass

    #------------------------------------------------------------On Remove Trap

    def on_remove_trap(self, mob):
        pass

    #------------------------------------------------------------------On Enter    

    def on_see(self, mob):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass

    #-----------------------------------------------------------------On Strike

    def on_strike(self, mob):
        pass

    #-----------------------------------------------------------------On Struck

    def on_struck(self, mob):
        pass

    #--------------------------------------------------------------------On Use

    def on_use(self, mob):
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
        THE_LOG.add("ERROR! Missing name in item config.")
        sys.exit(1)

    if 'uuid' in cfg:
        item.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("ERROR! Missing UUID in config for item '%s'." % item.name)
        sys.exit(1)

    if 'desc' in cfg:
        item.desc = cfg.pop('desc')
    else:
        item.desc = None

    if 'sell' in cfg:
        item.sell = cfg.pop('sell')
    else:
        item.sell = None        

    if 'buy' in cfg:
         item.buy = cfg.pop('buy')     
    else:
        item.buy = None

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("WARNING! Unrecognized key(s) in config for item '%s': %s" 
            % ( item.name, cfg.keys()) )

    return item    


#-----------------------------------------------------------------Register Item

def register_item(item):

    """
    Given a configured item, register it with the shared ITEM dictionary.
    """

    if item.uuid in ITEM:
        THE_LOG.add("ERROR! Duplicate UUID (%s) found while registering item"
            " '%s'."  % (item.uuid, item.name) )
        sys.exit(1)
    else:
        ITEM[item.uuid] = item

