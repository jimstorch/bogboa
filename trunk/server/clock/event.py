#------------------------------------------------------------------------------
#   File:       game_loop.py
#   Purpose:    Wraps a delayed function call, used the Scheduler class.
#   Author:     Jim Storch
#------------------------------------------------------------------------------

#import time
from server import shared


class Event(object):

    def __init__(self, delay, func, args):
    
        self.active = True
        self.when = shared.the_time + delay 
        self.func = func
        self.args = args

    def cancel(self):
        """Causes the event to not-fire when the scheduler selects it."""
        self.active = False



           
