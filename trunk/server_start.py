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


#---[ Age String ]-------------------------------------------------------------

# Convert a bunch of seconds into something readible
def age_string(age):
    days = int(age / 86400)
    age = age % 86400
    hours = int(age / 3600)
    age = age % 3600
    minutes = int(age / 60)
    seconds = int(age % 60)
    string = ''
    if days:
        string += "%d dy, " % days
    if hours:
        string += "%d hr, " % hours
    if minutes:
        string += "%d min, " % minutes
    string += "%d sec" % seconds
    
    return string


#--[ Still Kicking ]-----------------------------------------------------------

# Simple 10 second heartbeat to show the server isn't hung
def still_kicking(string):
    print string
    age = THE_SCHEDULER.age() + 5
    THE_SCHEDULER.add(5, still_kicking, "I am %s old. " % age_string(age))


#--[ Server Startup Code ]-----------------------------------------------------

#if not check_tables():
#    THE_LOG.add("Database tables not found -- creating tables.")
#    create_tables()


# Get still_kicking() ... kicking
#THE_SCHEDULER.add(1, still_kicking,"I live.")


# note the startup to the log
THE_LOG.add("**************")
THE_LOG.add("server started")
THE_LOG.add("**************") 


#--[ Load Zones ]--------------------------------------------------------------

## Load our mini testing zone
#load_rooms('The Landslid Crypt')

#print shared.ROOM_DICT

#--[ Main Loop ]---------------------------------------------------------------

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

