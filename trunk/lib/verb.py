##-----------------------------------------------------------------------------
##  File:       lib/verb.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib.action import movement
from lib.action import speech
from lib.action import info
from lib.action import usage
from lib.action import wizard
from lib.action import silly


VERB_THESAURUS = {}
VERB_PARSER = {}
VERB_HANDLER = {}

for command in COMMAND_LIST:

    ## Verb Thesaurus is used to match aliases to the one_true_verb(tm)
    aliases = command[0]
    for alias in aliases:
        one_true_verb = aliases[0]
        VERB_THESAURUS[alias] = one_true_verb

    ## Specify the parser to use with this verb
    VERB_PARSER[one_true_verb] = command[1]
   
    ## Specify the function to use with this verb
    VERB_HANDLER[one_true_verb] = command[2]


#------------------------------------------------------------------Command List

## Commands take the following format:
##      [0] = tuple of aliases with tuple[0] == One True Verb(tm)
##      [1] = parser function to convert extra words into arguments
##      [2] = verb function to call with those arguments
 

COMMAND_LIST = (

    ## Movement

    (('north', 'nor', 'n', '8'), movement.north.parser, movement.north),
    (('east', 'eas', 'e', '6'), movement.east.parser, movement.east),
    (('south', 'sou', 's', '2'), movement.south.parser, movement.south),
    (('west', 'wes', 'w', '4'), movement.west.parser, movement.west),
    (('up', 'u', 'climb', '9'), movement.up.parser, movement.up),
    (('down', 'dn', 'dwn', 'd', '3'),movement.down.parser, movement.down),
    (('recall', 'home'), movement.recall.parser, movement.recall),
    (('enter',), movement.enter.parser, movement.enter),
    
    ## Communication
    
    (('say', '/s'), speech.say.parser, speech.say),
    (('shout', 'yell', '/y'), speech.shout.parser, speech.shout),
    (('ooc',), speech.ooc.parser, speech.ooc),
    (('tell', 'whisper', '/t', '/w'), speech.tell.parser, speech.tell),
    (('reply', 'r', '/r'), speech.reply.parser, speech.reply),
    (('emote', '/em', ':'), speech.emote.parser, speech.emote),

    ## Information

    (('help', '?', 'info'), info.help.parser, info.help),
    (('score', 'played','stats'), info.score.parser, info.score),
    (('time', 'date', 'clock'), info.time.parser, info.time),
    (('inventory', 'i', 'inven'), info.inventory.parser, info.inventory),
    (('look', 'l', '5'), info.look.parser, info.look),    

    ## Interaction

    (('wear', 'don', 'eqip'), usage.wear.parser, usage.wear),
    (('remove', 'unequip'), usage.remove.parser, usage.remove),
    (('take', 'get', 'pickup', 'grab'), usage.take.parser, usage.take),
    (('drop', 'discard', 'toss', 'throw'), usage.drop.parser, usage.drop), 
    (('do', 'cast', 'doability', 'spell'), usage.do.parser, usage.do),
    (('attack', 'kill', 'atk', 'slay'), usage.attack.parser, usage.attack),
    (('target', 'tar'), usage.target.parser, usage.target),
    (('search',), usage.search.parser, usage.search),

    ## System

    (('quit', 'exit', 'logoff'), system.quit.parser, system.quit),

    ## Wizardry
    (('ban',), wizard.ban.parser, wizard.ban), 
    ('kick', 'punt'), wizard.kick.parser, wizard.kick),
    (('summon',) wizard.summon.parser, wizard.summon),
    (('teleport', 'port'), wizard.teleport.parser, wizard.teleport),
    (('zap',) wizard.zap.parser, wizard.zap),

    ## Silly
    (('verbose',), silly.verbose.parser, silly.verbose),
    (('plugh', 'xyzzy'), silly.plugh.parser, silly.plugh),
    (('pizza',), silly.pizza.parser, silly.pizza),
    (('iddqd', 'idkfa'), silly.iddqd.parser, silly.iddqd),

    )


#--------------------------------------------------------------------Split Verb
   
def split_verb(text):

    """Break a sentence into the verb and the balance of the remaining words.
    Strips off trailing punctuation and extra spaces.
    Returns a (verb, balance) tuple."""    
    
    words = text.split()
    count = len(words)

    if count == 0:
        verb = None
        balance = []        

    elif count == 1:
        a_verb = words[0].lower()
        balance = []

    else:
        a_verb = words[0].lower()
        balance = words[1:] 
   
    one_true_verb = VERB_THESAURUS.get(a_verb, None)

    return (one_true_verb, balance)


