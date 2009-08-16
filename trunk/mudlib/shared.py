# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/shared.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


## Boolean used by the main loop, False = stop the server

SERVER_RUN = True


## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: THE_TIME gets updates each cycle by 
## driver.scheduler.THE_SCHEDULER.tick().

THE_TIME = 0.0      


#--[ Client Connections ]------------------------------------------------------

LOBBY = []
PLAYERS = []


#--[ Reference Objects ]-------------------------------------------------------

GENDERS = {}        ## key is gender name
GUILDS = {}         ## key is guild name
HELPS = {}          ## key is help name
RACES = {}          ## key is race name 
ITEMS = {}          ## key is item UUID
SPAWNS = {}         ## key is npc UUID


#--[ Objects in the game world ]-----------------------------------------------

OBJECTS = {}        ## key is object UUID
ROOMS = {}          ## key is room UUID
BODIES = {}         ## key is body UUID
BRAINS = []         ## List of AI's


    


