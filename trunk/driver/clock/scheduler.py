##-----------------------------------------------------------------------------
##  File:       scheduler.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

"""Contains the event scheduler class and a shared instance on it."""

import sys
import time
import operator
from bisect import insort

from lib import shared


if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time

#--[ Scheduler Class ]---------------------------------------------------------


class Scheduler(object):

    """Manage scheduler events."""

    def __init__(self):
        self.event_list = []
        self.start_time = default_timer()  

    def add(self, delay, func, args):
        """Add a delayed function call to the schedule.  Delay is in seconds
        and may be a decimal."""
        ## create a new event object
        event = Event(delay, func, args)
        ## Do an in-order insertion 
        insort(self.event_list, event)
        return event 

    def age(self):
        """Return the age of the scheduler in seconds."""
        return shared.THE_TIME - self.start_time

    def tick(self):
        """Fire and delete all events that have a schedule time < now."""
        ## Give up some CPU time, just to be nice
        time.sleep(.001)

        ## Update the global time value 
        shared.THE_TIME = default_timer()

        while self.event_list:
            ## Look at the first event
            event = self.event_list[0]
            ## Is is past time for it to fire?
            if event.when < shared.THE_TIME:
                ## And is it still active?
                if event.active:
                    ## call it
                    event.func(event.args)
                ## and delete it from the list
                self.event_list.pop(0)
            else:
                ## all pending events are gone, let's get out of here 
                break


#--[ Global Instance ]---------------------------------------------------------

THE_SCHEDULER = Scheduler()

#------------------------------------------------------------------------------
   
