# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/action/info.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from lib import parsers
from lib.shared import HELP

#--------------------------------------------------------------------------Look

def look(client):

    """Look at the current room."""

    client.send('^C' + word_wrap(client.room.view, client.conn.columns))


#--------------------------------------------------------------------------Help

def help(client):

    """Display the selected help text."""

    if client.verb_args:

        topic = client.verb_args[0].lower()
        if topic in HELP:
            client.send(HELP[topic].text)
        else:
            client.send("Help topic not found.")

    else:
        client.send(HELP['help'].text)
    

#-------------------------------------------------------------------------Score

def score(client):

    """Fix Me"""

    pass

#--------------------------------------------------------------------------Time

def time(client):

    """Fix Me"""

    pass

#---------------------------------------------------------------------Inventory

def inventory(client):

    """Fix Me"""

    pass
