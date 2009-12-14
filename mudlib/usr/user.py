# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/user.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""Base class for interacting with a human operator."""

from mudlib.sys import shared
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.sys.error import BogCmdError
from mudlib.world.entity import Entity
from mudlib.usr.verb import VERB_ALIAS
from mudlib.usr.verb import VERB_HANDLER


#------------------------------------------------------------------------Client

class User(object):

    def __init__(self, client):

        self.client = client            ## Network connection
        self.commands = set()           ## Permitted commands
        self.verb_args = []             ## arguments for the verb handlers


#    def __del__(self):

#        print "User destructor called"
#        pass

    #----------------------------------------------------------------------Send

    def send(self, msg):
        """Transmit text to the distant end, with word wrapping."""
        self.client.send_cc(msg)

    #--------------------------------------------------------------Send Wrapped

    def send_wrapped(self, msg):
        self.client_send_wrapped(msg)

    #----------------------------------------------------------------------Send

    def send_raw(self, msg):
        """Transmit raw text to the distant end."""
        self.client.send(msg)

    #-------------------------------------------------------------------whisper

    def whisper(self, msg):
        """Transmit msg wrapped in whisper color (dark green)."""
        self.client.send_cc('^g%s^w' % msg)

    #---------------------------------------------------------------------Prose

    def prose(self, msg):
        """Transmit msg wrapped in reading color (dark white)."""
        self.client.send_cc('^w%s^w' % msg)

    #--------------------------------------------------------------------Inform

    def inform(self, msg):
        """Transmit msg wrapped in informing color (bright white)."""
        self.client.send_cc('^W%s^w' % msg)

    #---------------------------------------------------------------------Alert

    def alert(self, msg):
        """Transmit msg wrapped in alert color (bright yellow)."""
        self.client.send_cc('^Y%s^w' % msg)

    #----------------------------------------------------------------------Warn

    def warn(self, msg):
        """Transmit msg wrapped in warn color (dark red)."""
        self.client.send_cc('^r%s^w' % msg)

    #----------------------------------------------------------------------Warn

    def exclaim(self, msg):
        """Transmit msg wrapped in exclaime color (bright red)."""
        self.client.send_cc('^R%s^w' % msg)


#    #---------------------------------------------------------------Send Pretty

#    def send_wrapped(self, msg):
#        """Transmit text to the distant end."""
##        self.client.send(word_wrap(msg, self.client.columns))
#        self.client.send(msg)

    #-----------------------------------------------------------Process Command

    def process_command(self):

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

            #self.prompt()

        else:
            self.verb_args = None
            #self.soft_prompt()

    #--------------------------------------------------------------------Origin

    def origin(self):

        """Return the client's IP address and Port Numnber."""

        return self.client.addrport()

    #----------------------------------------------------------------Deactivate

    def deactivate(self):

        """
        Kick the user from the server via the client.
        """

        self.client.deactivate()

    #--------------------------------------------------------Delayed Deactivate

    def delayed_deactivate(self):

        """
        Kick the user from the server in 1 second.
        """

        THE_SCHEDULER.add(1, self.client.deactivate)


    #-------------------------------------------------------------------Verbing

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

    #-------------------------------------------------------------Grant Command

    def grant_command(self, command_name):
        """Authorize player to use an command and tell them."""
        if command_name not in self.commands:
            self.commands.add(command_name)
            self.send('You receive a new command: ^W%s^w' % command_name)
        else:
            self.send("Oddness -- attempt to re-grant command '%s'." %
                command_name)

    #------------------------------------------------------------Revoke Command

    def revoke_command(self, command_name):
        """De-authorize player to use an command and tell them."""
        if command_name in self.commands:
            self.commands.remove(command_name)
            self.send("You lose a command: ^y%s^w" % command_name)

    #-----------------------------------------------------Revoke Command Silent

    def revoke_command_silent(self, command_name):
        """Silently de-authorize a player to use an command."""
        if command_name in self.commands:
            self.commands.remove(command_name)

    #------------------------------------------------------Grant Command Silent

    def grant_command_silent(self, ability_name):
        """Silently authorize a player to use an command."""
        self.command.add(command_name)

    #-------------------------------------------------------------Clear Command

    def clear_commands(self):
        """Remove all command from client."""
        self.commands.clear()

    #---------------------------------------------------------------Has Command

    def has_command(self, command_name):
        """Return True if client has access to the given command."""
        return command_name in self.commands
