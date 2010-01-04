# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/mob.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import shared
from mudlib.actor.base_actor import BaseActor

"""
Non-Player Characters.  Inherits from Actor.
"""


class Mob(BaseActor):

    def __init__(self):

        BaseActor.__init__(self):


    def get_adj_stat(self, stat_name):
        """
        Stats for mobs are         
        """
        base_stat = level * 2
        adj_stat = self.get_stat(stat_name)
        return base_stat + adj_stat


    #-------------------------------------------------------------------Scaling

    def get_stat(self, stat_name):
        return self.stats.get(stat_name, 0.0)
