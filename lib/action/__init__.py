##-----------------------------------------------------------------------------
##  File:       ruleset/abilities/__init__.py
##  Purpose:    initialization of stuff needed
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib import shared
from lib.action import speech
from lib.action import system
from lib.action import movement

## Speech
shared.ACTION['tell'] = (speech.tell.parser, speech.tell)
shared.ACTION['t'] = (speech.tell.parser, speech.tell)
shared.ACTION['whisper'] = (speech.tell.parser, speech.tell)
shared.ACTION['wh'] = (speech.tell.parser, speech.tell)
shared.ACTION['reply'] = (speech.reply.parser, speech.reply)
shared.ACTION['r'] = (speech.reply.parser, speech.reply)
shared.ACTION['say'] = (speech.say.parser, speech.say)
shared.ACTION['shout'] = (speech.shout.parser, speech.shout)
shared.ACTION['broadcast'] = (speech.broadcast.parser, speech.broadcast)

## System
shared.ACTION['quit'] = (system.quit.parser, system.quit)
shared.ACTION['look'] = (system.look.parser, system.look)
shared.ACTION['l'] = (system.look.parser, system.look)

## Movement
shared.ACTION['north'] = (movement.north.parser, movement.north)
shared.ACTION['n'] = (movement.north.parser, movement.north)
shared.ACTION['northeast'] = (movement.northeast.parser, 
    movement.northeast)
shared.ACTION['ne'] = (movement.northeast.parser, 
    movement.northeast)
shared.ACTION['east'] = (movement.east.parser, movement.east)
shared.ACTION['e'] = (movement.east.parser, movement.east)
shared.ACTION['southeast'] = (movement.southeast.parser, 
    movement.southeast)
shared.ACTION['se'] = (movement.southeast.parser, 
    movement.southeast)
shared.ACTION['south'] = (movement.south.parser, movement.south)
shared.ACTION['s'] = (movement.south.parser, movement.south)
shared.ACTION['southwest'] = (movement.southwest.parser, 
    movement.southwest)
shared.ACTION['sw'] = (movement.southwest.parser, 
    movement.southwest)
shared.ACTION['west'] = (movement.west.parser, movement.west)
shared.ACTION['w'] = (movement.west.parser, movement.west)
shared.ACTION['northwest'] = (movement.northwest.parser, 
    movement.northwest)
shared.ACTION['nw'] = (movement.northwest.parser, 
    movement.northwest)
shared.ACTION['up'] = (movement.up.parser, movement.up)
shared.ACTION['u'] = (movement.up.parser, movement.up)
shared.ACTION['down'] = (movement.down.parser, movement.down)
shared.ACTION['d'] = (movement.down.parser, movement.down)
shared.ACTION['enter'] = (movement.enter.parser, movement.enter)
shared.ACTION['exit'] = (movement.exit.parser, movement.exit)
shared.ACTION['recall'] = (movement.recall.parser, movement.recall)


