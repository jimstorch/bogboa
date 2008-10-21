##-----------------------------------------------------------------------------
##  File:       driver/clock/series.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from driver.clock.scheduler import THE_SCHEDULER

# Series(5, 2, print_msg, ('Hi there',))  

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

        """Halt the series, deactivating each event in the batch."""

        self.active = False
        for event in self.event_list:
            event.cancel()

       
