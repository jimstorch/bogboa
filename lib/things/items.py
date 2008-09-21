#------------------------------------------------------------------------------
#   File:       lib/items/item.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Item(object):

    def __init__(self):
    
        self.uuid = uuid
        self.handle = None
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




