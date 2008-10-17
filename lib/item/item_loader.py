##-----------------------------------------------------------------------------
##  File:       lib/item/item_loader.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.item.item import Item


def register_item(item):
    pass


def configured_item(cfg):

    item = Item()

    if 'handle' in cfg:
        handle = cfg.pop('handle')
    else:
        print "ERROR! Missing handle in item config."
        sys.exit(1)

    if 'uuid' in cfg:
        item.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for item '%s'." % handle
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

    if cfg:
        print "WARNING! Unrecognized key(s) in config for item '%s':" % handle, 
        print cfg.keys()

    return item    
