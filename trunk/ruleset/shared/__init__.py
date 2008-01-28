#------------------------------------------------------------------------------
#   File:       shared/__init__.py
#   Purpose:    global values used by the server
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import time


## Boolean used by the main loop, False = stop the server
SERVER_RUN = True


## Since so much of code needs to know the current time it seemed better
## to share the value instead a bajillion OS calls via time.time().
## Note: the_time gets updates each cycle by Scheduler.tick().
THE_TIME = time.time()          ## Initialize to current time


## List of clients in the following pre-game modes:
##   Welcome, Login, CreateAccount, CreateCharacter, CharacterSelect 
LOBBY_LIST = []


## List of clients in character gameplay mode 
PLAY_LIST = []


## Dictionary of rooms players might occupy
ROOM_DICT = {}


## Handle Dictionary, maps handles to client play modes
HANDLE_DICT = {}


## Ability Dictionary, maps ability handles to ability functions 
ABILITY_DICT = {}

