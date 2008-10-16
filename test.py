#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------


from driver.loader.file_loader import item_iter


module = 'data/test_module'



for cfg in item_iter(module):

    #item = Item()
    #config_item(cfg, item)
    #register_item(item)

    print cfg
