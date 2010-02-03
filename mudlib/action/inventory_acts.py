# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/inventory_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

from mudlib import gvar
from mudlib.actor import WEAR_SLOTS


_MAX_STACK_SIZE = 99999999

#--[ Carried Items ]-----------------------------------------------------------

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
    #reduction = actor.profile.get('bag reduction', 1.0)
    #actor.burden -= (item.burden * reduction)
    count = actor.carried[item]
    if count == qty:
        del actor.carried[item]
    else:
        actor.carried[item] = count - qty

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


#--[ From Carried to Worn ]----------------------------------------------------

def wear_item_from_carried(actor, item):
    """
    Remove the given item from actor's inventory and equip it.
    """
    take_item(actor, item)
    equip_item(actor, item)


def wear_item_from_carried_by_uuid(actor, item):
    """
    Remove the given item from actor's carried inventory and equip it.
    """
    item = gvar.ITEMS[uuid]
    wear_item_from_carried(actor, item)


#--[ From Unspecified to Worn ]------------------------------------------------

def equip_item_by_uuid(actor, uuid):
    """
    Given an item UUID, equip the given item.
    """
    item = gvar.ITEMS[uuid]
    equip_item(actor, item)


def equip_item(actor, item):
    """
    Equip given item in the actor's appropriate slot.
    """
    slot = item.slot
    ## TODO remove this typo check
    assert slot in WEAR_SLOTS
    ## Some special rules of juggling...
    if slot == 'both hands':
        stow_item_by_slot(actor, 'both hands')
        stow_item_by_slot(actor, 'main hand')
        stow_item_by_slot(actor, 'off hand')

    elif slot == 'main hand':
        stow_item_by_slot(actor, 'both hands')
        stow_item_by_slot(actor, 'main hand')

    elif slot == 'off hand':
        stow_item_by_slot(actor, 'both hands')
        stow_item_by_slot(actor, 'off hand')

    else:
        stow_item_by_slot(actor, slot)

    actor.worn[slot] = item
    actor.send('^!%s^. added to %s.\n' % (item.name, slot))
    ## invoke item's on_equipt script
    item.on_equip(actor)


#---[ From Worn to Carried ]---------------------------------------------------

def stow_item_by_uuid(actor, uuid):
    """
    Given an item UUID, transfer the item to the actor's inventory.
    """
    item = gvar.ITEMS[uuid]
    stow_item(actor, item)


def stow_item(actor, item):
    """
    Transfer the given item to the actor's inventory.
    """
    slot = item.slot
    stow_item_by_slot(actor, slot)


def stow_item_by_slot(actor, slot):
    """
    If slot contains an item, transfer it to the actor's inventory.
    """
    item = actor.worn.get(slot, None)
    if item:
        if actor.is_player:
            actor.send('^!%s^. removed from %s.\n' % (item.name, slot))
        ## invoke item's on_remove script
        item.on_remove(actor)
        give_item(actor, item)
    actor.worn[slot] = None
