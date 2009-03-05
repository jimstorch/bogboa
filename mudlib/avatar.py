# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/avatar.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Avatar(object):

    def __init__(self):

        ## Identity
        self.uuid = None
        self.name = 'Guest'
        self.alias = None
        self.race = None
        self.gender = None
        self.guild = None
        self.level = None
        self.xp
        self.money
        self.room = None                ## Current location of the player
        self.target = None              ## Player's hostile target
        self.btarget = None             ## Player's beneficial target
        self.ctarget = None             ## Player's conversational target
        self.abilities = set()          ## Commands usuable by client
        self.skill = {}
        self.flag = {}          # Flags are persistent variables
        self.token = {}         # Tokens are non persistent variables


