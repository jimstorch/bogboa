# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/system.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.scheduler import THE_SCHEDULER
from driver.log import THE_LOG
from mudlib import parsers
from driver.dbms.map import set_ansi

#--------------------------------------------------------------------------Ansi
@parsers.set_or_show
def ansi(client, setting):

    """Turn on or off ANSI color.  No parameters means show current setting."""
    
    if setting == None:
        curr = client.conn.use_ansi
        if curr:
            use = 'on'
        else:
            use = 'off'
        client.send('^mANSI is currently set to %s.^w' % use)

    elif setting == True:
        client.conn.use_ansi = True
        client.send('^mSetting ANSI to on.^w')
        ## store preference in database
        set_ansi(client.name, True)

    else:
        client.conn.use_ansi = False
        client.send('Setting ANSI to off.')
        ## store preference in database         
        set_ansi(client.name, False)

#--------------------------------------------------------------------------Quit

@parsers.blank
def quit(client):

    """Exit from the game."""

    client.send('Logging you off -- take care.')
    THE_LOG.add('.. %s quits from %s' % (client.name, client.origin()))
    THE_SCHEDULER.add(.10, client.deactivate)

#---------------------------------------------------------------------------Bug

def bug(client):

    """Permit the player to report a bug to the bug log."""

    pass
