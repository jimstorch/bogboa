# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/speech.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared
from mudlib import parsers

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

@parsers.monologue
def emote(client, msg):

    """Displays an emote to everyone in the room."""

    pass


#--------------------------------------------------------------------------Tell
@parsers.dialogue
def tell(client, target, msg):

    """
    Send message from client to client.
    """


    if client == target:
        target.send('You tell yourself, %s' % msg)

    else:
        target.send('%s tells you, %s' % (client.name, msg))
        client.send('You tell %s, %s' % (target.name, msg))
        
        ## note the sender so that a reply works
        target.last_tell = client.name  


#-------------------------------------------------------------------------Reply

@parsers.monologue
def reply(client, msg):

    """Shortcut that tells to the last person who sent you one."""

    if client.last_tell:
        target = shared.find_player(client.last_tell)
        if target:
            target.send('%s replies, %s' % (client.name, msg))
            client.send('You reply to %s, %s' % (target.name, msg))

            ## note the sender so that a reply works
            target.last_tell = client.name  

        else:
            client.send('%s is no longer online.\n' % client.last_tell)    

    else:
        client.send('You have not recieved anything to reply to.')
    

#---------------------------------------------------------------------------OOC

@parsers.monologue
def ooc(client, msg):

    """Sends 'message' to every players."""

    for player in shared.PLAYERS:

        if player == client:
            player.send('You OOC; %s\n' % msg)                
        
        else:
            player.send('%s OOC; %s\n' % (client.name, msg))


#-------------------------------------------------------------------------Shout

@parsers.monologue
def shout(client, msg):

    """Sends 'message' to every players."""

    for player in shared.PLAYERS:

        if player == client:
            player.send('You shout, %s\n' % msg)                
        
        else:
            player.send('%s shouts, %s\n' % (client.name, msg))


#---------------------------------------------------------------------------Say

@parsers.monologue
def say(client, msg):
    
    """Sends message to every player in client's room."""

    body = client.body
    room = shared.ROOMS[body.room_uuid]

    room.tell_all_but(body, '%s says, %s\n' % (body.name, msg))
    client.send('You say, %s\n' % msg)    


