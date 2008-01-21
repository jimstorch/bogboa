#------------------------------------------------------------------------------
#   File:       system.py
#   Purpose:    general system abilitites
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset import parsers


#---[ Quit ]-------------------------------------------------------------------

def quit(client):

    """Exit from the game."""

    client.deactivate()

quit.parser = None





