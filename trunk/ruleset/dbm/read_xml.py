#------------------------------------------------------------------------------
#   File:       read_xml.py
#   Purpose:    load game data from xml files
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import glob
from xml.etree import cElementTree as et

from ruleset import shared
from ruleset.rooms.base_room import BaseRoom


#---[ Load Rooms ]-------------------------------------------------------------

def load_rooms(zone = 'default'):
    """Load all the rooms in the given zone."""
 
    print "Load Rooms called"          
    file_list = glob.glob('data/zones/%s/rooms/*.xml' % zone)
#    print file_list
    for filename in file_list:
        print filename
        tree = et.parse(open(filename,'rU'))
        for room in tree.getiterator('room'):

            handle = room.find('handle').text.strip()
            name = room.find('name').text.strip()
            view = room.find('view').text.strip()       


            new_room = BaseRoom(handle, name, view)

            for exit in room.getiterator('exit'):
                print exit.find('way').text
                print exit.find('to').text
