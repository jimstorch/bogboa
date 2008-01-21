#------------------------------------------------------------------------------
#   File:       player.py
#   Purpose:    general gameplay class
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset import shared
from ruleset.modes.base_mode import BaseMode
from ruleset.parsers import split_verb

GREETING = """
---[ Test Play Mode ]----------------------------------------------------------
"""    


#--[ Play Mode Class ]---------------------------------------------------------

class Player(BaseMode):

    def __init__(self, conn):
        self.active = True  
        self.conn = conn
        self.handle = ''
        self.name = ''
        self.gender = ''
        self.race = ''
        self.role = ''
        self.target_handle = ''
        self.ability_list = []
        self.last_tell = ''

        self.grant_ability('tell')
        self.grant_ability('t')
        self.grant_ability('whisper')
        self.grant_ability('w')
        self.grant_ability('reply')
        self.grant_ability('r')
        self.grant_ability('shout')
        self.grant_ability('quit')

        self.send(GREETING)
        self.prompt()

 
    #---[ Process Command ]----------------------------------------------------

    def process_command(self):
        """Get a line of player input and react to it."""

        cmd = self.get_cmd()
        verb, words = split_verb(cmd)
    
        if not verb:
            self.prompt()
            return
    
        if self.has_ability(verb):
            
            parser, function = shared.ABILITY_DICT[verb]

            if parser:
                args = parser(words)
                print args
                function(self, *args)

            else:
                function(self)
  
            self.prompt()

        else:
            self.send("^yUnrecognized verb '%s'." % verb)
            self.prompt()


    #---[ Has Ability ]--------------------------------------------------------

    def has_ability(self, ability_handle):
        """Test whether this character has access to a given ability name."""

        return ability_handle in self.ability_list


    #---[ Grant Ability ]------------------------------------------------------
    
    def grant_ability(self, ability_handle):
        """Grant the character permission to use the given ability."""
        if not ability_handle in self.ability_list:
            self.ability_list.append(ability_handle)


    #---[ Revoke Ability ]-----------------------------------------------------        

    def revoke_ability(self, ability_handle):
        """Revoke permission for the character to use the given ability."""
        if ability_handle in self.ability_list:
            self.ability_list.remove(ability_handle)
    

    #---[ Del ]----------------------------------------------------------------

    def __del__(self):
        """For testing garbage collection."""
#        print "Player destructor called"
        pass
