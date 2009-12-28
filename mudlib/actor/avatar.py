# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/avatar.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import shared
from mudlib.actor.base_actor import Actor


"""
The player's identity in the game world. Inherits from Actor.
"""


class Avatar(Actor):

    def __init__(self):

        Actor.__init__(self)
        self.skills = {}


    def get_stat(self, stat_name):
        
        return self.stats.get(stat_name, 0.0)


    def grant_ability(self, ability_name):
        self.abilities.
