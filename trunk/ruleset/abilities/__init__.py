#------------------------------------------------------------------------------
#   File:       ruleset/abilities/__init__.py
#   Purpose:    initialization of stuff needed
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared
from ruleset.abilities import speech

shared.ABILITY_DICT['tell'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['t'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['whisper'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['w'] = (speech.tell.parser, speech.tell)
shared.ABILITY_DICT['reply'] = (speech.reply.parser, speech.reply)
shared.ABILITY_DICT['r'] = (speech.reply.parser, speech.reply)
shared.ABILITY_DICT['shout'] = (speech.shout.parser, speech.shout)
