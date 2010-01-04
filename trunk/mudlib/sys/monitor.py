# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/monitor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import LOBBY, PLAYERS, ROOMS
from mudlib.sys import THE_LOG
from mudlib.sys.config import IDLE_TIMEOUT
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.usr.entrant import Entrant
from mudlib.cmd.speech import broadcast


def on_connect(client):
    """
    Handler for new client connections, called by miniboa server.
    """
    THE_LOG.add('++ New client from %s.' % client.addrport())
    client.request_terminal_type()
    client.request_naws()
    user = Entrant(client)
    LOBBY[client] = user


def on_disconnect(client):
    """
    Handler for lost client connections, called by miniboa server.
    """
    if client in LOBBY:
        THE_LOG.add('-- Lost lobby client from %s.' % client.addrport())
        del LOBBY[client]

    elif client in PLAYERS:
        user = PLAYERS[client]
        broadcast('^g%s has gone offline.^w' % client.name)
        THE_LOG.add('-- Deactivated player %s from %s.' %
            (user.name, client.addrport()))
        del PLAYERS[client]


def kick_idle_clients():
    """
    Test for and drop clients who aren't doing anything.
    """
    for client in LOBBY:
        if client.idle() > IDLE_TIMEOUT:
            user = LOBBY[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.inform('\nIdle timeout.\n')
            user.delayed_deactivate()
    for client in PLAYERS:
        if client.idle() > IDLE_TIMEOUT:
            user = LOBBY[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.inform('\nIdle timeout.\n')
            user.delayed_deactivate()


def process_client_commands():
    """
    Test clients for commands and process them.
    """

    print len(LOBBY), len(PLAYERS)

    for user in LOBBY.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()
    for user in PLAYERS.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()


def sweep_rooms():
    """
    Remove rotted items from the floors.
    """
    for room in ROOMS.values():
        room.sweep()
