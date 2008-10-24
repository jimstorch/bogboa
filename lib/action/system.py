##-----------------------------------------------------------------------------
##  File:       lib/action/system.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib import parsers


#--------------------------------------------------------------------------Quit

def quit(client):

    """Exit from the game."""

    client.deactivate()

quit.parser = None



