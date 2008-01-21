#------------------------------------------------------------------------------
#   File:       speech.py
#   Purpose:    communication based abilities
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset import parsers


#---[ Quit ]-------------------------------------------------------------------

def quit(client):

    """Exit from the game."""

    client.deactivate()

quit.parser = None





