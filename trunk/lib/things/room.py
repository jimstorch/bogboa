#------------------------------------------------------------------------------
#   File:       lib/rooms/room.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Room(object):

    def __init__(self, script=None):

        self.uuid = None
        self.handle = None
        self.module = None
        self.illumination = 0

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




