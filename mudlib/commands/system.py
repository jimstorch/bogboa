# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/system.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.scheduler import THE_SCHEDULER

#--------------------------------------------------------------------------Quit

def quit(client):

    """Exit from the game."""

    client.send('Logging you off -- take care.')
    THE_SCHEDULER.add(.10, client.deactivate)

#---------------------------------------------------------------------------Bug

def bug(client):

    """Permit the player to report a bug to the bug log."""

    pass
