##-----------------------------------------------------------------------------
##  File:       lib/verb.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib.action import movement
from lib.action import speech
from lib.action import info
from lib.action import usage
from lib.action import wizard
#from lib.action import silly


VERB_ALIAS = {}
VERB_HANDLER = {}

#------------------------------------------------------------------Command List

## Commands take the following format:
##      [0] = tuple of aliases with tuple[0] == One True Verb(tm)
##      [1] = verb function to call with those arguments
 

COMMAND_LIST = (

    ## Movement

    (('north', 'nor', 'n', '8'), movement.north),
    (('east', 'eas', 'e', '6'), movement.east),
    (('south', 'sou', 's', '2'), movement.south),
    (('west', 'wes', 'w', '4'), movement.west),
#    (('up', 'u', 'climb', '9'), movement.up),
#    (('down', 'dn', 'dwn', 'd', '3'), movement.down),
#    (('recall', 'home'), movement.recall),
#    (('enter',), movement.enter),
    
    ## Communication

    (('broadcast', 'announce'), speech.broadcast),
    (('emote', '/em', ':'), speech.emote),    
    (('ooc',), speech.ooc),
    (('reply', 'r', '/r'), speech.reply),
    (('say', '/s'), speech.say),
    (('shout', 'yell', '/y'), speech.shout),
    (('tell', 'whisper', '/t', '/w'), speech.tell),

    ## Information 

    (('help', '?', 'info'), info.help),
    (('score', 'played','stats'), info.score),
    (('time', 'date', 'clock'), info.time),
    (('inventory', 'i', 'inven'), info.inventory),
    (('look', 'l', '5'), info.look),    

    ## Interaction

    (('wear', 'don', 'equip'), usage.wear),
    (('remove', 'unequip'), usage.remove),
    (('take', 'get', 'pickup', 'grab'), usage.take),
    (('drop', 'discard', 'toss', 'throw'), usage.drop), 
    (('do', 'cast', 'doability', 'spell'), usage.do),
#    (('attack', 'kill', 'atk', 'slay'), usage.attack),
#    (('target', 'tar'), usage.target),
#    (('search',), usage.search),

    ## System

#    (('quit', 'exit', 'logoff'), system.quit),

    ## Wizardry
    (('ban',), wizard.ban), 
    (('grant',), wizard.grant),
    (('kick', 'punt'), wizard.kick),
    (('revoke',), wizard.revoke),
    (('summon',), wizard.summon),
    (('teleport', 'port'), wizard.teleport),
    (('zap',), wizard.zap),

    ## Silly
#    (('verbose',), silly.verbose),
#    (('plugh', 'xyzzy'), silly.plugh),
#    (('pizza',), silly.pizza),
#    (('iddqd', 'idkfa'), silly.iddqd),

    )

## Populate the command list

for command in COMMAND_LIST:

    ## Verb Alias is used to match synonymns to the one_true_verb(tm)
    aliases = command[0]
    one_true_verb = aliases[0]
    for alias in aliases:
        VERB_ALIAS[alias] = one_true_verb
   
    ## Specify the function to use with this verb
    VERB_HANDLER[one_true_verb] = command[1]

