##-----------------------------------------------------------------------------
##  File:       lib/player.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------


class Player(object):

    def __init__(self):

        ## Identity
        self.conn = None
        self.active = False
        self.uuid = None
        self.name = None
        self.alias = None
        self.race = None
        self.gender = None
        self.sect = None
        self.level = None
        self.skill = {}
        self.ability = {}
        self.flag = {}          # Flags are persistent variables
        self.token = {}         # Tokens are non persistent variables

        self.room = None
        self.friendly_target = None
        self.hostile_target = None        


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

    #----------------------------------------------------------------Deactivate

    def deactivate(self):
        self.active = False
        self.conn.active = False

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

    def give_item(self, item_uuid):
        pass

    #-------------------------------------------------------------Grant Ability

    def grant_ability(self, ability_uuid):
        pass

    #---------------------------------------------------------------Has Ability

    def has_ability(self, ability_name):
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

    def has_item(self, item_uuid):
        pass

    #------------------------------------------------------------------Has Item

    def has_token(self, token_name):
        return token_name in self.token


    #----------------------------------------------------------------------Kill

    def kill(self):
        pass

    #-----------------------------------------------------------Process Command

    def process_command(self):
        print self.conn.get_cmd()

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

