##-----------------------------------------------------------------------------
##  File:       driver/clock/cycle.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from driver.clock.scheduler import THE_SCHEDULER


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
        """Half the cycle and the next event."""
        self.active = False        
        self.next_event.cancel()


    def pause(self):
        """Halt the cycle."""
        ## Currenly the same as cancel()
        self.cancel()


    def restart(self):
        """Begin the cycle again in 'delay' seconds."""
        self.active = True
        self._schedule()

        
