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
from mudlib.actor import DISPLAY_SLOTS
from mudlib.sys import BogCmdError
from mudlib.lang import parsers
from mudlib.lang import match_carried
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
    player.send_wrapped('^c^!%s^., %s.\n^w' % (room.name, calendar.time_msg()))
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


@parsers.blank
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

@parsers.blank
def inventory(player):
    """
    Display the avatar's worn and carried items.
    """
    worn(player)
    carried(player)


@parsers.blank
def carried(player):
    """
    Display the avatar's carried items.
    """
    items = player.avatar.carried

    if not items:
        player.send('Your inventory is empty.\n')

    else:
        player.send('--^!Item^.------------------------------------'
            '^!Quantity^.----^!Burden^.----^!Rough Value^.--\n')
        for item in items:
            qty = items[item]

            player.send('  ^!%-38s^.' % item.name)
            player.send('%10d' % qty)
            player.send('%10.2f' % (qty * item.burden))
            player.send('%15.2f' % (qty * item.value))
            player.send('\n')


@parsers.arg_keyset
def examine(player, keyset):
    """
    Examine an item in inventory.
    """
    matches = match_carried(player.avatar, keyset)
    if matches:
        for item in matches:
            player.send('^!%s^.: %s\n' % (item.name, item.text))
    else:
        player.send('^yItem not found.^w\n')


@parsers.blank
def worn(player):
    """
    Display the avatar's worn items.
    """
    worn = player.avatar.worn
    player.send('--^!Slot^.--------^!Item^.-----------------------------'
        '------^!Burden^.----^!Rough Value^.--\n')

    ## Held items
    both = worn.get('both hands', None)
    main = worn.get('main hand', None)
    off = worn.get('off hand', None)
    if both:
        player.send('  both hands  ^!%-30s^.\n' % both.name)
    else:
        if main:
            player.send('  main hand   ^!%-30s^.\n' % main.name)
        if off:
            player.send('  off hand    ^!%-30s^..\n'% off.name)

    ## Armor slots
    for slot in DISPLAY_SLOTS:
        player.send('  %-12s' % slot)
        item = worn.get(slot, None)
        if item:
            player.send('^!%-30s^.' % item.name)
#        player.send('%10d' % qty)
#        player.send('%10.2f' % (qty * item.burden))
#        player.send('%15.2f' % (qty * item.value))
            player.send('\n')

        else:
            player.send('--empty--\n')
