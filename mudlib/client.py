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
        self.verb_args = None           ## arguments for the verb handlers

        ## Dictionary-like object used for string substitutions
        #self.stringsub = StringSub(self)    

    #----------------------------------------------------------------------Send

    def send(self, msg):
        self.conn.send(msg)

    #-----------------------------------------------------------Grant Abilities

    def grant_ability(self, ability_name):
        """Authorize player to use an ability and tell them."""
        if ability_name not in self.avatar.abilities:
            self.avatar.abilities.add(ability_name)
            self.send('\nYou receive a new ability: %s' % ability_name)
        else:
            self.send("\nOddness -- attempt to re-grant ability '%s'." %
                ability_name)

    #------------------------------------------------------Grant Ability Silent

    def grant_ability_silent(self, ability_name):
        """Silently authorize a player to use an ability."""
        self.avatar.abilities.add(ability_name)        

    #-----------------------------------------------------------Clear Abilities

    def clear_abilities(self):
        """Remove all abilities from player."""
        self.avatar.abilities.clear()

    #---------------------------------------------------------------Has Ability

    def has_ability(self, ability_name):
        return ability_name in self.avatar.abilities

    #-----------------------------------------------------------Process Command

    def process_command(self):
        cmd = self.conn.get_command()
        if cmd:
            verb, args = self._verbing(cmd)
            ## Did we get a verb and it is authozied?
            if verb and verb in self.avatar.abilities:
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


    #---------------------------------------------------------------Adj Faction

    def adj_faction(self, faction_uuid, amount):
        pass

    #-------------------------------------------------------------Adj Hitpoints

    def adj_hitpoints(self, value):
        pass

    #-----------------------------------------------------------------Adj Money

    def adj_money(self, amount):
        pass

    #-----------------------------------------------------------------Adj Skill

    def adj_skill(self, skill_uuid, amount):
        pass

    #--------------------------------------------------------------------Adj XP

    def adj_xp(self, amount):
        pass

    #-----------------------------------------------------------------------Ban

    def ban(self):
        pass

    #----------------------------------------------------------------------Bind

    def bind(self, room_uuid):
        pass

    #----------------------------------------------------------------Clear Flag

    def clear_flag(self, flag_uuid):
        pass

    #---------------------------------------------------------------Clear Token

    def clear_token(self, token_name):
        if token_name in self.token:
            del self.token[token_name]

    #----------------------------------------------------------------Do Ability

    def do_ability(self, ability_uuid):
        pass

    #-----------------------------------------------------------Do Ability Self

    def do_ability_self(self, ability_uuid):
        pass

    #-----------------------------------------------------------------Get Token

    def get_token(self, token_name):
        self.token.get(token_name, None)

    #-----------------------------------------------------------------Give Item

    def give_item(self, item_uuid, count=1):
        pass

    #-----------------------------------------------------------------Has Money

    def has_money(self, amount):
        pass

    #-----------------------------------------------------------------Has Skill

    def has_skill(self, skill_uuid, amount):
        pass

    #---------------------------------------------------------------Has Faction

    def has_faction(self, faction_uuid, amount):
        pass

    #------------------------------------------------------------------Has Flag

    def has_flag(self, flag_uuid):
        pass

    #------------------------------------------------------------------Has Item

    def has_item(self, item_uuid, count=1):
        pass

    #------------------------------------------------------------------Has Item

    def has_token(self, token_name):
        return token_name in self.token

    #----------------------------------------------------------------------Kill

    def kill(self):
        pass

    #-----------------------------------------------------------------On Attack

    def on_attack(self, mob):
        pass

    #------------------------------------------------------------------On Death

    def on_death(self, mob):
        pass

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        pass

    #-------------------------------------------------------------------On Slay

    def on_slay(self, mob):
        pass

    #------------------------------------------------------------Revoke Ability

    def revoke_ability(self, ability_uuid):
        pass

    #----------------------------------------------------------------------Save

    def save(self):
        pass

    #---------------------------------------------------------------Set Calling

    def set_clas(self, clas_uuid):
        pass

    #----------------------------------------------------------------Set Gender

    def set_gender(self, gender_uuid):
        pass

    #-------------------------------------------------------------Set Hitpoints

    def set_hitpoints(self, value):
        pass

    #-----------------------------------------------------------------Set Level

    def set_level(self, level):
        pass

    #------------------------------------------------------------------Set Name

    def set_name(self, name):
        pass

    #------------------------------------------------------------------Set Flag

    def set_flag(self, flag_uuid):
        pass

    #------------------------------------------------------------------Set Race

    def set_race(self, race_uuid):
        pass

    #-----------------------------------------------------------------Set Token

    def set_token(self, token_name, value):
        self.token[token_name] = value

    #----------------------------------------------------------------------Stun

    def stun(self, duration):
        pass

    #-------------------------------------------------------------------Suspend

    def suspend(self, days):
        pass

    #-----------------------------------------------------------------Take Item

    def take_item(self, item_uuid):
        pass

    #------------------------------------------------------------------Teleport

    def teleport(self, room_uuid):
        pass

    #--------------------------------------------------------------Zero Faction

    def zero_faction(self, faction_uuid):
        pass

    #----------------------------------------------------------------Zero Money

    def zero_money(self):
        pass

   #----------------------------------------------------------------Zero Skill

    def zero_skill(self, skill_uuid):
        pass

    #-------------------------------------------------------------------Zero XP

    def zero_xp(self):
        pass


