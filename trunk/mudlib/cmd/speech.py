# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/cmd_speech.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib.usr import parsers

#---------------------------------------------------------------------Broadcast

def broadcast(msg):

    """Send a message to all players."""

    for client in gvar.PLAYERS:
        client.send(msg)


#-----------------------------------------------------------------All Broadcast

def broadcast_all(msg):

    """Send a message to players and lobby clients."""

    broadcast(msg)

    for client in gvar.LOBBY:
        client.send(msg)


#-------------------------------------------------------------------------Emote

@parsers.monologue
def emote(client, msg):

    """Displays an emote to everyone in the room."""

    room = client.get_room()
    room.tell_all('^G... %s %s^w' % (client.name, msg))

#--------------------------------------------------------------------------Tell
@parsers.dialogue
def tell(client, target, msg):

    """
    Send message from client to client.
    """


    if client == target:
        target.send('^mYou tell yourself^w, %s' % msg)

    else:
        target.send('^M%s tells you^w, %s' % (client.name, msg))
        client.send('^mYou tell %s^w, %s' % (target.name, msg))

        ## note the sender so that a reply works
        target.last_tell = client.name


#-------------------------------------------------------------------------Reply

@parsers.monologue
def reply(client, msg):

    """Shortcut that tells to the last person who sent you one."""

    if client.last_tell:
        target = shared.find_player(client.last_tell)
        if target:
            target.send('^M%s replies^w, %s' % (client.name, msg))
            client.send('^mYou reply to %s^w, %s' % (target.name, msg))

            ## note the sender so that a reply works
            target.last_tell = client.name

        else:
            client.alert('%s is no longer online.\n' % client.last_tell)

    else:
        client.alert('You have not recieved anything to reply to.')


#---------------------------------------------------------------------------OOC

@parsers.monologue
def ooc(client, msg):

    """Sends 'message' to every players."""

    for player in gvar.PLAYERS:

        if player == client:
            player.send('^gYou OOC^w, %s' % msg)

        else:
            player.send('^G%s OOCs^w, %s' % (client.name, msg))


#-------------------------------------------------------------------------Shout

@parsers.monologue
def shout(client, msg):

    """Sends 'message' to every players."""

    for player in gvar.PLAYERS:

        if player == client:
            player.send('^rYou shout^w, %s' % msg)

        else:
            player.send('^R%s shouts^w, %s' % (client.name, msg))


#---------------------------------------------------------------------------Say

@parsers.monologue
def say(client, msg):

    """Sends message to every player in client's room."""

    room = client.get_room()
    body = client.body

    room.tell_all_but(body, '^W%s says^w, %s' % (body.name, msg))
    client.send('^WYou say^w, %s' % msg)

    ## Fire the on hear event
    room.on_hear(client.body, msg)
