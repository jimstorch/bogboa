# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/actor/avatar.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
The player's identity in the game world. Inherits from BaseActor.
"""

from mudlib.actor.base_actor import BaseActor
from mudlib.dat import set_kv
from mudlib.dat import delete_kv
from mudlib.dat import delete_kv_category


class Avatar(BaseActor):

    def __init__(self, client):
        BaseActor.__init__(self)
        self.is_player = True
        self.client = client
        self.abilities = set()

    def prep(self):
        """
        Set calculated fields based on gear, race, guild, and level.
        """
        pass

    def send(self, msg):
        """
        Send message with caret color encoding.
        """
        self.client.send_cc(msg)

    def send_raw(self, msg):
        """
        Send message, ignore caret color codes.
        """
        self.client.send(msg)
            
    def send_wrapped(self, msg):
        """
        Send message with word wrapping and caret color codes.
        """
        self.client.send_wrapped(msg)

    def get_origin(self):
        """
        Return the IP address & port number of the player.
        """
        return self.client.addrport()

    #--[ Ability Authorizing ]------------------------------------------------

    def grant_ability(self, ability_name):
        """
        Authorize Avatar to use an ability and tell them.
        """
        if command_name not in self.commands:
            self.grant_ability_silent(ability_name)
            self.send('You receive a new ability: ^W%s^w\n' % 
                ability_name)

    def grant_ability_silent(self, ability_name):
        """
        Silently authorize an Avatar to use an ability.
        """
        self.abilities.add(ability_name)
        set_kv(self.uuid, 'abilities', ability_name)

    def revoke_ability(self, ability_name):
        """
        Dis-allow an Avatar to use an ability and tell them.
        """
        if ability_name in self.ability:
            self.revoke_ability_silent(ability_name)
            self.send("You lose a ability: ^y%s^w\n" % ability_name)

    def revoke_ability_silent(self, ability_name):
        """
        Silently dis-allow an Avatar to use an ability.
        """
        if ability_name in self.abilities:
            self.abilities.remove(ability_name)
            delete_kv(self.uuid, 'abilities', ability_name)

    def clear_abilities(self):
        """
        Remove all abilities from Avatar.
        """
        self.abilities.clear()
        delete_kv_category(self.uuid, 'abilities')

    def has_ability(self, ability_name):
        """
        Return True if Avatar has access to the given ability.
        """
        return ability_name in self.abilities
