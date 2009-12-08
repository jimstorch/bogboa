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

#----------------------------------------------------------------------Resource

class Resource(object):

    """Resource tracking class."""

    def __init__(self, displayed_name):

        self.displayed_name = displayed_name    ## Name shown to user in errors
        self.current = 0.0                      ## Current resource level
        self.max = 0.0                          ## Maximum resource level
        self.regen = 0.0                        ## Regeneration per second
        self.ungen = 0.0                        ## Decay rate for overages


#--------------------------------------------------------------Resource Manager

## Currently every resource is on the same timer although each can have a
## different regen rate.  This might be a problem is temporay resources are
## created during gameplay.  If which case, the timer could be moved to the
## Resource object instead.

class ResourceManager(object):

    """Manages multiple resources by name."""

    def __init__(self):

        self.resources = {}
        self.last_tick = shared.THE_TIME

    def create_resource(self, name, displayed_name=None):
        """
        Given a name and an optional displayed_name,
        create a new resource tracker.
        """
        if displayed_name == None:
            displayed_name = name
        self.resources[name] = Resource(displayed_name)

    def set_current(self, name, amount):
        """Given a name and an amount, sets the current level."""
        self.resources[name].current = amount

    def set_max(self, name, amount):
        """Given a name and an amount, sets the resource maximum."""
        res = self.resources[name]
        res.max = amount
        if res.current > amount:
            res.current = amount

    def set_regen(self, name, rate):
        """Given a name and a value, sets the current regen per second."""
        self.resources[name].regen = rate

    def set_ungen(self, name, rate):
        """Given a name and a value, sets the current ungen per second."""
        self.resources[name].regen = rate

    def check_avail(self, name, amount):
        """Given a name and amount, if available boolean."""
        res = self.resources[name]
        return bool(res.current >= amount)

    def deduct(self, name, amount):
        """
        Given a name and amount, reduce by that much.
        Throws BogCmdError if current is insufficient, e.g. mana.
        """
        res = res.resources[name]
        if amount >= res.current:
            raise BogCmdError('Insufficient %s available.' % res.name)

        else:
            res.current -= amount

    def deplete(self, name, amount):
        """
        Given a name and amount, reduce by that much.
        Throws BogDepleteError if resource is exhausted, e.g. life.
        """
        res = res.resources[name]
        res.current -= amount

        if res.current <= 0:
            raise BogDepleteCond('No %s remaining.' % res.name)

    def add(self, name, amount):
        """Given a name and amount, increase resource towards max."""
        res = self.resources[name]
        if (res.current + amount) < res.max:
            res.current += amount
        else:
            res.current = max

    def bonus(self, name, amount):
        """Given a name and amount, increase resource possibly beyond max."""
        res = self.resources[name]
        res.current += amount

    def percent(self, name):
        """Give a name, return the percentage of resource relative to max."""
        res = self.resources[name]
        return (res.max / 100.0) * res.current

    def current(self, name):
        """Give a resource name, return the maximum amount."""
        res = self.resources[name]
        return res.max

    def maximum(self, name):
        """Give a resource name, return the current amount."""
        res = self.resources[name]
        return res.current

    def tick(self):
        """Regenerate resources based on elasped seconds."""
        t = THE_TIME - self.last_tick
        ## Only process regenerations of more than one second
        if t >= 1.0:
            for res in self.values():
                ## Increase by the regen rate
                if res.current <= res.max:
                    res.add(t * res.regen)
                ## If max exceeded, decay it by the ungen rate
                else:
                    res.current -= (t * res.ungen)

            self.last_time = shared.THE_TIME

    def db_save(self, uuid):
        """Write current resource amounts to the database."""
        pass

    def db_load(self, uuid):
        """Retrieve the current resource amounts from the database."""
        pass
