#------------------------------------------------------------------------------
#   File:       read_xml.py
#   Purpose:    load game data from xml files
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import glob
from xml.etree import cElementTree as et

from ruleset import shared
from ruleset.rooms.base_room import BaseRoom


def load_rooms(zone = 'default'):
    """Load all the rooms in the given zone."""
           
    file_list = glob.glob('data/zones/%s/*.xml' % zone)
    for filename in file_list:
        room = BaseRoom()
        tree = et.parse(open(filename,'rU'))
        for elem in tree.getiterator('room'):
            pass        

