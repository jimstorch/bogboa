# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/resource.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import shared
from mudlib.sys.error import BogCmdError, BogDepleteCond


"""Generic resource management."""


class Resource(object):

    def __init__(self, displayed_name, current=0, maximum=0, regen=0, ungen=0):

        self.displayed_name = displayed_name    ## Name shown to user in errors
        self.current = current                  ## Current resource level
        self.maximum = maximum                  ## Maximum resource level
        self.regen = regen                      ## Regeneration per second
        self.ungen = ungen                      ## Decay rate for overages
        self.last_tick = shared.THE_TIME
                  
    def deduct(self, name, amount):
        """
        Given a name and amount, reduce by that much.
        Throws BogCmdError if current is insufficient, e.g. mana.
        """
        if amount >= self.current:
            raise BogCmdError('Insufficent %s.' % self.displayed_name)
        else:
            self.current -= amount

    def deplete(self, name, amount):
        """
        Given a name and amount, reduce by that much.
        Throws BogDepleteCond if resource is exhausted, e.g. life.
        """
        self.current -= amount
        if self.current <= 0:
            raise BogDepleteCond('No %s remaining.' % self.displayed_name)

    def add(self, amount):
        """
        Increase resource towards max.
        """
        if (self.current + amount) < self.maximum:
            self.current += amount
        else:
            self.current = maximum

    def bonus(self, amount):
        """
        Increase resource, possibly beyond max.
        """
        self.current += amount

    def prime(self, amount):
        """
        Set maximum and current to amount.
        """
        self.maximum = amount
        self.current = amount

    def percent(self):
        """
        Give a name, return the percentage of resource relative to max.
        """
        return (self.maximum / 100.0) * self.current

    def tick(self):
        """
        Regenerate resources based on elasped seconds.
        """
        t = THE_TIME - self.last_tick
        ## Only process regenerations of more than one second
        if t >= 1.0:
            if self.current <= self.maximum:
                self.current += (t * self.regen)
                if self.current > self.maximum:
                    self.current = self.maximum
            ## If max exceeded, decay it by the ungen rate
            else:
                self.current -= (t * self.ungen)
                if self.current < self.maximum:
                    self.current = self.maximum
            self.last_time = shared.THE_TIME


