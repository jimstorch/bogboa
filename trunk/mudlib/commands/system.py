# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/action/system.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from driver.scheduler import THE_SCHEDULER

#--------------------------------------------------------------------------Quit

def quit(client):

    """Exit from the game."""

    client.send('Logging you off -- Take care.')
    THE_SCHEDULER.add(.10, client.deactivate)

#---------------------------------------------------------------------------Bug

def bug(client):

    """Permit the player to report a bug to the bug log."""

    pass
