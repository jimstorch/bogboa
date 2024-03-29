# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/monitor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib import action
from mudlib.sys import THE_LOG
from mudlib.sys.config import IDLE_TIMEOUT
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.usr.entrant import Entrant


def on_connect(client):
    """
    Handler for new client connections, called by miniboa server.
    """
    THE_LOG.add('++ New client from %s.' % client.addrport())
    #client.request_terminal_type()
    client.request_naws()
    user = Entrant(client)
    gvar.LOBBY[client] = user


def on_disconnect(client):
    """
    Handler for lost client connections, called by miniboa server.
    """
    if client in gvar.LOBBY:
        THE_LOG.add('-- Lost lobby client from %s.' % client.addrport())
        del gvar.LOBBY[client]

    elif client in gvar.PLAYERS:
        user = gvar.PLAYERS[client]
        avatar = user.avatar
        ## Remove them from the world
        action.leave(avatar, avatar.get_room_obj())
        name = avatar.get_name()
        #broadcast('^g%s has gone offline.^w' % client.name)
        THE_LOG.add('-- Lost player %s from %s.' %
            (name, client.addrport()))
        ## Delete references
        del gvar.PLAYERS[client]
        del gvar.AVATARS[name.lower()]
        #avatar.client = None


def kick_idle_clients():
    """
    Test for and drop clients who aren't doing anything.
    """
    #print len(gvar.LOBBY), len(gvar.PLAYERS), len(gvar.AVATARS)
    for client in gvar.LOBBY:
        if client.idle() > IDLE_TIMEOUT:
            user = gvar.LOBBY[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.send('\n^YIdle timeout.^w\n')
            user.delayed_deactivate()
    for client in gvar.PLAYERS:
        if client.idle() > IDLE_TIMEOUT:
            user = gvar.PLAYERS[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.send('\n^YIdle timeout.^w\n')
            user.delayed_deactivate()


def process_client_commands():
    """
    Test clients for commands and process them.
    """
    for user in gvar.LOBBY.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()
    for user in gvar.PLAYERS.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()


def sweep_rooms():
    """
    Remove rotted items from the floors.
    """
    for room in gvar.ROOMS.values():
        room.sweep()
