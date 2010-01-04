# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/player.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
User derived class that reprepresents visitor's during play state.
"""

from mudlib.usr import BaseUser
from mudlib.dat import set_kv
from mudlib.dat import delete_kv
from mudlib.dat import delete_kv_category


class Player(BaseUser):

    def __init__(self, client, avatar):

        BaseUser.__init__(self, client)
        self.avatar = avatar
        self.change_state('user_command')


    #----------------------------------------------------------Command Handling

    def grant_command(self, command_name):
        """
        Authorize User to use a command and tell them.
        """
        if command_name not in self.commands:
            self.grant_command_silent(command_name)
            self.send('You receive a new command: ^W%s^w' % command_name)

    def grant_command_silent(self, ability_name):
        """
        Silently authorize a User to use an command.
        """
        self.command.add(command_name)
        set_kv(self.uuid, 'commands', command_name)

    def revoke_command(self, command_name):
        """
        Dis-allow User to use a command and tell them.
        """
        if command_name in self.commands:
            self.revoke_command_silent(command_name)
            self.send("You lose a command: ^y%s^w" % command_name)

    def revoke_command_silent(self, command_name):
        """
        Silently dis-allow a User to use an command.
        """
        if command_name in self.commands:
            self.commands.remove(command_name)
            delete_kv(self.uuid, 'commands', command_name)

    def clear_commands(self):
        """
        Remove all command from User.
        """
        self.commands.clear()
        delete_kv_category(self.uuid, 'commands')

    def has_command(self, command_name):
        """
        Return True if User has access to the given command.
        """
        return command_name in self.commands
