#------------------------------------------------------------------------------
#   File:       abilty/__init__.py
#   Purpose:    mapping of player commands to functions
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from server import shared
from ruleset.abilities import speech

shared.ABILITY_DICT['tell'] = speech.tell


