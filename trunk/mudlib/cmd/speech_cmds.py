# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmd/speech_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib import action
from mudlib.lang import parsers


@parsers.monologue
def emote(client, msg):
    """
    Displays an emote to everyone in the room.
    """
    room = client.get_room()
    room.tell_all('^G... %s %s^w\n' % (client.name, msg))


@parsers.dialogue
def tell(client, target, msg):
    """
    Send message from client to client.
    """
    if client == target:
        target.send('^mYou tell yourself^w, %s\n' % msg)
    else:
        target.send('^M%s tells you^w, %s\n' % (client.name, msg))
        client.send('^mYou tell %s^w, %s\n' % (target.name, msg))
        ## note the sender so that a reply works
        target.last_tell = client.name


@parsers.monologue
def reply(client, msg):
    """
    Shortcut that tells to the last person who sent you one.
    """
    if client.last_tell:
        target = shared.find_player(client.last_tell)
        if target:
            target.send('^M%s replies^w, %s\n' % (client.name, msg))
            client.send('^mYou reply to %s^w, %s\n' % (target.name, msg))
            ## note the sender so that a reply works
            target.last_tell = client.name
        else:
            client.alert('%s is no longer online.\n' % client.last_tell)
    else:
        client.alert('You have not recieved anything to reply to.\n')


@parsers.monologue
def ooc(client, msg):
    """
    Sends 'message' to every players.
    """
    for player in gvar.PLAYERS:
        if player == client:
            player.send('^gYou OOC^w, %s\n' % msg)
        else:
            player.send('^G%s OOCs^w, %s\n' % (client.name, msg))


@parsers.monologue
def shout(client, msg):
    """
    Sends 'message' to every players.
    """
    for player in gvar.PLAYERS:
        if player == client:
            player.send('^rYou shout^w, %s\n' % msg)
        else:
            player.send('^R%s shouts^w, %s\n' % (client.name, msg))


@parsers.monologue
def say(player, msg):
    """
    Sends message to every player in client's room.
    """
    avatar = player.avatar
    room = avatar.get_room_obj()
    action.tell_all_but(room, '^W%s says^w, %s\n' % (avatar.get_name(), msg),
        avatar)
    player.send('^WYou say^w, %s\n' % msg)
    ## Fire the on hear event
    room.on_hear(avatar, msg)
