# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/actor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.actor.resource import Resource
from mudlib.actor.skill import Skill

## Pronouns by Gender
_NOMINATIVE = {'male':'he', 'female':'she', 'neutral':'it', 'group':'they'}
_OBJECTIVE = {'male':'him', 'female':'her', 'neutral':'it', 'group':'them'}
_POSSESSIVE = {'male':'his', 'female':'her', 'neutral':'its', 'group':'their'}
_NOUN_POSSESSIVE = {'male':'his', 'female':'hers', 'neutral':'its', 
    'group':'theirs'}
_REFLEXIVE = {'male':'himself', 'female':'herself', 'neutral':'itself',
    'group':'themselves'}


"""
Base Class for PCs and NPCs.
"""

class Actor(object):

    def __init__(self):

        ## Profile
        self.name   = '_spawn_'
        self.alias  = '_alias_'
        self.race   = '_race_'
        self.gender = 'neutral'
        self.guild  = '_guild_'
        self.level  = 1

        ## 
        self.abilities = set()
        self.stats = {}
        self.resources = {}         # Dictionary of resource objects by name
        self.worn = {}
        self.carried = {}

        ## 
        self.target = None


    #-------------------------------------------------------------------Scaling

    def get_adj_stat(self, stat_name):
        return self.stats.get(stat_name, 0.0)


    #---------------------------------------Methods to support action messaging

    def get_name(self): return self.name
    def get_alias(self): return self.alias
    def get_race(self): return self.race
    def get_gender(self): return self.gender
    def get_guild(self): return self.guild
    def get_level(self): return self.level
    def get_nom(self): return _NOMINATIVE[self.gender]
    def get_obj(self): return _OBJECTIVE[self.gender]
    def get_pos(self): return _POSSESSIVE[self.gender]
    def get_npos(self): return _NOUN_POSSESSIVE[self.gender]
    def get_reflx(self): return _REFLEXIVE[self.gender]
    
