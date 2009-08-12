# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/action/info.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib.shared import HELPS


#----------------------------------------------------------------------Commands

def commands(client):

    """List the player's granted command set."""

    clist = list(client.commands)
    clist.sort()
    cmds = ', '.join(clist)
    client.send('Your current commands are:\n%s' % cmds)

#--------------------------------------------------------------------------Look

def look(client):

    """Look at the current room."""

    client.send('^C' + word_wrap(client.room.view, client.conn.columns))


#--------------------------------------------------------------------------Help

def help(client):

    """Display the selected help text."""

    if client.verb_args:

        topic = client.verb_args[0].lower()
        if topic in HELPS:
            client.send(HELPS[topic].text)
        else:
            client.send("Help topic not found.")

    else:
        client.send(HELPS['help'].text)
    

#-------------------------------------------------------------------------Score

def score(client):

    """Fix Me"""

    pass

#--------------------------------------------------------------------------Time

def time(body):

    """Fix Me"""

    pass

#---------------------------------------------------------------------Inventory

def inventory(body):

    """Fix Me"""

    pass
