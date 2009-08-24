# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/commands/wizard.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

#from mudlib import parsers
from driver.scheduler import THE_SCHEDULER
from mudlib.commands.speech import broadcast
from mudlib import shared
from mudlib import parsers
from driver.log import THE_LOG

#---------------------------------------------------------------------------Ban

def ban(client):
    pass


#-------------------------------------------------------------------------Grant

def grant(client):
    pass


#--------------------------------------------------------------------------Kick
@parsers.online_player
def kick(client, target):

    """Kick a miscreant player offline. They can come back."""

    client.warn('You kick %s offline.' % target.name)
    THE_LOG.add('?? %s kicked %s offline' % (client.name, target.name))
    target.deactivate()


#------------------------------------------------------------------------Revoke

def revoke(client):
    pass


#----------------------------------------------------------------------Shutdown

@parsers.blank
def shutdown(client):

    """Shutdown the server with a ten second warning to users."""

    def second_warning():
        broadcast("\n!! ^RServer shutdown in 5 seconds. Please log off.^w\n")

    def kill():
        shared.SERVER_RUN = False
   
    THE_LOG.add('?? %s requested server shutdown' % client.name)
    broadcast("\n!! ^RServer shutdown in 10 seconds.  Please log off.^w\n")
    THE_SCHEDULER.add(5, second_warning)
    THE_SCHEDULER.add(10, kill)


#------------------------------------------------------------------------Summon

def summon(client):
    pass


#----------------------------------------------------------------------Teleport

def teleport(client):
    pass


#------------------------------------------------------------------------Uptime

@parsers.blank
def uptime(client):

    """Report the uptime of the server in days/hours/minutes."""

    seconds = THE_SCHEDULER.age()

    MINUTES = 60
    HOURS = MINUTES * 60
    DAYS = HOURS * 24

    days = int(seconds / DAYS)
    seconds = seconds % DAYS
    hours = int(seconds / HOURS)
    seconds = seconds % HOURS
    minutes = int(seconds / MINUTES)

    if days == 1:
        s = '1 day, '
    elif days:
        s = '%d days, ' % days
    else:
        s = ''    

    if hours == 1:
        s += '1 hour, '
    else:
        s += '%d hours, ' % hours

    if minutes == 1:
        s += '1 min'
    else:
        s += '%d mins' % minutes

    client.inform(s)


#---------------------------------------------------------------------------Zap

def zap(client):
    pass


