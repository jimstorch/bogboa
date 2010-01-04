# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/ai/brains.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from operator import itemgetter

from mudlib.eggtimer import EggTimer
from mudlib.lookup import find_body


class Brain(object):

    ## AI Parameters control this creature's tendency to:
    aggression = 0.0            ##  attack / retaliate
    mobility = 0.5              ##  give chase
    memory = 0.50               ##  forget
    evolution = 0.50            ##  use advanced abilities
    fealty = 0.50               ##  make faction-based decisions
    courage = 0.50              ##  keep fighting
    sight = 0.80                ##  see bodies
    hearing = 0.80              ##  hear bodies
    smell = 0.25                ##  smell bodies

    def __init__(self, body):

        self.like = {}
        self.timer = EggTimer()
        self.state = self._idle
        self.body = body


    def __call__(self):

        """When called, execute the active state."""

        self.state()


    #--------------------------------------------------------------------Events

    def encounter(self, body):

        """Activated when a body entered the same room."""

        self._see(body)
        self._hear(body)
        self._smell(body)


    def pain(self, body, amount):

        """Record a pain event and adj like accordingly."""

        curr = self.like.get(body.index, 0)
        self.like[body.index] = curr - ( amount * self.aggression )
        if self.state == self._idle:
            self._decide()

    def joy(self, body, amount):

        """Record a joy event and adj like accordingly."""

        curr = self.like.get(body.index, 0)
        self.like[body.index] = curr + amount
        if self.state == self._idle:
            self._decide()

    def stun(self, body, amount):

        """Halt brain activity and record the duration as dislike."""

        self.timer.set('stunned', amount)
        self.state = self._stunned
        self.pain(body, amount)

    def fetch(self, object):
        pass

    def drive(self, room):
        pass

    def fear(self, body, amount):
        pass

    def reset(self):
        pass

    def _see(self, body):

        """React (or not) to seeing a body."""

        if not self.like.has_key(body.index):
            #TODO add some faction testing here
            pass

    def _hear(self, body):
        pass

    def _smell(self, body):
        pass


    #--------------------------------------------------------------------Decide

    def _decide(self):

        """Imitate free will and choose a new state for the AI."""

        ## Sort our affinity for other bodies by dislike
        hated = sorted(self.like.iteritems(), key=itemgetter(1))

        if hated:
            enemy = hated[0]
            friend = hated[-1]


        else:
            return self._idle


    #--------------------------------------------------------------------States

    def _idle(self):
        """The default, do-nothing state"""
        return

    def _stunned(self):
        """Brain is temporarily non-reactive."""
        if self.timer.ready_check('stunned'):
            self.state = self._decide()

    def _driving(self):
        pass

    def _fetching(self):
        pass

    def _attacking(self):
        pass

    def _fleeing(self):
        pass

    def _seeking(self):
        pass



#-----------------------------------------------------------------Custom Brains


class ManiacBrain(Brain):

    """Subclassed brain that attacks anything."""

    aggression = 1.0
    mobility = 1.0


class UndeadBrain(Brain):

    """Subclassed brain that thinks like the undead."""

    aggression = .75
    mobility = .2
    sight = .50
    hearing = .05
    smell = .05


class PlantBrain(Brain):

    """Subclassed brain that just takes abuse."""

    mobility = 0.0
    aggression = 0.0
    evolution = 0.0
    sight = 0.0
    hearing = 0.0
    smell = 0.0
