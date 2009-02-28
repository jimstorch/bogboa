# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/tcp/async.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

"""Handle Asynchronous Telnet Connections."""

import socket
import select
import sys

from driver.log import THE_LOG
from driver.tcp.telnet import Telnet
#from driver.tcp.listen import THE_SERVER_SOCKET

from driver.config import ADDRESS
from driver.config import PORT

from driver.connect import lobby_connect
from mudlib import shared


# TODO: add a real source here
BAN_LIST = []   


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
                THE_LOG.add('Closed connection to %s' % conn.addrport()) 
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
            THE_LOG.add("FATAL SELECT error '%d:%s'!" % (err[0], err[1])) 
            sys.exit(1)

        ## Process socket file descriptors with data to recieve
        for sockfd in rlist:

            ## If it's coming from the server's socket then this is a new
            ## connection request.
            if sockfd == self.server_fd:
            
                try:
                    sock, addr_tup = self.server_socket.accept()
                    
                except socket.error, err:
                    THE_LOG.add("ACCEPT error '%d:%s'." % (err[0], err[1]))  
                    continue          

                ## Check for banned IP's
                if addr_tup[0] in BAN_LIST:
                    THE_LOG.add("BANNED IP connection refused from %s:%s." % (
                        addr_tup[0], addr_tup[1]))
                    continue                     
              
                conn = Telnet(sock, addr_tup)
                THE_LOG.add("Opened new connection to %s" % conn.addrport())
                ## Add the connection to our dictionary
                self.fdconn[conn.fileno] = conn

                ## Whatever we do with new connections goes here:
   
                lobby_connect(conn)


                #shared.LOBBY_LIST.append(WelcomeMode(conn))

            else:
                ## Call the connection's recieve method
                #print "calling conn %d _recv" % sockfd            
                self.fdconn[sockfd].socket_recv()
         
        ## Process sockets with data to send
        for sockfd in slist:
            ## Call the connection's send method            
            self.fdconn[sockfd].socket_send()


#--[ Global Instance ]---------------------------------------------------------

THE_PORT_AUTHORITY = PortAuthority(THE_SERVER_SOCKET)

#------------------------------------------------------------------------------

