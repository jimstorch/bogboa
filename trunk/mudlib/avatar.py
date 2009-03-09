# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/avatar.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Avatar(object):

    def __init__(self):

        ## Creation
        self.name = ''
        self.password = ''
        self.race = ''
        self.gender = ''
        self.guild = ''

        ## Identity
        self.uuid = None
        self.alias = None
        self.level = 1
        self.xp = 0

        ## Inventory
        self.money = 0
        self.pouch = None
        self.satchel = None
        self.kit = None
        self.backpack = None
        self.bank = None

        ## Details
        self.room = None                ## Current location of the player
        self.target = None              ## Player's hostile target
        self.btarget = None             ## Player's beneficial target
        self.ctarget = None             ## Player's conversational target
        self.abilities = set()          ## Commands usuable by client
        self.skill = {}
        self.flag = {}                  ## Flags are persistent variables
        self.token = {}                 ## Tokens are non persistent variables


