#------------------------------------------------------------------------------
#   File:       game_loop.py
#   Purpose:    Wraps a delayed function call, used by the Scheduler class.
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared

class Event(object):

    def __init__(self, delay, func, args):
    
        self.active = True
        self.when = shared.THE_TIME + delay 
        self.func = func
        self.args = args

    def cancel(self):
        """Causes the event to not-fire when the scheduler selects it."""
        self.active = False



           
