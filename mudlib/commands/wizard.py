# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/wizard.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

#from mudlib import parsers
from driver.scheduler import THE_SCHEDULER
from mudlib.commands.speech import broadcast
from mudlib import shared

#---------------------------------------------------------------------------Ban

def ban(client):
    pass


#-------------------------------------------------------------------------Grant

def grant(client):
    pass


#--------------------------------------------------------------------------Kick

def kick(client):
    pass


#------------------------------------------------------------------------Revoke

def revoke(client):
    pass


#----------------------------------------------------------------------Shutdown

def shutdown(client):

    """Shutdown the server with a ten second warning to users."""

    def second_warning():
        broadcast("\n!! Server shutdown in 5 seconds. Please log off.\n")

    def kill():
        shared.SERVER_RUN = False

    if client.verb_args:
        client.send('\nShutdown command takes no arguments.')
        
    else:
        broadcast("\n!! Server shutdown in 10 seconds.  Please log off.\n")
        THE_SCHEDULER.add(5, second_warning)
        THE_SCHEDULER.add(10, kill)


#------------------------------------------------------------------------Summon

def summon(client):
    pass


#----------------------------------------------------------------------Teleport

def teleport(client):
    pass


#---------------------------------------------------------------------------Zap

def zap(client):
    pass


