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


    #---[ Add Player ]---------------------------------------------------------

    def add_player(self, client, direction):
        
        """Adds player to the room population."""
        
        self.players[client.handle] = client
        self.tell_all_but(client, '%s appears%s.' % (
            client.name, direction))
        client.room = self
        client.send('^cArrived at %s.' % self.name)

    #---[ Remove Player ]------------------------------------------------------

    def remove_player(self, client, direction):
    
        """Remove player from the room population."""
    
        if client.handle in self.players:
            del self.players[client.handle]
            self.tell_all('%s departs%s.' % (client.name, direction))


    #---[ Tell All But ]-------------------------------------------------------

    def tell_all_but(self, client, text):
    
        """Send a message to every player in the room except the client."""

        for player in self.players.values():
            if player != client:
                player.send(text)


    #---[ Tell All ]-----------------------------------------------------------

    def tell_all(self, text):

        """Send a message to every player in the room."""

        for player in self.players.values():
            player.send(text)        


    #---[ Add Exit ]-----------------------------------------------------------

    def add_exit(self, way, to_handle):

        """Add or change an exit from this room"""

        self.exits[way] = to_handle  


    #---[ Remove Exit ]--------------------------------------------------------

    def remove_exit(self, exit):
        pass


    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def add_mob(self, mob, direction):
        pass

    def remove_mob(self, mob, direction):
        pass

          
            



