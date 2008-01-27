#------------------------------------------------------------------------------
#   File:       server.py
#   Purpose:    maintainance functions and such
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from server.log import THE_LOG
from ruleset.abilities.speech import broadcast


## You'll notice that we keep two lists of clients; LOBBY_LIST and PLAY_LIST.
## They are split so we can handle them differently.  For instance, you
## wouldn't broadcast the disconnection of someone from the Welcome screen.


#---[ Test Connections ]-------------------------------------------------------

def test_connections():

    """Iterate through the clients and check for dead connections."""

    for client in shared.LOBBY_LIST:
        if client.conn.active == False:
            client.deactivate()

    for client in shared.PLAY_LIST:
        if client.conn.active == False:
            client.deactivate()
            broadcast('^y%s has gone offline.' % client.name)    


#---[ Kill Idle Clients ]------------------------------------------------------
                
def kill_idle_clients():

    """
    Test for and drop clients who aren't doing anything.  I might merge this
    with test_connections().
    """

    for client in shared.LOBBY_LIST:
        if client.conn.idle() > 3000:
            THE_LOG.add('Kicking idle lobby client from %s' %  
                client.conn.addrport())
            client.deactivate()
            
    for client in shared.PLAY_LIST:
        if client.conn.idle() > 3000:
            THE_LOG.add('Kicking idle gameplay client %s from %s' % (
                client.name, client.conn.addrport()))
            client.deactivate()
            broadcast('^y%s has gone offline.' % client.name)


#---[ Purge Dead Clients ]-----------------------------------------------------

def purge_dead_clients():

    """
    Remove all clients that are flagged inactive.  This will also close their
    sockets when their Connections are garbage collected.
    """

    shared.LOBBY_LIST = [ client for client in shared.LOBBY_LIST 
        if client.active == True ]
        
    shared.PLAY_LIST = [ client for client in shared.PLAY_LIST 
        if client.active == True ]         


#---[ Process Client Input ]---------------------------------------------------
        
def process_client_commands():

    """Test clients for commands and process them."""

    for client in shared.LOBBY_LIST:
        if client.active and client.conn.active:
            if client.conn.cmd_ready:
                client.process_command()

    for client in shared.PLAY_LIST:
        if client.active and client.conn.active:
            if client.conn.cmd_ready:
                client.process_command()


#---[ Is Online ]--------------------------------------------------------------
     
def is_online(handle):

    """Check if a player with the given handle is currently playing."""
    
    if shared.HANDLE_DICT.has_key(handle):
        return True
    else:
        return False


