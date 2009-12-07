# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/entity.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import copy

from mudlib import shared
from mudlib import calendar
from mudlib.inventory import Bag
from mudlib.resource import ResourceManager


## Pronouns by Gender
_NOMINATIVE = {'male':'he', 'female':'she', 'neutral':'it', 'group':'they'}
_OBJECTIVE = {'male':'him', 'female':'her', 'neutral':'it', 'group':'them'}
_POSSESSIVE = {'male':'his', 'female':'her', 'neutral':'its', 'group':'their'}
_POS_NOUN = {'male':'his', 'female':'hers', 'neutral':'its', 'group':'theirs'}
_REFLEXIVE = {'male':'himself', 'female':'herself', 'neutral':'itself',
    'group':'themselves'}


class Entity(object):

    def __init__(self):


        self.name = None
        self.uuid = None
        self.client = None

        self.profile = None
        self.abilities = None
        self.bag = Bag()
        self.resource = ResourceManager()
        self.stats = None
        self.skills = None
        self.wardrobe = None
        self.target = None

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
            'room_name':self.get_room_name,
            'time':calendar.time_msg,
            'date':calendar.date_msg,
            }

    ##--[ Methods to support String Templates ]--------------------------------

    def __getitem__(self, key): return self.keywords[key]()

    def get_name(self):
        return self.profile['name']
    def get_alias(self):
        return self.profile['alias']
    def get_race(self):
        return self.profile['race']
    def get_guild(self):
        return self.profile['guild']
    def get_level(self):
        return self.profile['level']
    def get_gender(self):
        return self.profile['gender']
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
        return self.target.name if self.target else '<notar name>'
    def get_tar_race(self):
        return self.target.race if self.target else '<notar race>'
    def get_tar_guild(self):
        return self.target.guild if self.target else '<notar guild>'
    def get_tar_gender(self):
        return self.target.gender if self.target else '<notar gender>'
    def get_tar_level(self):
        return self.target.level if self.target else '<notar level>'
    def get_tar_nominative(self):
        return _NOMINATIVE[target.gender] if self.target else '<notar nom>'
    def get_tar_objective(self):
        return _OBJECTIVE[target.gender] if self.target else '<notar obj>'
    def get_tar_possessive(self):
        return _POSSESSIVE[target.gender] if self.target else '<notar pos>'
    def get_tar_possessive_noun(self):
        return _POS_NOUN[target.gender] if self.target else '<notar posn>'
    def get_tar_reflexive(self):
        return _REFLEXIVE[target.gender] if self.target else '<notar reflx>'
    def get_room_name(self):
        return self.room.name
