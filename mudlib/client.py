# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/client.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

# connection --> client <-- body

import shared
from mudlib.body import Body
from mudlib.verb import VERB_ALIAS
from mudlib.verb import VERB_HANDLER


#------------------------------------------------------------------------Client

class Client(object):

    def __init__(self):

        self.conn = None                ## Network connection 
        self.active = False             ## Delete during housekeeping?
        self.login_attempts=0
        self.name = 'Anonymous'         ## Changed to body name later     

        ## Create and link a fresh body
        self.body = Body()              ## Player's character in the world
        self.body.is_player = True
        self.body.mind = self
        self.commands = set()           ## Permitted commands   
        self.verb_args = None           ## arguments for the verb handlers

        ## Dictionary-like object used for string substitutions
        #self.stringsub = StringSub(self)    

    #----------------------------------------------------------------------Send

    def send(self, msg):
        """Transmit text to the distant end."""
        self.conn.send(msg)

    #-----------------------------------------------------------Process Command

    def process_command(self):

        """
        Retrieve a line of text sent from the distant end and attempt to
        execute as a game command, with or without additional arguments.
        """         

        cmd = self.conn.get_command()

        if cmd:
            verb, args = self._verbing(cmd)
            ## Did we get a verb and it is authozied?
            if verb and verb in self.commands:
                self.verb_args = args
                ## Find the function mapped to this verb
                handler = VERB_HANDLER[verb]
                ## and call it, passing it the client
                handler(self)

            else:
                self.send("Unknown action.")
                
            self.prompt()

        else:
            self.verb_args = None
            self.soft_prompt()

    #----------------------------------------------------------------Deactivate

    def deactivate(self):
        """Client disconnected or was kicked."""
        ## Unlink the player's body for garbage collecting

        if self.body and self.body.room_uuid:
            shared.ROOMS[self.body.room_uuid].on_exit(self.body)

        if self.body and self.body.mind:
            self.body.mind = None        
        self.body = None #TODO: remember to delete from BODIES too
        ## Schedule for cleanup via driver.monitor.test_connections()
        self.active = False
        self.conn.active = False

    #--------------------------------------------------------------------Prompt

    def prompt(self):
        """Transmit a newline and a prompt"""
        self.send('\n')
        self.soft_prompt()

    #---------------------------------------------------------------Soft Prompt

    def soft_prompt(self):
        """Called when a leading new-line is not desired"""
        self.send('> ')

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
            self.send('\nYou receive a new command: %s' % command_name)
        else:
            self.send("\nOddness -- attempt to re-grant command '%s'." %
                command_name)

    #------------------------------------------------------------Revoke Command

    def revoke_command(self, command_name):
        """De-authorize player to use an command and tell them."""
        if command_name in self.commands:
            self.commands.remove(command_name)
            self.send("\nYou lose a command: %s" % command_name)

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


