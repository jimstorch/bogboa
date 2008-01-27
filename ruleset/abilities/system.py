#------------------------------------------------------------------------------
#   File:       system.py
#   Purpose:    general system abilitites
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset import parsers


#---[ Look ]-------------------------------------------------------------------

def look(client):

    """Look at the current room."""

    client.send('^C' + client.room.view)

look.parser = None

#---[ Quit ]-------------------------------------------------------------------

def quit(client):

    """Exit from the game."""

    client.deactivate()

quit.parser = None



