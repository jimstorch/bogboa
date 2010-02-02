# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/base_actor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Base Class for Avatars and Mobs.
"""

from mudlib import gvar
#from mudlib.actor.inventory import Bag
#from mudlib.actor.inventory import Outfit

## Pronouns by Gender
_NOMINATIVE = {'male':'he', 'female':'she', 'neutral':'it', 'group':'they'}
_OBJECTIVE = {'male':'him', 'female':'her', 'neutral':'it', 'group':'them'}
_POSSESSIVE = {'male':'his', 'female':'her', 'neutral':'its', 'group':'their'}
_NOUN_POSSESSIVE = {'male':'his', 'female':'hers', 'neutral':'its',
    'group':'theirs'}
_REFLEXIVE = {'male':'himself', 'female':'herself', 'neutral':'itself',
    'group':'themselves'}


class BaseActor(object):

    def __init__(self):
        self.room = None
        self.is_player = False
        ## Character Stats;
        ## key = stat name, value = amount
        self.stats = {}
        ## Carried items;
        ## key = Item Obj, value = item count
        self.carried = {}
        ## Worn Items;
        ## key = slot name, value = Item Obj
        self.worn = {}
        ## Burden = adjusted weight of carried items + worn items
        self.burden = 0.0

    def get_burden(self):
        """
        Return the actor's burden of carried and worn items.
        """
        return self.bag.burden + self.outfit.burden

    def get_alias(self):
        """
        Actor's alias.
        """
        return self.profile['alias']

    def get_gender(self):
        """
        Actor's gender as a string.
        """
        return self.profile['gender']

    def get_guild(self):
        """
        Actor's guild as a string.
        """
        return self.profile['guild']

    def get_guild_obj(self):
        """
        Actor's guild object or None.
        """
        return gvar.GUILDS.get(self.get_guild(), None)

    def get_level(self):
        """
        Actor's level as an integer value.
        """
        return int(self.profile['level'])

    def get_name(self):
        """
        Actor's name.
        """
        return self.profile['name']

    def get_race(self):
        """
        Actor's race as a string.
        """
        return self.profile['race']

    def get_room_uuid(self):
        """
        UUID of the Actor's room.
        """
        return self.profile['room']

    def get_room_obj(self):
        """
        Actor's Room object.
        """
        return gvar.ROOMS[self.get_room_uuid()]


    def get_race_obj(self):
        """
        Actor's Race object or None.
        """
        return gvar.RACES[self.get_race()]

    ##-----------------------------------------------------------------Pronouns

    def get_nom(self):
        """
        Actor's nominative form; he, she, it, they.
        """
        return _NOMINATIVE[self.get_gender()]

    def get_obj(self):
        """
        Actor's objective form; him, her, it, them.
        """
        return _OBJECTIVE[self.get_gender()]

    def get_pos(self):
        """
        Actor's possessive form; his, her, its, their.
        """
        return _POSSESSIVE[self.get_gender()]

    def get_npos(self):
        """
        Actor's possessive form following the noun; his, hers, its, theirs.
        """
        return _NOUN_POSSESSIVE[self.get_gender()]

    def get_reflx(self):
        """
        Actor's reflexive form; himself, herself, itself, themselves.
        """
        return _REFLEXIVE[self.get_gender()]
