#!/usr/bin/env python
##-----------------------------------------------------------------------------
##  File:       test.py
##-----------------------------------------------------------------------------

module = 'data/test_module'

from driver.loader.file_loader import item_cfg_iter
from lib.item import configured_item
from lib.item import register_item

for cfg in item_cfg_iter(module):
    register_item(configured_item(cfg))

from driver.loader.file_loader import room_cfg_iter
from lib.room import configured_room
from lib.room import register_room
for cfg in room_cfg_iter(module):
    register_room(configured_room(cfg))

from driver.loader.file_loader import sect_cfg_iter
from lib.sect import configured_sect
from lib.sect import register_sect
for cfg in sect_cfg_iter(module):
    register_sect(configured_sect(cfg))

from driver.loader.file_loader import race_cfg_iter
from lib.race import configured_race
from lib.race import register_race
for cfg in race_cfg_iter(module):
    register_race(configured_race(cfg))

from driver.loader.file_loader import gender_cfg_iter
from lib.gender import configured_gender
from lib.gender import register_gender
for cfg in gender_cfg_iter(module):
    register_gender(configured_gender(cfg))
