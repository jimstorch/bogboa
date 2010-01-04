# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/base_user.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Base class for interacting with a human operator.
"""

from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.sys.error import BogCmdError
from mudlib.usr.verb import VERB_ALIAS
from mudlib.usr.verb import VERB_HANDLER


class BaseUser(object):

    def __init__(self, client):

        self.client = client            ## Network connection
        self.commands = set()           ## Permitted commands
        self.verb_args = []             ## arguments for the verb handlers

#    def __del__(self):
#        print "User destructor called"


    #------------------------------State switching for alternate input handlers

    def change_state(self, state):
        func_name = 'state__' + state
        self.state = func_name

    def cmd_driver(self):
        ## call the driver method for current state via class introspection
        self.__class__.__dict__[self.state](self)

    def _fsm_do_nothing(self):
        """Do nothing driver for users that being kicked."""
        pass

    #----------------------------------------------Various text sending methods

    def send(self, msg):
        """Transmit text to the distant end, with word wrapping."""
        self.client.send_cc(msg)

    def send_wrapped(self, msg):
        self.client_send_wrapped(msg)

    def send_raw(self, msg):
        """Transmit raw text to the distant end."""
        self.client.send(msg)

    def whisper(self, msg):
        """Transmit msg wrapped in whisper color (dark green)."""
        self.client.send_cc('^g%s^w' % msg)

    def prose(self, msg):
        """Transmit msg wrapped in reading color (dark white)."""
        self.client.send_wrapped('^w%s^w' % msg)

    def inform(self, msg):
        """Transmit msg wrapped in informing color (bright white)."""
        self.client.send_cc('^W%s^w' % msg)

    def alert(self, msg):
        """Transmit msg wrapped in alert color (bright yellow)."""
        self.client.send_cc('^Y%s^w' % msg)

    def warn(self, msg):
        """Transmit msg wrapped in warn color (dark red)."""
        self.client.send_cc('^r%s^w' % msg)

    def exclaim(self, msg):
        """Transmit msg wrapped in exclaime color (bright red)."""
        self.client.send_cc('^R%s^w' % msg)

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
        self.change_state('do_nothing')
        THE_SCHEDULER.add(1, self.client.deactivate)

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

    def state__user_command(self):
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
