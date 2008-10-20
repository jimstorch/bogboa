##-----------------------------------------------------------------------------
##  File:       lib/item/item_loader.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.item.item import Item
from lib.shared import ITEM

#-----------------------------------------------------------------Register Item

def register_item(item):

    """
    Given a configured item, register it with the shared ITEM dictionary.
    """

    if item.uuid in ITEM:
        print ( "ERROR! Duplicate UUID (%s) found while registering item"
            " '%s'."  % (item.uuid, item.name) )
        sys.exit(1)
    else:
        ITEM[item.uuid] = item


#----------------------------------------------------------------Configure Item

def configured_item(cfg):

    """
    Given a configuration dictionary, create an item and configure it.
    Returns the configured item.
    """

    item = Item()

    if 'name' in cfg:
        item.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in item config."
        sys.exit(1)

    if 'uuid' in cfg:
        item.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for item '%s'." % item.name
        sys.exit(1)

    if 'desc' in cfg:
        item.desc = cfg.pop('desc')
    else:
        item.desc = None

    if 'sell' in cfg:
        item.sell = cfg.pop('sell')
    else:
        item.sell = None        

    if 'buy' in cfg:
         item.buy = cfg.pop('buy')     
    else:
        item.buy = None

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        print ( "WARNING! Unrecognized key(s) in config for item '%s': %s" 
            % ( item.name, cfg.keys()) )

    return item    
