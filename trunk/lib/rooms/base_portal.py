#------------------------------------------------------------------------------
#   File:       base_portal.py
#   Purpose:    parent class for portals
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class BasePortal(object):

    def __init__(self):

        self.handle = ''
        self.name = ''
        self.description = ''
        self.room = None
        self.flags = {}


    def use(self, *args):
        pass
    
    def reset(self):
        pass


    def has_flag(self, handle):
        if handle in self.flags:
            return self.flags[handle]
        else:
            return None
    

