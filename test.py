#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------


from driver.loader.file_loader import item_cfg_iter
from driver.loader.file_loader import room_cfg_iter
from lib.item.item_creator import configured_item
from lib.item.item_creator import register_item

module = 'data/test_module'



#for cfg in item_cfg_iter(module):
#    item = configured_item(cfg)
#    register_item(item)
#    print item


for cfg in room_cfg_iter(module):
    print cfg
