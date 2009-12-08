# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/character.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import copy

from mudlib import shared
from mudlib.world import calendar
from mudlib.usr.inventory import Bag
from mudlib.resource import ResourceManager
from mublib.world.entity import Entity


class Character(Entity):

    def __init__(self):
        pass


    #--------------------------------------------------------------------------
    #   Convenience Hooks for Client Methods
    #--------------------------------------------------------------------------

    #-------------------------------------------------------------Clear Command

    def clear_commands(self):
        """Remove all command from client."""
        if self.is_player:
            self.mind.clear_commands()

    #-------------------------------------------------------------Grant Command

    def grant_command(self, command_name):
        """Authorize player to use an command and tell them."""
        if self.is_player:
            self.mind.grant_command(command_name)

    #------------------------------------------------------Grant Command Silent

    def grant_command_silent(self, command_name):
        """Silently authorize a player to use an command."""
        if self.is_player:
            self.mind.grant_command_silent(command_command)

    #---------------------------------------------------------------Has Command

    def has_command(self, command_name):
        if self.is_player:
            return self.mind.has_command(command_name)
        else:
            return False

    #------------------------------------------------------------Revoke Command

    def revoke_command(self, command_name):
        """De-authorize player to use an command and tell them."""
        if self.is_player:
            self.mind.revoke_command(command_name)

    #-----------------------------------------------------Revoke Command Silent

    def revoke_command_silent(self, command_name):
        """Silently de-authorize a player to use an command."""
        if self.is_player:
            self.mind.revoke_command_silent(command_name)

    #----------------------------------------------------------------------Send

    def send(self, msg):
        if self.is_player:
            self.mind.send(msg)

    #----------------------------------------------------------------------Send

    def send_nowrap(self, msg):
        if self.is_player:
            self.mind.send_nowrap(msg)
