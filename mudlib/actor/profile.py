# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/profile.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Base class to provide dictionary lookups for referencing profile attributes
in string templates.
"""

## Pronouns by Gender
_NOMINATIVE = {'male':'he', 'female':'she', 'neutral':'it', 'group':'they'}
_OBJECTIVE = {'male':'him', 'female':'her', 'neutral':'it', 'group':'them'}
_POSSESSIVE = {'male':'his', 'female':'her', 'neutral':'its', 'group':'their'}
_NOUN_POSSESSIVE = {'male':'his', 'female':'hers', 'neutral':'its', 
    'group':'theirs'}
_REFLEXIVE = {'male':'himself', 'female':'herself', 'neutral':'itself',
    'group':'themselves'}


class BaseProfile(object):

    def __init__(self):

        ## Children must provide the dictionary 'profile' as a class property

        ## Keywords for String Templates
        self.__keywords = {
            'name':self.get_name,
            'alias':self.get_alias,
            'race':self.get_race,
            'guild':self.get_guild,
            'gender':self.get_gender,
            'level':self.get_level,
            'nom':self.get_nom,
            'obj':self.get_obj,
            'pos':self.get_pos,
            'npos':self.get_npos,
            'reflx':self.get_reflx,
            }

    #---------------------------------------Methods to support String Templates

    def __getitem__(self, key): return self.__keywords[key]()

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


