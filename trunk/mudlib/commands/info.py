# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/info.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib import parsers
from mudlib import calendar

#----------------------------------------------------------------------Commands
@parsers.blank
def commands(client):

    """List the player's granted command set."""

    clist = list(client.commands)
    clist.sort()
    cmds = ', '.join(clist)
    client.send('Your current commands are: %s' % cmds)


#-------------------------------------------------------------------------Stats
@parsers.blank
def stats(client):

    """List the player's stats."""
    
    body = client.get_body()
    stats = body.stats.keys()
    stats.sort()
    s = ''
    for stat in stats:
        s += '%s=%s ' % (stat.upper(), body.stats[stat])
    client.send('Your current stats: %s' % s)


#--------------------------------------------------------------------------Look

def look(client):

    """Look at the current room."""

    room = shared.ROOMS[client.body.room_uuid]
    client.send(room.desc)


#--------------------------------------------------------------------------Help
@parsers.none_or_one
def help(client, arg):

    """Display the selected help text."""

    if arg != None:
        topic = arg.lower()
        if topic in shared.HELPS:
            client.send(shared.HELPS[topic].text)
        else:
            client.send("Help topic not found.")

    else:
        client.send(shared.HELPS['help'].text)
    

#-------------------------------------------------------------------------Score

def score(client):

    """Fix Me"""

    pass

#--------------------------------------------------------------------------Time
@parsers.blank
def time(client):

    """Tell the client the current game time."""
    
    client.send('The time is %s.' % calendar.time_msg())


#--------------------------------------------------------------------------Date
@parsers.blank
def date(client):

    """Tell the client the current game date."""
    
    client.send('The date is %s.' % calendar.date_msg())



#---------------------------------------------------------------------Inventory

def inventory(client):

    """Fix Me"""

    pass
