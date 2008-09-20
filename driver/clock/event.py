#------------------------------------------------------------------------------
#   File:       driver/clock/event.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from lib import shared


class Event(object):

    """ Wraps a delayed function call, used by the Scheduler class."""

    def __init__(self, delay, func, args=None):
    
        self.active = True
        self.when = shared.THE_TIME + delay 
        self.func = func
        self.args = args

    def __cmp__(self, other):

        """Define a compare function for bisect's sorted insert"""

        return cmp(self.when, other.when)


    def cancel(self):

        """Causes the event to not-fire when the scheduler selects it."""

        self.active = False



           
