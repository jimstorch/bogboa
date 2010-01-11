# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/verb.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Map game verbs to associated command functions.
"""

from mudlib import cmd


VERB_ALIAS = {}
VERB_HANDLER = {}

#------------------------------------------------------------------Command List

## Commands take the following format:
##      [0] = tuple of aliases with tuple[0] == One True Verb(tm)
##      [1] = handler function to call with those arguments


COMMAND_LIST = (

    ## Account

#    (('create',), account.create),
#    (('name',), account.name),
#    (('gender',), account.gender),
#    (('race',), account.race),
#    (('guild',), account.guild),
#    (('password',), account.password),
#    (('email',), account.email),
#    (('review',), account.review),
#    (('save',), account.save),
#    (('load',), account.load),

    ## Movement

    (('north', 'n', '8'), cmd.north),
    (('east', 'e', '6'), cmd.east),
    (('south', 's', '2'), cmd.south),
    (('west', 'w', '4'), cmd.west),
    (('up', 'u', 'climb', '9'), cmd.up),
    (('down', 'd', '3'), cmd.down),
    (('recall', 'home'), cmd.recall),
    (('enter',), cmd.enter),
    (('exit',), cmd.exit),

    ## Communication

#    (('broadcast', 'announce'), speech.broadcast),
    (('emote', '/em', ':', 'em'), cmd.emote),
    (('ooc',), cmd.ooc),
    (('reply', 'r', '/r'), cmd.reply),
    (('say', '/s'), cmd.say),
    (('shout', 'yell', '/y'), cmd.shout),
    (('tell', 'whisper', '/t', '/w'), cmd.tell),

    ## Information

    (('help', '?', 'info'), cmd.help),
    (('topics',), cmd.topics),
    (('commands','command', 'cmds', '??'), cmd.commands),
    (('score', 'played','stats'), cmd.score),
    (('time', 'clock', 'hour'), cmd.time),
    (('date', 'calendar', 'year'), cmd.date),
    (('inventory', 'i', 'inven'), cmd.inventory),
    (('look', 'l',), cmd.look),
    (('stats', 'stat',), cmd.stats),

    ## Interaction

    (('wear', 'don', 'equip'), cmd.wear),
    (('remove', 'unequip'), cmd.remove),
    (('take', 'get', 'pickup', 'grab'), cmd.take),
    (('drop', 'discard', 'toss', 'throw'), cmd.drop),
#    (('do', 'cast', 'doability', 'spell'), cmd.do),
#    (('attack', 'kill', 'atk', 'slay'), cmd.attack),
#    (('target', 'tar'), cmd.target),
#    (('search',), cmd.search),

    ## System

    (('quit', 'exit', 'logoff'), cmd.quit),
    (('bug',), cmd.bug),
    (('ansi','color'), cmd.ansi),

    ## Wizardry
    (('ban',), cmd.ban),
    (('grant',), cmd.grant),
    (('kick', 'punt'), cmd.kick),
    (('revoke',), cmd.revoke),
    (('summon',), cmd.summon),
    (('teleport', 'port'), cmd.teleport),
    (('zap',), cmd.zap),
    (('shutdown',), cmd.shutdown),
    (('uptime',), cmd.uptime),

    ## Silly
#    (('verbose',), cmd.verbose),
#    (('plugh', 'xyzzy'), cmd.plugh),
#    (('pizza',), cmd.pizza),
#    (('iddqd', 'idkfa'), cmd.iddqd),

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
