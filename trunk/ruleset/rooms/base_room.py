#------------------------------------------------------------------------------
#   File:       base_room.py
#   Purpose:    parent class for rooms
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared

class BaseRoom(object):

    def __init__(self, handle = '', name='', view='' ):

        self.handle = handle            # 'south_hall'
        self.name = name                # Southern Hallway
        self.view = view                # 'A large ..."
        self.zone = ''                  # 'The Landslid Crypt'
        self.players = {}               # Player Handle: Player Obj 
        self.devices = {}               # Device Obj : None
        self.items = {}                 # Item Obj : None
        self.mobs = {}                  # Mob Obj : None
        self.flags = {}                 # 'dark' : None
        self.exits = {}                 # 'north' : Room Obj


        print "Loaded", self.name


    def add_player(self, client, direction):
        print 'room.add_player', client.handle
        self.players[client.handle] = client
        self.tell_all_but(client, '%s enters the room %s.' % (
            client.name, direction))
        client.room = self
        print self.players

    def remove_player(self, client, direction):
        del self.players[client.handle]
        self.tell_all('%s leaves the room %s.' % (client.name, direction))

    def tell_all_but(self, client, text):
        """Send a message to every player in the room except the client."""
        for player in self.players.values():
            if player != client:
                player.send(text)

    def tell_all(self, text):
        """Send a message to every player in the room."""
        for player in self.players.values():
            player.send(text)        


    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def add_mob(self, mob, direction):
        pass

    def remove_mob(self, mob, direction):
        pass

    def add_exit(self, way, to_handle):
        """Add an exit to this room"""

        ## Due to the serial nature of loading from XML, quite often we'll
        ## receive exit directions to rooms that have do not exist yet.
        ## No problem, we'll just make a placeholder entry in the ROOMS
        ## dictionary.
                
        if to_handle not in shared.ROOMS:
            shared.ROOMS[to_handle] = None

        ## Map the direction to the room itself, not a handle.
        self.exits[way] = shared.ROOMS[to_handle]            
            

    def remove_exit(self, exit):
        pass

