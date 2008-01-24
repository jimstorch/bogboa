#------------------------------------------------------------------------------
#   File:       speech.py
#   Purpose:    communication based abilities
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset import parsers
from ruleset import lookup


#---[ Broadcast ]--------------------------------------------------------------

def broadcast(message):

    """Send a message to everyone online."""

    for player in shared.PLAY_LIST:
        player.send(message)

broadcast.parser = None


#---[ Tell ]-------------------------------------------------------------------

def tell(client, target_handle, message):

    """Send message from client to target."""

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

        client.send("^'%s' is not online." % target_handle.capitalize())

## Specify the proper parser for this verb
tell.parser = parsers.dialogue


#---[ Reply ]------------------------------------------------------------------

def reply(client, message):

    """Shortcut that tells to the last person who sent you one."""

    if client.last_tell:
        target_handle = client.last_tell
        tell(client, target_handle, message)

    else:
        client.send('^yYou have not recieved any tells.')
    
reply.parser = parsers.monologue


#---[ Shout ]------------------------------------------------------------------

def shout(client, message):

    """Sends 'message' to every players."""

    for player in shared.PLAY_LIST:

        if player == client:
            client.send('^wYou shout, %s' % message)                
        
        else:
            player.send('^R%s shouts,^W %s' % (client.name, message))

shout.parser = parsers.monologue


#---[ Say ]--------------------------------------------------------------------


def say(client, message):
     pass

## Specify the proper parser for this verb
say.parser = parsers.monologue

