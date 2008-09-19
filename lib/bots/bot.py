#------------------------------------------------------------------------------
#   File:       lib/bots/bot.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Bot(object):

    def __init__(self):

        ## Identity
        self.uuid = None
        self.handle = None
        self.alias = None
        self.race = None
        self.gender = None
        self.archetype = None
        self.level = None
        self.module = None


    #--------------------------------------------------------------------Banish

    def banish(self):
        pass

    #---------------------------------------------------------------Clear Token

    def clear_token(self, token):
        pass


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

    def follow(self, mob):
        pass


    #-----------------------------------------------------------------Give Item

    def give_item(self, item_uuid):
        pass

    #----------------------------------------------------------------------Hate

    def hate(self, mob, amount):
        pass

    #----------------------------------------------------------------------Kill

    def kill(self):
        pass

    #----------------------------------------------------------------------Love

    def love(self, mob, amount):
        pass

    #----------------------------------------------------------------------Poof

    def poof(self):
        pass


    #-----------------------------------------------------------------On Attack

    def on_attack(self, mob):
        pass

    #------------------------------------------------------------------On Death

    def on_death(self, mob):
        pass

    #------------------------------------------------------------------On Given

    def on_given(self, mob, item):
        pass

    #-------------------------------------------------------------------On Hear

    def on_hear(self, mob):
        pass

    #--------------------------------------------------------------------On See

    def on_see(self, mob):
        pass

    #-----------------------------------------------------------------On Signal

    def on_signal(self, signal):
        pass

    #-------------------------------------------------------------------On Slay

    def on_slay(self, mob):
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

    def spawn(self, mob_uuid, level):
        pass

    #----------------------------------------------------------------------Stun

    def stun(self, duration):
        pass

    #--------------------------------------------------------------------Summon

    def summon(self, mob_uuid):
        pass

    #------------------------------------------------------------------Teleport

    def teleport(self, room_uuid):
        pass

    #----------------------------------------------------------------------Tell

    def tell(self, mob, text):
        pass


