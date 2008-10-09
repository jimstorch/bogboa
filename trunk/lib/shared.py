##-----------------------------------------------------------------------------
##  File:       lib/shared.py
##  Purpose:    global values used by the server
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

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


ACTION_DICT = {}

## List of clients in character gameplay mode 
PLAY_LIST = []


## Map an archetype alias to Archetype Object
ARCHETYPE_DICT = {}


## Map a UUID to a Creature Prototype Object
PROTOTYPE_DICT = {}


## Map a creature alias to an active Creature Object
CREATURE_DICT = {}


## Map an effect alias to an Effect object
EFFECT_DICT = {}


## Map an item UUID to an item object 
ITEM_DICT = {}


## Map a Player handle to a Player object
PLAYER_DICT = {}


## Map a Skill alias to a Skill object
SKILL_DICT = {}


## Map a room UUID to a Room object
ROOM_DICT = {}


