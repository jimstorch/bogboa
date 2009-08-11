# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/body.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Body(object):

    def __init__(self, index):

        ## Identity
        self.index = index
        self.brain = None               ## Brain or Client
        self.alias = None
        self.race = None
        self.gender = None
        self.guild = None
        self.level = None
        
        ## Inventory
        self.money = 0
        self.pouch = None
        self.satchel = None
        self.kit = None
        self.backpack = None
        self.bank = None

        ## Details
        self.room = None                ## Current location of the player
#        self.target = None              ## Player's hostile target
#        self.btarget = None             ## Player's beneficial target
#        self.ctarget = None             ## Player's conversational target
        self.abilities = set()          ## Commands usuable by client
        self.skill = {}
        self.flag = {}                  ## Flags are persistent variables
        self.token = {}                 ## Tokens are non persistent variables
        


    

