#------------------------------------------------------------------------------
#   File:       lookup.py
#   Purpose:    matches handles (string) to a game objects
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared


#---[ Find Player ]------------------------------------------------------------

def find_player(handle):

    if shared.HANDLE_DICT.has_key(handle):
        return shared.HANDLE_DICT[handle]

    else:
        return None


