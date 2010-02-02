# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/stat_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Character stat related actions.
"""

_STAT_LIST = [ 'brawn', 'vigor', 'precision', 'knowledge', 'faith', 'cunning']


def adjust_stat(actor, stat, amount):
    """
    Modify the actor's current stat by amount, positive or negative.
    """
    ## TODO: temporary typo check
    assert stat in _STAT_LIST
    current = actor.stats.get(stat, 0)
    actor.stats[stat] = current + amount

    if actor.is_player:
        if amount > 0:
            actor.send('%s increased by %d.\n' % (stat.title(), amount))
        else:
            actor.send('%s reduced by %d.\n' % (stat.title(), amount))
