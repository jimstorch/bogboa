# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/profile.py
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
_POS_NOUN = {'male':'his', 'female':'hers', 'neutral':'its', 'group':'theirs'}
_REFLEXIVE = {'male':'himself', 'female':'herself', 'neutral':'itself',
    'group':'themselves'}


class Profile(object):

    def __init__(self):

        ## Children must provide the dictionary 'profile' as a class property

        ## Keywords for String Templates
        self.keywords = {
            'name':self.get_name,
            'alias':self.get_alias,
            'race':self.get_race,
            'guild':self.get_guild,
            'gender':self.get_gender,
            'level':self.get_level,
            'nom':self.get_nominative,
            'obj':self.get_objective,
            'pos':self.get_possessive,
            'posn':self.get_possessive_noun,
            'reflx':self.get_reflexive,
            'tar_name':self.get_tar_name,
            'tar_race':self.get_tar_race,
            'tar_guild':self.get_tar_guild,
            'tar_level':self.get_tar_level,
            'tar_nom':self.get_tar_nominative,
            'tar_obj':self.get_tar_objective,
            'tar_pos':self.get_tar_possessive,
            'tar_posn':self.get_tar_possessive_noun,
            'tar_reflx':self.get_tar_reflexive,
            }

    #---------------------------------------Methods to support String Templates

    def __getitem__(self, key): return self.keywords[key]()

    def get_name(self):
        return self.profile['name']

    def get_alias(self):
        return self.profile['alias']

    def get_race(self):
        return self.profile['race']

    def get_gender(self):
        return self.profile['gender']

    def get_guild(self):
        return self.profile['guild']

    def get_level(self):
        return self.profile['level']


    def get_nominative(self):
        return _NOMINATIVE[self.profile['gender']]

    def get_objective(self):
        return _OBJECTIVE[self.profile['gender']]

    def get_possessive(self):
        return _POSSESSIVE[self.profile['gender']]

    def get_possessive_noun(self):
        return _POSSESSIVE_NOUN[self.profile['gender']]

    def get_reflexive(self):
        return _REFLEXIVE[self.profile['gender']]

    def get_tar_name(self):
        if target:
            return self.target.get_name()
        else:
            return '<notarget name>'

    def get_tar_race(self):
        if target:
            return self.target.get_race()
        else:
            return '<notarget race>'

    def get_tar_gender(self):
        if target:
            return self.target.get_gender()
        else:
            return '<notarget gender>'

    def get_tar_guild(self):
        if target:
            return self.target.get_guild()
        else:
            return '<notarget guild>'

    def get_tar_level(self):
        if target:
            return self.target.get_level()
        else:
            return '<notarget level>'

    def get_tar_nominative(self):
        if target:
            return _NOMINATIVE[target.get_gender]
        else:
            return '<notarget nominative>'

    def get_tar_objective(self):
        if target:
            return _OBJECTIVE[target.get_gender()]
        else:
            return '<notarget objective>'

    def get_tar_possessive(self):
        if target:
            return _POSSESSIVE[target.get_gender()]
        else:
            return '<notar possessive>'

    def get_tar_possessive_noun(self):
        if target:
            return _POS_NOUN[target.get_gender()]
        else:
            return '<notar possessive noun>'

    def get_tar_reflexive(self):
        if target:
            return _REFLEXIVE[target.get_gender()]
        else:
            return '<notarget reflexive>'
