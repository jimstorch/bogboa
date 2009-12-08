# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/timer.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from shared import THE_TIME

##  The eggtimer class is used to track cooldowns of certain abilities.
##  It should be used for timers that ellaspse even while the character
##  if offline.


class Timer(object):

    """
    Simple class to track a dictionary of timers by string values.
    """

    def __init__(self):
        self.eggs = {}
        self.session_start = THE_TIME

    #-----------------------------------------------------------------Set Timer

    def set_timer(self, egg, duration):

        """
        Sets a timer by name and duration in seconds.
        """

        self.eggs[egg] = THE_TIME + duration

    #---------------------------------------------------------------Ready Check

    def ready_check(self, egg):

        """
        Boolean check to see if the named delay has elasped.
        """

        target = self.eggs.get(egg, 0)
        if target < THE_TIME:
            return True
        else:
            return False

    #-----------------------------------------------------------------Time Left

    def time_remaining(self, egg)

        """
        Given a timer name, returns the remaining time in seconds.
        """

        target = self.eggs.get(egg, 0)

        if target < THE_TIME:
            return 0
        else:
            return target - THE_TIME
