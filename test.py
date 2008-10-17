#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------


from driver.loader.file_loader import item_cfg_iter
from lib.item.item_loader import configured_item

module = 'data/test_module'



for cfg in item_cfg_iter(module):

    #item = Item()
    #config_item(cfg, item)
    #register_item(item)

    #print cfg

    item = configured_item(cfg)
    print item
