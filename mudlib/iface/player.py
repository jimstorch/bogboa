# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/player.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

# Client --> Player <-- Character

import shared
from driver.error import BogCmdError
from mudlib.entity import Entity
from mudlib.verb import VERB_ALIAS
from mudlib.verb import VERB_HANDLER

#from driver.decorate import word_wrap


#------------------------------------------------------------------------Client

class Player(object):

    def __init__(self):

        self.client = None              ## Network connection
        self.active = False             ## Delete during housekeeping?
        #self.login_attempts = 0
        #self.name = 'Anonymous'         ## Changed to body name later

        ## Create and link a fresh body
        self.body = Body()              ## Player's character in the world
        self.body.is_player = True
        self.body.mind = self
        self.commands = set()           ## Permitted commands
        self.verb_args = []             ## arguments for the verb handlers
        self.last_tell = None           ## used for replies

        ## Dictionary-like object used for string substitutions
        #self.stringsub = StringSub(self)

    #----------------------------------------------------------------------Send

    def send(self, msg):
        """Transmit text to the distant end with word wrapping."""
        self.client.send(msg)

    #---------------------------------------------------------------Send Nowrap

    def send_nowrap(self, msg):
        """Transmit text to the distant end, without word wrapping."""
        self.client.send_nowrap(msg)


    #-------------------------------------------------------------------whisper

    def whisper(self, msg):
        """Transmit msg wrapped in whisper color (dark green)."""
        self.client.send('^g%s^w' % msg)

    #---------------------------------------------------------------------Prose

    def prose(self, msg):
        """Transmit msg wrapped in reading color (dark white)."""
        self.client.send('^w%s^w' % msg)

    #--------------------------------------------------------------------Inform

    def inform(self, msg):
        """Transmit msg wrapped in informing color (bright white)."""
        self.client.send('^W%s^w' % msg)

    #---------------------------------------------------------------------Alert

    def alert(self, msg):
        """Transmit msg wrapped in alert color (bright yellow)."""
        self.client.send('^Y%s^w' % msg)

    #----------------------------------------------------------------------Warn

    def warn(self, msg):
        """Transmit msg wrapped in warn color (dark red)."""
        self.client.send('^r%s^w' % msg)

    #----------------------------------------------------------------------Warn

    def exclaim(self, msg):
        """Transmit msg wrapped in exclaime color (bright red)."""
        self.client.send('^R%s^w' % msg)


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


    #------------------------------------------------------------------Get Room

    def get_room(self):

        """Return the room object the client's body is in."""

        return self.body.room

    #------------------------------------------------------------------Get Body

    def get_body(self):

        """Return the client's body."""

        return self.body

    #--------------------------------------------------------------------Origin

    def origin(self):

        """Return the client's IP address and Port Numnber."""

        return self.client.addrport()

    #----------------------------------------------------------------Deactivate

    def deactivate(self):
        """Client disconnected or was kicked."""
        ## Unlink the player's body for garbage collecting

        if self.body and self.body.room:
            self.body.room.on_exit(self.body)

        if self.body and self.body.mind:
            self.body.mind = None
        self.body = None
        ## Remove from the name lookup
        if self.name.lower() in shared.BY_NAME:
            del shared.BY_NAME[self.name.lower()]
        ## Schedule for cleanup via driver.monitor.test_connections()
        self.active = False
        self.client.active = False

#    #--------------------------------------------------------------------Prompt

#    def prompt(self):
#        """Transmit a newline and a prompt"""
#        #self.send('\n')
#        #self.soft_prompt()

#    #---------------------------------------------------------------Soft Prompt

#    def soft_prompt(self):
#        """Called when a leading new-line is not desired"""
#        #self.send('> ', lf=False)

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
