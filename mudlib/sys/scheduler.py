# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/scheduler.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Contains the event scheduler class and a shared instance on it.
"""

import sys
import time
import operator
from bisect import insort

from mudlib import gvar


class Event(object):
    """
    Wraps a delayed function call, used by the Scheduler class.
    """
    def __init__(self, delay, func, args):
        self.active = True
        self.when = gvar.THE_TIME + delay
        self.func = func
        self.args = args

    def __cmp__(self, other):
        """
        Define a compare function for bisect's sorted insert
        """
        return cmp(self.when, other.when)

    def cancel(self):
        """
        Causes the event to not-fire when the scheduler selects it.
        """
        self.active = False


class Cycle(object):
    """
    Schedules a delayed event that repeats until canceled.
    """
    def __init__(self, delay, func, args=()):

        self.active = True
        self.delay = delay
        self.func = func
        self.args = args
        self._schedule()

    def _fire(self):
        ## call the requested func
        self.func(*self.args)
        ## and reschedule our _fire method
        self._schedule()

    def _schedule(self):
        ## Schedule an event to call our _fire method
        self.next_event = THE_SCHEDULER.add(self.delay, self._fire)

    def cancel(self):
        """
        Halt the cycle and the next event.
        """
        self.active = False
        self.next_event.cancel()

    def pause(self):
        """
        Halt the cycle.
        """
        ## Currenly the same as cancel()
        self.cancel()

    def restart(self):
        """
        Begin the cycle again in 'delay' seconds.
        """
        self.active = True
        self._schedule()


class Series(object):
    """
    Scheduler a set number of identical events with consecutive delays.
    """
    def __init__(self, count, delay, func, args=() ):
        self.active = True
        self.event_list = []
        for x in range(count):
            event = THE_SCHEDULER.add(delay * (x + 1), func, args)
            self.event_list.append(event)

    def cancel(self):
        """
        Halt the series, deactivating each event in the batch.
        """
        self.active = False
        for event in self.event_list:
            event.cancel()


class Scheduler(object):
    """
    Manage scheduler events.
    """
    def __init__(self):
        self.event_list = []
        self.start_time = time.time()
        THE_TIME = self.start_time

    def add(self, delay, func, args=()):
        """
        Add a delayed function call to the schedule.  Delay is in seconds
        and may be a decimal.
        """
        ## create a new event object
        event = Event(delay, func, args)
        ## Do an in-order insertion
        insort(self.event_list, event)
        return event

    def age(self):
        """
        Return the age of the scheduler in seconds.
        """
        return gvar.THE_TIME - self.start_time

    def tick(self):
        """
        Fire and delete all events that have a schedule time < now.
        """
        ## Update the global time value
        gvar.THE_TIME = time.time()

        while self.event_list:
            ## Look at the first event
            event = self.event_list[0]
            ## Is is past time for it to fire?
            if event.when < gvar.THE_TIME:
                ## And is it still active?
                if event.active:
                    event.func(*event.args)
                ## and delete it from the list
                self.event_list.pop(0)
            else:
                ## all pending events are gone, let's get out of here
                break


#--[ Shared Instance ]---------------------------------------------------------

THE_SCHEDULER = Scheduler()

#------------------------------------------------------------------------------
