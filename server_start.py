#!/usr/bin/env python
#------------------------------------------------------------------------------
#   File:       server_start.py
#   Purpose:    loads and loops the server
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from lib import shared
from driver.log import THE_LOG
from driver.tcp.listen import PORT

from driver.scheduler import THE_SCHEDULER
from driver.scheduler import Cycle
from driver.scheduler import Series

from driver.tcp.async import THE_PORT_AUTHORITY
from driver.monitor import test_connections
from driver.monitor import kill_idle_clients
from driver.monitor import purge_dead_clients
from driver.monitor import process_client_commands
#from lib.model.tables import check_tables
#from lib.model.tables import create_tables

from driver.loader.file_loader import load_module


THE_LOG.add("**************")
THE_LOG.add("server started")
THE_LOG.add("**************") 

#------------------------------------------------------------------------------
#       Load Game Data
#------------------------------------------------------------------------------

module = 'data/test_module'
load_module(module)


#------------------------------------------------------------------------------
#       Schedule Repeating Events
#------------------------------------------------------------------------------

Cycle(5, test_connections)
Cycle(5, kill_idle_clients)
Cycle(5, purge_dead_clients)


#------------------------------------------------------------------------------
#       Main Loop
#------------------------------------------------------------------------------

THE_LOG.add("Listening for connections on port %d" % PORT)

while shared.SERVER_RUN == True:
    THE_SCHEDULER.tick()
    THE_PORT_AUTHORITY.poll()
    process_client_commands()

## All done   
THE_LOG.add('Normal shutdown')

