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

from mudlib.sys import RACES
from mudlib.sys import GUILDS
from mudlib.actor.base_actor import BaseActor


class Avatar(BaseActor):

    def __init__(self):
        BaseActor.__init__(self)
        self.commands = set()

    def grant_ability(self, ability_name):
        self.abilities

    #----------------------------------------------------------Command Handling

    def grant_command(self, command_name):
        """Authorize Avatar to use an command and tell them."""
        if command_name not in self.commands:
            self.commands.add(command_name)
            self.send('You receive a new command: ^W%s^w' % command_name)
        else:
            self.send("Oddness -- attempt to re-grant command '%s'." %
                command_name)

    def revoke_command(self, command_name):
        """De-authorize player to use an command and tell them."""
        if command_name in self.commands:
            self.commands.remove(command_name)
            self.send("You lose a command: ^y%s^w" % command_name)

    def revoke_command_silent(self, command_name):
        """Silently de-authorize a player to use an command."""
        if command_name in self.commands:
            self.commands.remove(command_name)

    def grant_command_silent(self, ability_name):
        """Silently authorize a player to use an command."""
        self.command.add(command_name)

    def clear_commands(self):
        """Remove all command from client."""
        self.commands.clear()

    def has_command(self, command_name):
        """Return True if client has access to the given command."""
        return command_name in self.commands

    def _verbing(self, cmd):
        """
        'Verbing weirds language'
        -- Calvin and Hobbes

        Split a command line into an array of words and convert the first
        one into the One True Verb(tm).
        """
        words = cmd.split()
        count = len(words)
        if count == 0:
            verb = None
            args = []
        elif count == 1:
            verb = words[0].lower()
            args = []
        else:
            verb = words[0].lower()
            args = words[1:]
        one_true_verb = VERB_ALIAS.get(verb, None)
        return (one_true_verb, args)

    def _fsm_user_command(self):
        """
        Retrieve a line of text sent from the distant end and attempt to
        execute as a game command, with or without additional arguments.
        """
        cmd = self.client.get_command()
        if cmd:
            verb, args = self._verbing(cmd)
            ## Did we get a verb and it is authozied?
            if verb and verb in self.commands:
                self.verb_args = args
                ## Find the function mapped to this verb
                handler = VERB_HANDLER[verb]
                ## and call it, passing it the client
                try:
                    handler(self)
                except BogCmdError, error:
                    self.alert(error)
            else:
                self.alert("Unknown action.")
        else:
            self.verb_args = None
