# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/inventory_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar

_MAX_STACK_SIZE = 99999999

def give_item(actor, item, qty=1):
    """
    Add qty of item to actor's inventory.
    """
    reduction = actor.profile.get('bag reduction', 1.0)
    actor.burden += (item.burden * reduction)
    count = actor.carried.get(item, 0)
    actor.carried[item] = count + qty

    if actor.is_player:
        if qty == 1:
            actor.send('^!%s^. added to inventory.\n' % item.name)
        else:
            actor.send('^!%s x %d^. added to inventory.\n'
                % (item.name, qty))


def give_item_by_uuid(actor, uuid, qty=1):
    """
    Add qty of item to actor's inventory by UUID.
    """
    item = gvar.ITEMS[uuid]
    give_item(actor, item, qty)


def take_item(actor, item, qty=1):
    """
    Remove qty of item from actor's inventory.
    """
    reduction = actor.profile.get('bag reduction', 1.0)
    actor.burden -= (item.burden * reduction)
    cout = actor.carried.get(item, 0)
    actor.carried[item] -= count + qty

    if actor.is_player:
        if qty == 1:
            actor.send('^!%s^. removed from inventory.\n' % item.name)
        else:
            actor.send('^!%s x %d^. removed from inventory.\n'
                % (item.name, qty))


def take_item_by_uuid(actor, uuid, qty=1):
    """
    Remove qty of item to actor's inventory by UUID.
    """
    item = gvar.ITEMS[uuid]
    take_item(actor, item, qty)
