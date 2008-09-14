#------------------------------------------------------------------------------
#   File:       lib/player.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------


class Player(object):

    def __init__(self):

        ## Identity
        self.uuid = None
        self.handle = None
        self.race = None
        self.gender = None
        self.archetype = None
        self.level = None
        self.skill_map = {}

        self.room = None
        
        self.friendly_target = None
        self.hostile_target = None        


    
