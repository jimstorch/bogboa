# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/verb.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.iface import cmd_account
from mudlib.iface import cmd_movement
from mudlib.iface import cmd_speech
from mudlib.iface import cmd_info
from mudlib.iface import cmd_use
from mudlib.iface import cmd_wiz
from mudlib.iface import cmd_system
#from mudlib.iface import silly


VERB_ALIAS = {}
VERB_HANDLER = {}

#------------------------------------------------------------------Command List

## Commands take the following format:
##      [0] = tuple of aliases with tuple[0] == One True Verb(tm)
##      [1] = handler function to call with those arguments


COMMAND_LIST = (

    ## Account

    (('create',), cmd_account.create),
    (('name',), cmd_account.name),
    (('gender',), cmd_account.gender),
    (('race',), cmd_account.race),
    (('guild',), cmd_account.guild),
    (('password',), cmd_account.password),
#    (('email',), cmd_account.email),
    (('review',), cmd_account.review),
    (('save',), cmd_account.save),
    (('load',), cmd_account.load),

    ## Movement

    (('north', 'n', '8'), cmd_movement.north),
    (('east', 'e', '6'), cmd_movement.east),
    (('south', 's', '2'), cmd_movement.south),
    (('west', 'w', '4'), cmd_movement.west),
#    (('up', 'u', 'climb', '9'), cmd_movement.up),
#    (('down', 'd', '3'), cmd_movement.down),
#    (('recall', 'home'), cmd_movement.recall),
#    (('enter',), cmd_movement.enter),
#    (('exit',), cmd_movement.exit),

    ## Communication

    (('broadcast', 'announce'), cmd_speech.broadcast),
    (('emote', '/em', ':', 'em'), cmd_speech.emote),
    (('ooc',), cmd_speech.ooc),
    (('reply', 'r', '/r'), cmd_speech.reply),
    (('say', '/s'), cmd_speech.say),
    (('shout', 'yell', '/y'), cmd_speech.shout),
    (('tell', 'whisper', '/t', '/w'), cmd_speech.tell),

    ## Information

    (('help', '?', 'info'), cmd_info.help),
    (('topics',), cmd_info.topics),
    (('commands','command', 'cmds', '??'), cmd_info.commands),
    (('score', 'played','stats'), cmd_info.score),
    (('time', 'clock', 'hour'), cmd_info.time),
    (('date', 'calendar', 'year'), cmd_info.date),
    (('inventory', 'i', 'inven'), cmd_info.inventory),
    (('look', 'l',), cmd_info.look),
    (('stats', 'stat',), cmd_info.stats),

    ## Interaction

    (('wear', 'don', 'equip'), cmd_use.wear),
    (('remove', 'unequip'), cmd_use.remove),
    (('take', 'get', 'pickup', 'grab'), cmd_use.take),
    (('drop', 'discard', 'toss', 'throw'), cmd_use.drop),
#    (('do', 'cast', 'doability', 'spell'), cmd_use.do),
#    (('attack', 'kill', 'atk', 'slay'), cmd_use.attack),
#    (('target', 'tar'), cmd_use.target),
#    (('search',), cmd_use.search),

    ## System

    (('quit', 'exit', 'logoff'), cmd_system.quit),
    (('bug',), cmd_system.bug),
    (('ansi','color'), cmd_system.ansi),

    ## Wizardry
    (('ban',), cmd_wiz.ban),
    (('grant',), cmd_wiz.grant),
    (('kick', 'punt'), cmd_wiz.kick),
    (('revoke',), cmd_wiz.revoke),
    (('summon',), cmd_wiz.summon),
    (('teleport', 'port'), cmd_wiz.teleport),
    (('zap',), cmd_wiz.zap),
    (('shutdown',), cmd_wiz.shutdown),
    (('uptime',), cmd_wiz.uptime),

    ## Silly
#    (('verbose',), cmd_silly.verbose),
#    (('plugh', 'xyzzy'), cmd_silly.plugh),
#    (('pizza',), cmd_silly.pizza),
#    (('iddqd', 'idkfa'), cmd_silly.iddqd),

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
