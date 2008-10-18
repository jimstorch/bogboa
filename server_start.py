#!/usr/bin/env python
#------------------------------------------------------------------------------
#   File:       server_start.py
#   Purpose:    loads and loops the server
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from lib import shared
from driver.log import THE_LOG
from driver.tcp.listen import PORT

from driver.clock.scheduler import THE_SCHEDULER
from driver.tcp.async import THE_PORT_AUTHORITY
from driver.control import test_connections
from driver.control import kill_idle_clients
from driver.control import purge_dead_clients
from driver.control import process_client_commands
#from lib.model.tables import check_tables
#from lib.model.tables import create_tables


THE_LOG.add("**************")
THE_LOG.add("server started")
THE_LOG.add("**************") 

#------------------------------------------------------------------------------
#       Load Game Data
#------------------------------------------------------------------------------

module = 'data/test_module'

from driver.loader.file_loader import room_cfg_iter
from lib.room.room_creator import configured_room
from lib.room.room_creator import register_room

for cfg in room_cfg_iter(module):
    room = configured_room(cfg)
    register_room(room)

from driver.loader.file_loader import sect_cfg_iter
from lib.sect.sect_creator import configured_sect
from lib.sect.sect_creator import register_sect

for cfg in sect_cfg_iter(module):
    sect = configured_sect(cfg)
    register_sect(sect)

#------------------------------------------------------------------------------
#       Main Loop
#------------------------------------------------------------------------------

THE_LOG.add("Listening for connections on port %d" % PORT)

# Our process loop
while shared.SERVER_RUN == True:
    THE_SCHEDULER.tick()
    THE_PORT_AUTHORITY.poll()
    test_connections()
    kill_idle_clients()
    purge_dead_clients()
    process_client_commands()

# All done   
THE_LOG.add('Normal shutdown')

