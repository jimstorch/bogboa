# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/client.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

# connection --> client <-- avatar

#from lib.stringsub import StringSub
from mudlib.avatar import Avatar
from mudlib.verb import VERB_ALIAS
from mudlib.verb import VERB_HANDLER


#------------------------------------------------------------------------Client

class Client(object):

    def __init__(self):

        self.conn = None                ## Network connection 
        self.active = False             ## Delete during housekeeping?
        self.avatar = Avatar()          ## Player's character in the world
        self.avatar.client = self
        self.verb_args = None           ## arguments for the verb handlers


        ## Dictionary-like object used for string substitutions
        #self.stringsub = StringSub(self)    


    #--------------------------------------------------------------------Inform

    def send(self, msg):
        self.conn.send(msg) 

    #-----------------------------------------------------------Process Command

    def process_command(self):
        cmd = self.conn.get_command()
        if cmd:
            verb, args = self._verbing(cmd)
            ## Did we get a verb and it is authozied?
            if verb and verb in self.abilities:
                self.verb_args = args
                handler = VERB_HANDLER[verb]
                handler(self)

            else:
                self.send("Unknown action.")
                
            self.prompt()

        else:
            self.verb_args = None
            self.soft_prompt()
                    

    #----------------------------------------------------------------Deactivate

    def deactivate(self):
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
    


