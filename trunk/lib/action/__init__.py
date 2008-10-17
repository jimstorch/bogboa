##-----------------------------------------------------------------------------
##  File:       ruleset/abilities/__init__.py
##  Purpose:    initialization of stuff needed
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib import shared
from lib.actions import speech
from lib.actions import system
from lib.actions import movement

## Speech
shared.ACTION_DICT['tell'] = (speech.tell.parser, speech.tell)
shared.ACTION_DICT['t'] = (speech.tell.parser, speech.tell)
shared.ACTION_DICT['whisper'] = (speech.tell.parser, speech.tell)
shared.ACTION_DICT['wh'] = (speech.tell.parser, speech.tell)
shared.ACTION_DICT['reply'] = (speech.reply.parser, speech.reply)
shared.ACTION_DICT['r'] = (speech.reply.parser, speech.reply)
shared.ACTION_DICT['say'] = (speech.say.parser, speech.say)
shared.ACTION_DICT['shout'] = (speech.shout.parser, speech.shout)
shared.ACTION_DICT['broadcast'] = (speech.broadcast.parser, speech.broadcast)

## System
shared.ACTION_DICT['quit'] = (system.quit.parser, system.quit)
shared.ACTION_DICT['look'] = (system.look.parser, system.look)
shared.ACTION_DICT['l'] = (system.look.parser, system.look)

## Movement
shared.ACTION_DICT['north'] = (movement.north.parser, movement.north)
shared.ACTION_DICT['n'] = (movement.north.parser, movement.north)
shared.ACTION_DICT['northeast'] = (movement.northeast.parser, 
    movement.northeast)
shared.ACTION_DICT['ne'] = (movement.northeast.parser, 
    movement.northeast)
shared.ACTION_DICT['east'] = (movement.east.parser, movement.east)
shared.ACTION_DICT['e'] = (movement.east.parser, movement.east)
shared.ACTION_DICT['southeast'] = (movement.southeast.parser, 
    movement.southeast)
shared.ACTION_DICT['se'] = (movement.southeast.parser, 
    movement.southeast)
shared.ACTION_DICT['south'] = (movement.south.parser, movement.south)
shared.ACTION_DICT['s'] = (movement.south.parser, movement.south)
shared.ACTION_DICT['southwest'] = (movement.southwest.parser, 
    movement.southwest)
shared.ACTION_DICT['sw'] = (movement.southwest.parser, 
    movement.southwest)
shared.ACTION_DICT['west'] = (movement.west.parser, movement.west)
shared.ACTION_DICT['w'] = (movement.west.parser, movement.west)
shared.ACTION_DICT['northwest'] = (movement.northwest.parser, 
    movement.northwest)
shared.ACTION_DICT['nw'] = (movement.northwest.parser, 
    movement.northwest)
shared.ACTION_DICT['up'] = (movement.up.parser, movement.up)
shared.ACTION_DICT['u'] = (movement.up.parser, movement.up)
shared.ACTION_DICT['down'] = (movement.down.parser, movement.down)
shared.ACTION_DICT['d'] = (movement.down.parser, movement.down)
shared.ACTION_DICT['enter'] = (movement.enter.parser, movement.enter)
shared.ACTION_DICT['exit'] = (movement.exit.parser, movement.exit)
shared.ACTION_DICT['recall'] = (movement.recall.parser, movement.recall)


