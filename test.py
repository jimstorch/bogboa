#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------

module = 'data/test_module'

#from driver.loader.file_loader import item_cfg_iter
#from lib.item.item_creator import configured_item
#from lib.item.item_creator import register_item

#from driver.loader.file_loader import room_cfg_iter
#from lib.room.room_creator import configured_room
#from lib.room.room_creator import register_room

#from driver.loader.file_loader import sect_cfg_iter
#from lib.sect.sect_creator import configured_sect
#from lib.sect.sect_creator import register_sect

#from driver.loader.file_loader import race_cfg_iter
#from lib.race.race_creator import configured_race
#from lib.race.race_creator import register_race

from driver.loader.file_loader import gender_cfg_iter
from lib.gender.gender_creator import configured_gender
from lib.gender.gender_creator import register_gender


#for cfg in item_cfg_iter(module):
#    item = configured_item(cfg)
#    register_item(item)
#    print item


#for cfg in room_cfg_iter(module):
#    print cfg
#    room = configured_room(cfg)
#    register_room(room)

#for cfg in sect_cfg_iter(module):
#    print cfg
#    sect = configured_sect(cfg)
#    register_sect(sect)

for cfg in gender_cfg_iter(module):
    #print cfg
    gender = configured_gender(cfg)
    register_gender(gender)
