#!/usr/bin/env python
#------------------------------------------------------------------------------
#   server_start.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import gc
gc.set_debug(gc.DEBUG_LEAK)

from miniboa import TelnetServer

from mudlib import gvar
from mudlib.sys import THE_LOG
from mudlib.sys.config import PORT
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.sys.scheduler import Cycle
from mudlib.sys.scheduler import Series
from mudlib.sys.monitor import on_connect
from mudlib.sys.monitor import on_disconnect
from mudlib.sys.monitor import kick_idle_clients
from mudlib.sys.monitor import process_client_commands
from mudlib.sys.monitor import sweep_rooms
from mudlib.dat import load_module
from mudlib.dat import check_database


THE_LOG.add(">> **************")
THE_LOG.add(">> server started")
THE_LOG.add(">> **************")


#------------------------------------------------------------------------------
#       Validate the SQLite Database
#------------------------------------------------------------------------------

check_database()


#------------------------------------------------------------------------------
#       Load Game Data
#------------------------------------------------------------------------------

load_module('data/base')
load_module('data/testville')


#------------------------------------------------------------------------------
#       Schedule Repeating Events
#------------------------------------------------------------------------------

Cycle(2, kick_idle_clients)
Cycle(10, sweep_rooms)
Cycle(.25, process_client_commands)


#------------------------------------------------------------------------------
#       Create the Telnet Server
#------------------------------------------------------------------------------

server = TelnetServer(port=PORT, timeout=.05)
server.on_connect = on_connect
server.on_disconnect = on_disconnect


#------------------------------------------------------------------------------
#       Main Loop
#------------------------------------------------------------------------------

THE_LOG.add(">> Listening for connections on port %d" % PORT)

while gvar.SERVER_RUN == True:
    THE_SCHEDULER.tick()
    server.poll()

## All done
THE_LOG.add('?? Administrative shutdown')
