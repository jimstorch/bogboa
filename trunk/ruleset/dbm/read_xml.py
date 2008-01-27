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
            view = room.find('view').text    

            new_room = BaseRoom(handle, name, view)

            for exit in room.getiterator('exit'):
                way = exit.find('way').text
                to = exit.find('to').text
                new_room.add_exit(way, to)

            shared.ROOMS[handle] = new_room
        

            
