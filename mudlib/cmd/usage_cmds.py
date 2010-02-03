# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/cmd/usage_cmds.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib.sys import BogCmdError
from mudlib.lang import parsers
from mudlib.lang import create_keyset
from mudlib.lang import match_carried
from mudlib.lang import match_worn
from mudlib import action
from mudlib.actor import WEAR_SLOTS


def too_many_matches(player, matches):
    """
    Complain that we matched too many items.
    """
    player.send('^yDid you mean ^w')
    names = [ name for match.name in matches[:-1] ]
    player.send(', '.join(names))
    player.send(' or %s?\n' % matches[-1].name)


@parsers.arg_keyset
def wear(player, keyset):
    """
    Examine an item in inventory.
    """
    matches = match_carried(player.avatar, keyset)
    if len(matches) == 0:
        player.send('^yItem not found.^w\n')
    elif len(matches) > 1:
        too_many_matches(player, matches)
    else:
        item = matches[0]
        if item.slot in WEAR_SLOTS:
            action.wear_item_from_carried(player.avatar, item)
        else:
            player.send('^Y%s^y cannot be worn.^w\n' % item.name.title())


def remove(player):
    raise BogCmdError('Not implemented')

def take(player):
    raise BogCmdError('Not implemented')

def drop(player):
    raise BogCmdError('Not implemented')
