# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/brain.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from operator import itemgetter

from mudlib.eggtimer import EggTimer
from mudlib.lookup import find_mobs


class Brain(object):
    
    ## AI Parameters control this creature's tendency to:
    aggression = 0.0            ##  attack / retaliate 
    mobility = 0.5              ##  give chase
    memory = 0.50               ##  forget
    evolution = 0.50            ##  use advanced abilities
    fealty = 0.50               ##  make faction-based decisions
    courage = 0.50              ##  keep fighting
    sight = 0.80                ##  see mobs
    hearing = 0.80              ##  hear mobs
    smell = 0.25                ##  smell mobs

    def __init__(self, body):

        self.like = {}
        self.timer = EggTimer()
        self.state = self._idle
        self.body = body


    def __call__(self):

        """When called, execute the active state."""

        self.state()


    #--------------------------------------------------------------------Events

    def encounter(self, mob):

        """Activated when a mob entered the same room."""

        self._see(mob)
        self._hear(mob)
        self._smell(mob)


    def pain(self, mob, amount):

        """Record a pain event and adj like accordingly."""

        curr = self.like.get(mob.index, 0)
        self.like[mob.index] = curr - ( amount * self.aggression )
        if self.state == self._idle:
            self._decide()

    def joy(self, mob, amount):

        """Record a joy event and adj like accordingly."""

        curr = self.like.get(mob.index, 0)
        self.like[mob.index] = curr + amount
        if self.state == self._idle:
            self._decide()

    def stun(self, mob, amount):

        """Halt brain activity and record the duration as dislike."""

        self.timer.set('stunned', amount)
        self.state = self._stunned
        self.pain(mob, amount)

    def fetch(self, object):
        pass

    def drive(self, room):
        pass

    def fear(self, mob, amount):
        pass

    def reset(self):
        pass

    def _see(self, mob):

        """React (or not) to seeing a mob."""

        if not self.like.has_key(mob.index):
            #TODO add some faction testing here
            pass
                        
    def _hear(self, mob):
        pass

    def _smell(self, mob):
        pass


    #--------------------------------------------------------------------Decide

    def _decide(self):

        """Imitate free will and choose a new state for the AI."""

        ## Sort our affinity for other mobs by dislike 
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


    
