# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/speech_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Message related actions.
"""

from mudlib import gvar


def tell_all(room, msg):
    """
    Send msg to everyone in a room.
    """
    #print room

    for actor in room.actors:
        if actor.is_player:
            actor.send(msg)


def tell_all_but(room, msg, stinky_pete):
    """
    Send msg to everyone in the room except actor.
    """
    for actor in room.actors:
        if actor.is_player and actor != stinky_pete:
            actor.send(msg)


def broadcast(msg):
    """
    Send a message to all players.
    """
    for client in gvar.PLAYERS:
        client.send(msg)


def broadcast_all(msg):
    """
    Send a message to players and lobby clients.
    """
    broadcast(msg)
    for client in gvar.LOBBY:
        client.send(msg)


def whisper(actor, msg):
    """Transmit msg wrapped in whisper color (dark green)."""
    actor.client.send_cc('^g%s^w' % msg)


def prose(actor, msg):
    """Transmit msg wrapped in reading color (dark white)."""
    actor.client.send_wrapped('^w%s^w\n' % msg)


def inform(actor, msg):
    """Transmit msg wrapped in informing color (bright white)."""
    actor.client.send_cc('^W%s^w' % msg)


def alert(actor, msg):
    """Transmit msg wrapped in alert color (bright yellow)."""
    actor.client.send_cc('^Y%s^w' % msg)


def warn(actor, msg):
    """Transmit msg wrapped in warn color (dark red)."""
    actor.client.send_cc('^r%s^w' % msg)


def exclaim(actor, msg):
    """Transmit msg wrapped in exclaime color (bright red)."""
    actor.client.send_cc('^R%s^w' % msg)
