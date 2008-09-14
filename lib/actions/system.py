#------------------------------------------------------------------------------
#   File:       system.py
#   Purpose:    general system abilitites
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset import parsers
from server.decorate import word_wrap


#---[ Look ]-------------------------------------------------------------------

def look(client):

    """Look at the current room."""

    client.send('^C' + word_wrap(client.room.view, client.conn.columns))

look.parser = None

#---[ Quit ]-------------------------------------------------------------------

def quit(client):

    """Exit from the game."""

    client.deactivate()

quit.parser = None



