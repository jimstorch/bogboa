#------------------------------------------------------------------------------
#   File:       lib/modules/module.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Module(object):

    def __init__(self, script=None):

        self.uuid = None
        self.handle = None
        self.module = None
        self.illumination = 0
        
    #-----------------------------------------------------------------On Create

    def on_init(self):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass




