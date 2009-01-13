# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/shared.py
#   Purpose:    global values used by the server
#   Author:     Jim Storch
#------------------------------------------------------------------------------

SERVER_NAME = 'BogBoa Test Realm'

## Boolean used by the main loop, False = stop the server
SERVER_RUN = True

## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: the_time gets updates each cycle by Scheduler.tick().
THE_TIME = 0.0      

##
## List of client connections in Lobby or Play Mode
##
LOBBY_LIST = []
PLAY_LIST = []

##
##  Am I using this?
## 
ACTION = {}

##  Help files
HELP = {}

##
##  Prototypes are "models" that are used either as a reference for game math
##  or a blueprint from which to spawn game objects.  
## 
ITEM = {}
RACE = {}
GENDER = {}
SECT = {}
PROTO_NPC = {}

##
##  The following are "real" things the players interact with.   
##
ROOM = {}
OBJECT = {}
PLAYER = {}
NPC = {}


