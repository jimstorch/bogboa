#------------------------------------------------------------------------------
#   File:       base_room.py
#   Purpose:    parent class for rooms
#   Author:     Jim Storch
#------------------------------------------------------------------------------



class BaseRoom(object):

    def __init__(self, handle = '', name='', view='' ):

        self.handle = handle            # 'south_hall'
        self.name = name                # Southern Hallway
        self.view = view                # 'A large ..."
        self.zone = ''                  # 'The Landslid Crypt'

        self.exits = {}                 # 'north' : Room Obj
        self.devices = {}               # Device Obj : None
        self.players = {}               # Player Obj : None  
        self.items = {}                 # Item Obj : None
        self.mobs = {}                  # Mob Obj : None
        self.flags = {}                 # 'dark' : None


    def add_player(self, player):
        pass

    def remove_player(self, player):
        pass

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def add_mob(self, mob):
        pass

    def remove_mob(self, mob):
        pass

    def add_exit(self, exit):
        pass

    def remove_exit(self, exit):
        pass

