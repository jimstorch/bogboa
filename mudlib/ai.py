# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/ai.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from operator import itemgetter

from mudlib.eggtimer import EggTimer
from mudlib.lookup import find_mobs


class Brain(object):

    def __init__(self):

        self.like = {}
        self.timer = EggTimer()
        self.state = self._idle


    def __call__(self):

        """When called, execute the active state."""

        self.state()


    #--------------------------------------------------------------------Events

    def see(self, mob):
        pass

    def hear(self, mob):
        pass

    def pain(self, mob, amount):

        """Record a pain event and adj hate accordingly."""

        curr = self.like.get(mob.name, 0)
        self.like[mob.name] = curr - amount
        if self.state == self._idle:
            self._decide()

    def fear(self, mob, amount):
        pass

    def joy(self, mob, amount):
        pass

    def stun(self, mob, amount):

        self.timer.set('stunned', amount)
        self.state = self._stunned
        self.pain(mob, amount)

    def reset(self):
        pass

    def fetch(self, object):
        pass


    #--------------------------------------------------------------------Decide

    def _decide(self):

        """Imitate free will and choose a new state for the AI."""

        ## Sort our affinity for other mobs by dislike 
        hated = sorted(self.like.iteritems(), key=itemgetter(1))

        if hated:
            enemy = hated[0]        
            friend = hated[-1]  

            if enemy[1] < 0:
                
                                
        else:
            return self._idle
  

    #--------------------------------------------------------------------States


    def _idle(self):

        """The default, do-nothing state"""

        pass

    def _stunned(self):

        """Brain is temporarily non-reactive."""    

        if self.timer.ready_check('stunned'):
            self.state = self._decide()           

    def _attacking(self):
        pass

    def _fleeing(self):
        pass

    def _seeking(self):
        pass

    
