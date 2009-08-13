# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/body.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

#from lib.stringsub import StringSub

class Body(object):

    def __init__(self):

        ## Identity
        self.name = ''                ## True name
        self.alias = ''               ## Displayed name
        self.password = ''
        self.is_player = False    
        self.index = None               ## numerical index
        self.brain = None               ## Brain or Client object
        self.race = ''
        self.gender = ''
        self.guild = ''
        self.level = 1
        self.strsub = None        

        ## Inventory
#        self.money = 0
#        self.pouch = None
#        self.satchel = None
#        self.kit = None
#        self.backpack = None
#        self.bank = None

        ## Details
        self.room = None                ## Current location 
        self.target = None              ## Hostile target
        self.btarget = None             ## Beneficial target
        self.ctarget = None             ## Conversational target
        self.abilities = set()          ## Commands useable
        self.skill = {}
        self.flag = {}                  ## Flags are persistent variables
        self.token = {}                 ## Tokens are non persistent variables


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

    #--------------------------------------------------------------------Banish

    def banish(self):
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

    #---------------------------------------------------------------------Emote

    def emote(self, text):
        pass

    #--------------------------------------------------------------------Follow

    def follow(self, body):
        pass

    #-----------------------------------------------------------------Give Item

    def give_item(self, item_uuid):
        pass

    #-----------------------------------------------------------------------Joy

    def joy(self, body, amount):
        pass

    #----------------------------------------------------------------------Kill

    def kill(self):
        pass

    #----------------------------------------------------------------------Poof

    def poof(self):
        pass

    #-----------------------------------------------------------------On Attack

    def on_attack(self, body):
        pass

    #------------------------------------------------------------------On Death

    def on_death(self, body):
        pass

    #------------------------------------------------------------------On Given

    def on_given(self, body, item):
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, body):
        pass

    #--------------------------------------------------------------------On See

    def on_see(self, body):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass

    #-------------------------------------------------------------------On Slay

    def on_slay(self, body):
        pass

    #------------------------------------------------------------------On Spawn

    def on_spawn(self):
        pass

    #-----------------------------------------------------------------On Strike

    def on_strike():
        pass 

    #-----------------------------------------------------------------On Struck
 
    def on_struck():
        pass    

    #----------------------------------------------------------------------Pain

    def pain(self, body, amount):
        pass

    #-----------------------------------------------------------------------Say

    def say(self, text):
        pass

    #---------------------------------------------------------------Set Faction

    def set_faction(self, faction_uuid, value):
        pass

    #-------------------------------------------------------------Set Hitpoints

    def set_hitpoints(self, value):
        pass

    #-----------------------------------------------------------------Set Level

    def set_level(self, level):
        pass

    #-----------------------------------------------------------------Set Token

    def set_token(self, token, value):
        pass

    #---------------------------------------------------------------------Shout

    def shout(self, text):
        pass

    #----------------------------------------------------------------------Stop

    def stop(self):
        pass

    #---------------------------------------------------------------------Spawn

    def spawn(self, uuid, level=None):
        pass

    #--------------------------------------------------------------------Summon

    def summon(self, body):
        pass

    #-------------------------------------------------------------------Suspend

    def suspend(self, days):
        pass

    #------------------------------------------------------------------Teleport

    def teleport(self, room_uuid):
        pass

    #----------------------------------------------------------------------Tell

    def tell(self, body, text):
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

    def on_attack(self, body):
        pass

    #------------------------------------------------------------------On Death

    def on_death(self, body):
        pass

    #----------------------------------------------------------------On Destroy

    def on_destroy(self):
        pass

    #-------------------------------------------------------------------On Init

    def on_init(self):
        pass

    #-------------------------------------------------------------------On Slay

    def on_slay(self, body):
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

    #--------------------------------------------------------------------------
    #   Convenience Hooks for Client Methods
    #--------------------------------------------------------------------------

    #-------------------------------------------------------------Clear Command

    def clear_commands(self):
        """Remove all command from client."""
        if self.is_player:
            self.brain.clear_commands()

    #-------------------------------------------------------------Grant Command

    def grant_command(self, command_name):
        """Authorize player to use an command and tell them."""
        if self.is_player:
            self.brain.grant_command(command_name)

    #------------------------------------------------------Grant Command Silent

    def grant_command_silent(self, command_name):
        """Silently authorize a player to use an command."""
        if self.is_player:
            self.brain.grant_command_silent(command_command)

    #---------------------------------------------------------------Has Command

    def has_command(self, command_name):
        if self.is_player:
            return self.brain.has_command(command_name)
        else:
            return False

    #------------------------------------------------------------Revoke Command

    def revoke_command(self, command_name):
        """De-authorize player to use an command and tell them."""
        if self.is_player:
            self.brain.revoke_command(command_name)

    #-----------------------------------------------------Revoke Command Silent

    def revoke_command_silent(self, command_name):
        """Silently de-authorize a player to use an command."""
        if self.is_player:
            self.brain.revoke_command_silent(command_name)

    #----------------------------------------------------------------------Send

    def send(self, msg):
        if self.is_player:
            self.brain.send(msg)

    #--------------------------------------------------------------------Prompt

    def prompt(self):
        """Transmit a newline and a prompt"""
        if self.is_player:
            self.brain.prompt()

    #---------------------------------------------------------------Soft Prompt

    def soft_prompt(self):
        """Called when a leading new-line is not desired"""
        if self.is_player:
            self.brain.soft_prompt()





