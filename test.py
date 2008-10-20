#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------

module = 'data/test_module'

from driver.loader.file_loader import *
from lib.item import configured_item, register_item
from lib.room import configured_room, register_room
from lib.sect import configured_sect, register_sect
from lib.race import configured_race, register_race
from lib.gender import configured_gender, register_gender

for cfg in item_cfg_iter(module):
    item = configured_item(cfg)
    register_item(item)

for cfg in room_cfg_iter(module):
    room = configured_room(cfg)
    register_room(room)

for cfg in sect_cfg_iter(module):
    sect = configured_sect(cfg)
    register_sect(sect)

for cfg in race_cfg_iter(module):
    race = configured_race(cfg)
    register_race(race)

for cfg in gender_cfg_iter(module):
    print cfg
    gender = configured_gender(cfg)
    register_gender(gender)
