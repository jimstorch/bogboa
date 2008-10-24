##-----------------------------------------------------------------------------
##  File:       lib/action/info.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

from lib import parsers


#--------------------------------------------------------------------------Look

def look(client):

    """Look at the current room."""

    client.send('^C' + word_wrap(client.room.view, client.conn.columns))

look.parser = None
