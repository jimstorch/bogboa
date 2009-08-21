# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/verb.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.commands import account
from mudlib.commands import movement
from mudlib.commands import speech
from mudlib.commands import info
from mudlib.commands import usage
from mudlib.commands import wizard
from mudlib.commands import system
#from mudlib.action import silly


VERB_ALIAS = {}
VERB_HANDLER = {}

#------------------------------------------------------------------Command List

## Commands take the following format:
##      [0] = tuple of aliases with tuple[0] == One True Verb(tm)
##      [1] = handler function to call with those arguments
 

COMMAND_LIST = (

    ## Account

    (('create',), account.create),
    (('name',), account.name),
    (('gender',), account.gender),
    (('race',), account.race),
    (('guild',), account.guild),
    (('password',), account.password),
#    (('email',), account.email),
    (('review',), account.review),
    (('save',), account.save),
    (('load',), account.load),

    ## Movement

    (('north', 'n', '8'), movement.north),
    (('east', 'e', '6'), movement.east),
    (('south', 's', '2'), movement.south),
    (('west', 'w', '4'), movement.west),
#    (('up', 'u', 'climb', '9'), movement.up),
#    (('down', 'd', '3'), movement.down),
#    (('recall', 'home'), movement.recall),
#    (('enter',), movement.enter),
#    (('exit',), movement.exit),
    
    ## Communication

    (('broadcast', 'announce'), speech.broadcast),
    (('emote', '/em', ':', 'em'), speech.emote),    
    (('ooc',), speech.ooc),
    (('reply', 'r', '/r'), speech.reply),
    (('say', '/s'), speech.say),
    (('shout', 'yell', '/y'), speech.shout),
    (('tell', 'whisper', '/t', '/w'), speech.tell),

    ## Information 

    (('help', '?', 'info'), info.help),
    (('commands','command', 'cmds', '??'), info.commands),
    (('score', 'played','stats'), info.score),
    (('time', 'clock', 'hour'), info.time),
    (('date', 'calendar', 'year'), info.date),
    (('inventory', 'i', 'inven'), info.inventory),
    (('look', 'l', '5','x','examine'), info.look),    

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

    (('quit', 'exit', 'logoff'), system.quit),
    (('bug',), system.bug),
    (('ansi','color'), system.ansi),

    ## Wizardry
    (('ban',), wizard.ban), 
    (('grant',), wizard.grant),
    (('kick', 'punt'), wizard.kick),
    (('revoke',), wizard.revoke),
    (('summon',), wizard.summon),
    (('teleport', 'port'), wizard.teleport),
    (('zap',), wizard.zap),
    (('shutdown',), wizard.shutdown),
    (('uptime',), wizard.uptime),

    ## Silly
#    (('verbose',), silly.verbose),
#    (('plugh', 'xyzzy'), silly.plugh),
#    (('pizza',), silly.pizza),
#    (('iddqd', 'idkfa'), silly.iddqd),

    )


#----------------------------------------------------------------Initialization

## Populate the verb alias and the verb handler dictionaries

for command in COMMAND_LIST:

    ## Verb Alias is used to match synonymns to the one_true_verb(tm)
    aliases = command[0]
    one_true_verb = aliases[0]
    for alias in aliases:
        VERB_ALIAS[alias] = one_true_verb
   
    ## Specify the function to use with this verb
    VERB_HANDLER[one_true_verb] = command[1]

