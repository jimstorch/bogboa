#------------------------------------------------------------------------------
#   File:       base_room.py
#   Purpose:    parent class for rooms
#   Author:     Jim Storch
#------------------------------------------------------------------------------



class BaseRoom(object):

    def __init__(self):

        self.handle = ''
        self.zone_handle = ''
        self.name = ''
        self.description = ''

        self.players = {}  
        self.item_list = []
        self.mob_list = []
        self.effect_list = []
        self.exits = []
        self.portals = []
        self.flags = {}

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

    def remove_mod(self, mob)
        pass

    def add_effect(self, effect):
        pass    
        
    def remove_effect(self, effect):
        pass

    def add_exit(self, exit):
        pass

    def remove_exit(self, exit):
        pass

    def add_portal(self, portal):
        pass

    def remove_portal(self, portal):
        pass


