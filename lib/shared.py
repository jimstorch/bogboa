##-----------------------------------------------------------------------------
##  File:       lib/shared.py
##  Purpose:    global values used by the server
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

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

##
##  Prototypes are "models" that are used either as a reference for game math
##  or a blueprint from which to spawn game objects.  
## 
PROTO_ITEM = {}
PROTO_RACE = {}
PROTO_GENDER = {}
PROTO_SECT = {}
PROTO_NPC = {}

##
##  The following are "real" things the players interact with.   
##
ROOM = {}
OBJECT = {}
PLAYER = {}
NPC = {}


