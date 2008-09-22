#------------------------------------------------------------------------------
#   File:       lib/scripting/parse_room.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from lib.scripting.from_yaml import parse_script
from lib.things.room import Room
from driver.log import THE_LOG


def parse_room(script):

    room = Room()
    cfg, error = test_script(script)

    ## If there was an error converting the script, log it and exit
    if cfg == None:
        THE_LOG.add('[parse_room]: %s' % error)
        sys.exit(1)




