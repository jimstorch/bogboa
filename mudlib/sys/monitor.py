# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/monitor.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import shared
from mudlib.sys.log import THE_LOG
from mudlib.sys.config import IDLE_TIMEOUT
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.usr.entrant import Entrant
from mudlib.usr.cmd_speech import broadcast


#--------------------------------------------------------------------On Connect

def on_connect(client):

    """
    Handler for new client connections, called by miniboa server.
    """

    THE_LOG.add('++ New client from %s.' % client.addrport())
    client.request_terminal_type()
    client.request_naws()
    user = Entrant(client)
    shared.LOBBY_CLIENTS[client] = user

#-----------------------------------------------------------------On Disconnect

def on_disconnect(client):

    """
    Handler for lost client connections, called by miniboa server.
    """

    if client in shared.LOBBY_CLIENTS:
        THE_LOG.add('-- Lost entrant client from %s.' % client.addrport())
        user = shared.LOBBY_CLIENTS[client]
        del user.cmd_driver
        del shared.LOBBY_CLIENTS[client]
        del user
        # force garbage collection of Client to drop socket
        #del user.client
        #del user

    elif client in shared.PLAY_CLIENTS:
        user = shared.PLAY_CLIENTS[client]
        broadcast('^g%s has gone offline.^w' % client.name)
        THE_LOG.add('-- Deactivated player %s from %s.' %
            (user.name, client.addrport()))
        del shared.PLAY_CLIENTS[client]
        del user.client

#-------------------------------------------------------------Kill Idle Clients

def kick_idle_clients():

    """
    Test for and drop clients who aren't doing anything.
    """

    print len(shared.LOBBY_CLIENTS), len(shared.PLAY_CLIENTS)


    for client in shared.LOBBY_CLIENTS.keys():
        if client.idle() > IDLE_TIMEOUT:
            user = shared.LOBBY_CLIENTS[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.inform('\nIdle timeout.\n')
            user.delayed_deactivate()

    for client in shared.PLAY_CLIENTS.keys():
        if client.idle() > IDLE_TIMEOUT:
            user = shared.LOBBY_CLIENTS[client]
            THE_LOG.add('-- Kicking idle client from %s' % client.addrport())
            user.inform('\nIdle timeout.\n')
            user.delayed_deactivate()


#----------------------------------------------------------Process Client Input

def process_client_commands():

    """Test clients for commands and process them."""

    for user in shared.LOBBY_CLIENTS.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()

    for user in shared.PLAY_CLIENTS.values():
        if user.client.active and user.client.cmd_ready:
            user.cmd_driver()

#-------------------------------------------------------------------Sweep Rooms

#def sweep_rooms():

#    """Remove rotted items from the floors."""

#    for uuid in shared.ROOMS.keys():
#        shared.ROOMS[uuid].sweep()
