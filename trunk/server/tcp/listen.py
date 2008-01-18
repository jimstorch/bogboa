#------------------------------------------------------------------------------
#   File:       listen.py
#   Purpose:    defines the address and port the server uses
#   Author:     Jim Storch
#------------------------------------------------------------------------------

"""Sets the server port to listen for new connections on.""" 

import socket
import sys

ADDRESS = ''
PORT = 7777

THE_SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
THE_SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    THE_SERVER_SOCKET.bind((ADDRESS, PORT))
    THE_SERVER_SOCKET.listen(5)

except socket.error, e:
    print "Unable to create the server socket:", e
    sys.exit(1)
   
