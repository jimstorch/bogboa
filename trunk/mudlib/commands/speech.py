# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/commands/speech.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib import lookup


#---------------------------------------------------------------------Broadcast

def broadcast(msg):

    """Send a message to all players."""

    for client in shared.PLAYERS:
        client.send(msg)


#-----------------------------------------------------------------All Broadcast

def broadcast_all(msg):

    """Send a message to players and lobby clients."""

    broadcast(msg)

    for client in shared.LOBBY:
        client.send(msg)


#-------------------------------------------------------------------------Emote

def emote(client):

    """Displays an emote to everyone in the room."""

    pass


#--------------------------------------------------------------------------Tell

def tell(client):

    """
    Send message from client to client's target.
    """

    target = lookup.find_player(target_handle)

    if target:

        if client == target:
            target.send('^MYou tell yourself,^W %s' % message)

        else:
            target.send('^M%s tells you,^W %s' % (client.name, message))
            client.send('^wYou tell %s, %s' % (target.name, message))
        
        ## note the sender so that a reply works
        target.last_tell = client.handle   

    else:

        client.send("^y%s is not in this world." % target_handle.capitalize())


#-------------------------------------------------------------------------Reply

def reply(client):

    """Shortcut that tells to the last person who sent you one."""

    if client.last_tell:
        target_handle = client.last_tell
        tell(client, target_handle, message)

    else:
        client.send('^yYou have not recieved any tells.')
    

#---------------------------------------------------------------------------OOC

def ooc(client):

    """Sends 'message' to every players."""

    for player in shared.PLAY_LIST:

        if player == client:
            client.send('^wYou OOC; %s' % message)                
        
        else:
            player.send('^R%s OOC; ^W %s' % (client.name, message))


#-------------------------------------------------------------------------Shout

def shout(client):

    """Sends 'message' to every players."""

    for player in shared.PLAY_LIST:

        if player == client:
            client.send('^wYou shout, %s' % message)                
        
        else:
            player.send('^R%s shouts,^W %s' % (client.name, message))


#---------------------------------------------------------------------------Say

def say(client):
    
    """Sends message to every player in client's room."""

    client.room.tell_all_but(client, '^w%s says,^W %s' % (client.name, 
        message))
    client.send('^wYou say, %s' % message)    


