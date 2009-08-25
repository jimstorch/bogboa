#!/usr/bin/env python
#------------------------------------------------------------------------------
#   server_start.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import shared
from driver.log import THE_LOG
from driver.config import PORT

from driver.scheduler import THE_SCHEDULER
from driver.scheduler import Cycle
from driver.scheduler import Series

from driver.tcp.async import THE_PORT_AUTHORITY
from driver.monitor import test_connections
from driver.monitor import kill_idle_clients
from driver.monitor import purge_dead_clients
from driver.monitor import process_client_commands
from driver.monitor import sweep_rooms

from driver.loader.file_loader import load_module
from driver.dbms.tables import check_database

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

module = 'data/base'
load_module(module)

module = 'data/testville'
load_module(module)


#------------------------------------------------------------------------------
#       Schedule Repeating Events
#------------------------------------------------------------------------------

Cycle(2, test_connections)
Cycle(2, kill_idle_clients)
Cycle(2, purge_dead_clients)
Cycle(10, sweep_rooms)


#------------------------------------------------------------------------------
#       Main Loop
#------------------------------------------------------------------------------

THE_LOG.add(">> Listening for connections on port %d" % PORT)

while shared.SERVER_RUN == True:
    THE_SCHEDULER.tick()
    THE_PORT_AUTHORITY.poll()
    process_client_commands()

## All done   
THE_LOG.add('?? Administrative shutdown')

