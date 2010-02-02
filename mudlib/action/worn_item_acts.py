# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/action/worn_item_acts.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Actions related to worn or held items.
"""

from mudlib import gvar
from mudlib.actor import WEAR_SLOTS
from mudlib.actions.inventory_acts import give_item
from mudlib.actions.inventory_acts import take_item




#------------------------------------------------------From Inventory to Outfit

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


#----------------------------------------------------From Unspecified to Outfit

def equip_item_by_uuid(actor, uuid)
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
    assert slot in _WEAR_SLOTS
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
    ## invoke item's on_equipt script
    item.on_equip(actor)


#------------------------------------------------------From Outfit to Inventory

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
            actor.send('^!%s^. removed from %.\n' % (item.name, slot))
        ## invoke item's on_remove script
        item.on_remove(actor)
        give_item(actor, item)
    actor.worn[slot] = None
