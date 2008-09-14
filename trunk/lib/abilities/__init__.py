#------------------------------------------------------------------------------
#   File:       ruleset/abilities/__init__.py
#   Purpose:    initialization of stuff needed
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset.abilities import speech
from ruleset.abilities import system
from ruleset.abilities import movement

## Speech
shared.ABILITY_DICT['tell'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['t'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['whisper'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['wh'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['reply'] = (speech.reply.parser, speech.reply)
shared.ABILITY_DICT['r'] = (speech.reply.parser, speech.reply)
shared.ABILITY_DICT['say'] = (speech.say.parser, speech.say)
shared.ABILITY_DICT['shout'] = (speech.shout.parser, speech.shout)
shared.ABILITY_DICT['broadcast'] = (speech.broadcast.parser, speech.broadcast)

## System
shared.ABILITY_DICT['quit'] = (system.quit.parser, system.quit)
shared.ABILITY_DICT['look'] = (system.look.parser, system.look)
shared.ABILITY_DICT['l'] = (system.look.parser, system.look)

## Movement
shared.ABILITY_DICT['north'] = (movement.north.parser, movement.north)
shared.ABILITY_DICT['n'] = (movement.north.parser, movement.north)
shared.ABILITY_DICT['northeast'] = (movement.northeast.parser, 
    movement.northeast)
shared.ABILITY_DICT['ne'] = (movement.northeast.parser, 
    movement.northeast)
shared.ABILITY_DICT['east'] = (movement.east.parser, movement.east)
shared.ABILITY_DICT['e'] = (movement.east.parser, movement.east)
shared.ABILITY_DICT['southeast'] = (movement.southeast.parser, 
    movement.southeast)
shared.ABILITY_DICT['se'] = (movement.southeast.parser, 
    movement.southeast)
shared.ABILITY_DICT['south'] = (movement.south.parser, movement.south)
shared.ABILITY_DICT['s'] = (movement.south.parser, movement.south)
shared.ABILITY_DICT['southwest'] = (movement.southwest.parser, 
    movement.southwest)
shared.ABILITY_DICT['sw'] = (movement.southwest.parser, 
    movement.southwest)
shared.ABILITY_DICT['west'] = (movement.west.parser, movement.west)
shared.ABILITY_DICT['w'] = (movement.west.parser, movement.west)
shared.ABILITY_DICT['northwest'] = (movement.northwest.parser, 
    movement.northwest)
shared.ABILITY_DICT['nw'] = (movement.northwest.parser, 
    movement.northwest)
shared.ABILITY_DICT['up'] = (movement.up.parser, movement.up)
shared.ABILITY_DICT['u'] = (movement.up.parser, movement.up)
shared.ABILITY_DICT['down'] = (movement.down.parser, movement.down)
shared.ABILITY_DICT['d'] = (movement.down.parser, movement.down)
shared.ABILITY_DICT['enter'] = (movement.enter.parser, movement.enter)
shared.ABILITY_DICT['exit'] = (movement.exit.parser, movement.exit)
shared.ABILITY_DICT['recall'] = (movement.recall.parser, movement.recall)


