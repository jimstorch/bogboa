# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/shared.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


## Boolean used by the main loop, False = stop the server

SERVER_RUN = True


## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: THE_TIME gets updates each cycle by Scheduler.tick().

THE_TIME = 0.0      


#--[ Client Connections ]------------------------------------------------------

LOBBY_LIST = []
PLAY_LIST = []


#--[ Reference Objects ]-------------------------------------------------------

GENDERS = {}
GUILDS = {}
HELPS = {}
ITEMS = {}
NPCs = {}
RACES = {}


#--[ Objects in the game world ]-----------------------------------------------


OBJECTS = {}
PLAYERS = {}
SPAWNS = {}
ROOMS = {}

