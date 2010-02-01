# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmds/info_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Information related Player commands.
"""

from mudlib import gvar
from mudlib.sys.error import BogCmdError
from mudlib.usr import parsers
from mudlib.world import calendar


@parsers.blank
def commands(player):
    """
    List the player's granted command set.
    """
    clist = list(player.commands)
    clist.sort()
    cmds = ', '.join(clist)
    player.send_wrapped('Your current commands are: ^W%s^w\n' % cmds)


@parsers.blank
def topics(player):
    """
    List the player's granted command set.
    """
    tlist = list(gvar.HELPS.keys())
    tlist.sort()
    topics = ', '.join(tlist)
    player.send_wrapped('Available help topics are: ^W%s^w\n' % topics)


@parsers.blank
def stats(player):
    """
    List the player's stats.
    """
    stats = player.avatar.stats.keys()
    stats.sort()
    s = ''
    for stat in stats:
        s += '%s=%s ' % (stat.upper(), player.avatar.stats[stat])
    player.send_wrapped('Your current stats: ^W%s^w\n' % s)


@parsers.blank
def look(player):
    """
    Look at the current room.
    """
    room = player.avatar.get_room_obj()
    player.send_wrapped('^c^!%s^1, %s.\n^w' % (room.name, calendar.time_msg()))
    player.send_wrapped(room.text)


@parsers.none_or_one
def help(player, arg):

    """Display the selected help text."""

    if arg != None:
        topic = arg.lower()
        if topic in gvar.HELPS:
            player.send_wrapped(gvar.HELPS[topic].text)
        else:
            raise BogCmdError('Help topic not found')

    else:
        player.send_wrapped(gvar.HELPS['help'].text)


def score(player):
    """
    Fix Me
    """
    raise BogCmdError('Not implemented')


@parsers.blank
def time(player):
    """
    Tell the player the current game time.
    """
    player.send_wrapped('^CThe time is %s.^w\n' % calendar.time_msg())
    print player.avatar.profile



@parsers.blank
def date(player):
    """
    Tell the player the current game date.
    """
    player.send_wrapped('^CThe date is %s.^w\n' % calendar.date_msg())



def inventory(player):
    """
    Display the avatar's inventory.
    """
    items = player.avatar.bag.items

    if not items:
        player.send('Your inventory is empty.\n')

    else:
        player.send('--^!Item^.------------------------------------'
            '^!Quantity^.----^!Burden^.----^!Rough Value^.--\n')
        for item in items:
            qty = items[item]

            player.send('  ^Y%-38s^w' % item.name)
            player.send('%10d' % qty)
            player.send('%10.2f' % (qty * item.burden))
            player.send('%15.2f' % (qty * item.value))
            player.send('\n')


