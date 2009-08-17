# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/monitor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from driver.log import THE_LOG
from driver.config import IDLE_TIMEOUT
from mudlib import shared
from mudlib.commands.speech import broadcast


## You'll notice that we keep two lists of clients; LOBBY_LIST and PLAY_LIST.
## They are split so we can handle them differently.  For instance, you
## wouldn't broadcast the disconnection of someone from the Welcome screen.


#--------------------------------------------------------------Test Connections

def test_connections():

    """Iterate through the clients and check for dead connections."""

    #print len(shared.LOBBY), len(shared.PLAYERS)

    for client in shared.LOBBY:
        if client.conn.active == False:
            client.deactivate()

    for client in shared.PLAYERS:
        if client.conn.active == False:
            client.deactivate()
            broadcast('%s has gone offline.\n' % client.name)    


#-------------------------------------------------------------Kill Idle Clients
                
def kill_idle_clients():

    """
    Test for and drop clients who aren't doing anything.  I might merge this
    with test_connections().
    """

    for client in shared.LOBBY:
        if client.conn.idle() > IDLE_TIMEOUT:
            THE_LOG.add('Kicking idle lobby client from %s' % 
                client.conn.addrport())
            client.deactivate()
            
    for client in shared.PLAYERS:
        if client.conn.idle() > IDLE_TIMEOUT:
            THE_LOG.add('Kicking idle %s from %s' % (
                client.name, client.conn.addrport()))
            client.deactivate()
            broadcast('%s has gone offline.\n' % client.name)


#------------------------------------------------------------Purge Dead Clients

def purge_dead_clients():

    """
    Remove all clients that are flagged inactive.  This will also close their
    sockets when their Connections are garbage collected.
    """

    shared.LOBBY = [ client for client in shared.LOBBY 
        if client.active == True ]
        
    shared.PLAYERS = [ client for client in shared.PLAYERS 
        if client.active == True ]         


#----------------------------------------------------------Process Client Input
        
def process_client_commands():

    """Test clients for commands and process them."""

    for client in shared.LOBBY:
        if client.active and client.conn.active:
            if client.conn.cmd_ready:
                client.process_command()

    for client in shared.PLAYERS:
        if client.active and client.conn.active:
            if client.conn.cmd_ready:
                client.process_command()

