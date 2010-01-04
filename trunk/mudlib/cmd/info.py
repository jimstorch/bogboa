# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/cmd_info.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib.sys.error import BogCmdError
from mudlib.usr import parsers
from mudlib.world import calendar


#----------------------------------------------------------------------Commands
@parsers.blank
def commands(client):

    """List the player's granted command set."""

    clist = list(client.commands)
    clist.sort()
    cmds = ', '.join(clist)
    client.send('Your current commands are: ^W%s^w' % cmds)

#------------------------------------------------------------------------Topics
@parsers.blank
def topics(client):

    """List the player's granted command set."""

    tlist = list(gvar.HELPS.keys())
    tlist.sort()
    topics = ', '.join(tlist)
    client.send('Available help topics are: ^W%s^w' % topics)


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
    client.send('Your current stats: ^W%s^w' % s)


#--------------------------------------------------------------------------Look
@parsers.blank
def look(client):

    """Look at the current room."""

    room = client.body.room
    room.client_see(client)


#--------------------------------------------------------------------------Help
@parsers.none_or_one
def help(client, arg):

    """Display the selected help text."""

    if arg != None:
        topic = arg.lower()
        if topic in gvar.HELPS:
            client.prose(HELPS[topic].text)
        else:
            raise BogCmdError('Help topic not found')

    else:
        client.prose(gvar.HELPS['help'].text)


#-------------------------------------------------------------------------Score

def score(client):

    """Fix Me"""

    pass

#--------------------------------------------------------------------------Time
@parsers.blank
def time(client):

    """Tell the client the current game time."""

    client.inform('The time is %s.' % calendar.time_msg())


#--------------------------------------------------------------------------Date
@parsers.blank
def date(client):

    """Tell the client the current game date."""

    client.inform('The date is %s.' % calendar.date_msg())



#---------------------------------------------------------------------Inventory

def inventory(client):

    """Fix Me"""

    pass
