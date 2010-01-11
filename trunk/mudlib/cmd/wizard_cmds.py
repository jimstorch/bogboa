# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmd/wizard_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib import action
from mudlib.sys import THE_LOG
from mudlib.sys.scheduler import THE_SCHEDULER
from mudlib.usr import parsers


def ban(player):
    raise BogCmdError('Not implemented')


def grant(player):
    raise BogCmdError('Not implemented')


@parsers.online_player
def kick(player, target):
    """
    Kick a miscreant player offline. They can come back.
    """
    player.send('^YYou kick %s offline.^w\n' % target.name)
    THE_LOG.add('?? %s kicked %s offline' % (player.avatar.get_name(),
        target.get_name()))
    target.client.deactivate()


def revoke(player):
    raise BogCmdError('Not implemented')



@parsers.blank
def shutdown(player):

    """Shutdown the server with a ten second warning to users."""

    def second_warning():
        action.broadcast(
            "\n!! ^RServer shutdown in 5 seconds. Please log off.^w\n")

    def kill():
        gvar.SERVER_RUN = False

    THE_LOG.add('?? %s requested server shutdown' % player.avatar.get_name())
    action.broadcast(
        "\n!! ^RServer shutdown in 10 seconds.  Please log off.^w\n")
    THE_SCHEDULER.add(5, second_warning)
    THE_SCHEDULER.add(10, kill)


def summon(player):
    raise BogCmdError('Not implemented')


def teleport(player):
    raise BogCmdError('Not implemented')


@parsers.blank
def uptime(player):
    """
    Report the uptime of the server in days/hours/minutes.
    """
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
    player.send('^CServer has been running for %s.^w\n' % s)


def zap(player):
    raise BogCmdError('Not implemented')
