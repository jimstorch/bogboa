# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmd/system_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------


from mudlib.sys import THE_LOG
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.usr import parsers
#from mudlib.dat.map import set_ansi

#--------------------------------------------------------------------------Ansi
@parsers.set_or_show
def ansi(player, setting):

    """Turn on or off ANSI color.  No parameters means show current setting."""

    if setting == None:
        curr = player.client.use_ansi
        if curr:
            use = 'on'
        else:
            use = 'off'
        player.send('^YANSI^W is currently set to %s.^w' % use)

    elif setting == True:
        player.client.use_ansi = True
        player.send('^WSetting ^YANSI^W to on.^w')
        ## store preference in database
        #set_ansi(client.name, True)

    else:
        player.client.use_ansi = False
        player.send('Setting ANSI to off.')
        ## store preference in database
        #set_ansi(client.name, False)

#--------------------------------------------------------------------------Quit

@parsers.blank
def quit(player):

    """Exit from the game."""

    player.send('\n^YLogging you off -- take care.^w\n')
    THE_LOG.add('.. %s quits from %s' % (player.avatar.get_name(),
        player.client.addrport()))
    THE_SCHEDULER.add(.10, player.deactivate)

#---------------------------------------------------------------------------Bug

def bug(player):

    """Permit the player to report a bug to the bug log."""

    pass
