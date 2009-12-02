# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/tcp/async.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""Handle Asynchronous Telnet Connections."""

import socket
import select
import sys

from driver.error import BogClientError
from driver.log import THE_LOG
from driver.tcp.telnet import Telnet
from driver.config import ADDRESS
from driver.config import PORT
from driver.connect import lobby_connect
from driver.dbms.map import check_banned_ip
from mudlib import shared

## Cap sockets to 512 on Windows because winsock can only process 512 at time
if sys.platform == 'win32':
    MAX_CONNECTIONS = 512
## Cap sockets to 1000 on Linux because you can only have 1024 file descriptors
else:
    MAX_CONNECTIONS = 1000

#--[ Open the Server's Socket ]------------------------------------------------

THE_SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
THE_SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    THE_SERVER_SOCKET.bind((ADDRESS, PORT))
    THE_SERVER_SOCKET.listen(5)

except socket.error, e:
    print "Unable to create the server socket:", e
    sys.exit(1)


#----------------------------------------------------------------Port Authority

class PortAuthority(object):

    """Poll sockets for new connections and sending/receiving data from
    clients."""

    def __init__(self, server_socket):

        self.server_socket = server_socket
        self.server_fd = server_socket.fileno()

        ## Dictionary of active connections
        self.fdconn = {}

    def connection_count(self):
        """Returns the number of active connections."""
        return len(self.fdconn)


    def poll(self):
        """Perform a non-blocking scan of recv and send states on the server
        and client connection sockets.  Process new connection requests,
        read incomming data, and send outgoing data.  Sends and receives may
        be partial.
        """

        ## Build a list of connections to test for receive data pending
        recv_list = [self.server_fd]    # always add the server
        for conn in self.fdconn.values():
            if conn.active:
                recv_list.append(conn.fileno)
            ## Delete inactive connections from the dictionary
            else:
                THE_LOG.add('-- Closed connection to %s' % conn.addrport())
                del self.fdconn[conn.fileno]

        ## Build a list of connections that need to send data
        send_list = []
        for conn in self.fdconn.values():
            if conn.send_pending:
                send_list.append(conn.fileno)

        ## Get active socket file descriptors from select.select()
        try:
            rlist, slist, elist = select.select(recv_list, send_list, [], 0)

        except select.error, err:
            ## If we can't even use select(), game over man, game over
            THE_LOG.add("!! FATAL SELECT error '%d:%s'!" % (err[0], err[1]))
            sys.exit(1)

        ## Process socket file descriptors with data to recieve
        for sockfd in rlist:

            ## If it's coming from the server's socket then this is a new
            ## connection request.
            if sockfd == self.server_fd:

                try:
                    sock, addr_tup = self.server_socket.accept()

                except socket.error, err:
                    THE_LOG.add("!! ACCEPT error '%d:%s'." % (err[0],
                        err[1]))
                    continue

                ## Check for banned IP's
                if check_banned_ip(addr_tup[0]):
                    THE_LOG.add("?? BANNED IP rejected from %s:%s."
                        % (addr_tup[0], addr_tup[1]))
                    sock.close()
                    continue

                ## Check for maximum connections
                if self.connection_count() >= ( MAX_CONNECTIONS ):
                    THE_LOG.add('?? Refusing new connection; maximum in use.')
                    sock.close()
                    continue

                conn = Telnet(sock, addr_tup)
                THE_LOG.add("++ Opened connection to %s" % conn.addrport())
                ## Add the connection to our dictionary
                self.fdconn[conn.fileno] = conn

                ## Whatever we do with new connections goes here:
                lobby_connect(conn)

            else:
                ## Call the connection's recieve method
                try:
                    self.fdconn[sockfd].socket_recv()
                except BogClientError, err:
                    THE_LOG.add("-- %s" % err)

        ## Process sockets with data to send
        for sockfd in slist:
            ## Call the connection's send method
            self.fdconn[sockfd].socket_send()


#--[ Global Instance ]---------------------------------------------------------

THE_PORT_AUTHORITY = PortAuthority(THE_SERVER_SOCKET)

#------------------------------------------------------------------------------
