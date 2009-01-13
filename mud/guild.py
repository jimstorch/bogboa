# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mud/guild.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from mud.shared import GUILD
from driver.log import THE_LOG

#-------------------------------------------------------------------------Guild

class Guild(object):

    def __init__(self):
   
        self.uuid = None
        self.name = None
        self.module = None

        self.skill_mod = {}     # Dictionary of Skill modifiers
        self.ability = {}       # List of guild abilities by name

    #-------------------------------------------------------------Get Skill Mod        

    def get_skill_mod(self, skill_name):
        """
        Return the guild skill modifier or zero if skill not found.
        """
        return self.skill_mod(skill_name, 0.0)

    #---------------------------------------------------------------Has Ability

    def has_ability(self, ability_name):
        return ability_name in self.ability


#---------------------------------------------------------------Configure Guild

def configure_guild(cfg):

    """
    Given a configuration dictionary, create a guild and configure it.
    Returns the configured guild.
    """

    guild = Guild()

    if 'name' in cfg:
        guild.name = cfg.pop('name')
    else:
        THE_LOG.add("ERROR! Missing name in guild config.")
        sys.exit(1)

    if 'uuid' in cfg:
        guild.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("ERROR! Missing UUID in config for guild '%s'." 
            % guild.name)
        sys.exit(1)

    if 'desc' in cfg:
        guild.desc = cfg.pop('desc')
    else:
        guild.desc = None

    if 'module' in cfg:
        guild.module = cfg.pop('module')
    else:
        guild.module = None


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("WARNING! Unrecognized key(s) in config for guild '%s': %s" 
            % ( guild.name, cfg.keys()) ) 

    return guild    


#----------------------------------------------------------------Register Guild

def register_guild(guild):

    """
    Given a configured guild, register it with the shared guild dictionary.
    """

    if guild.uuid in GUILD:
        THE_LOG.add("ERROR! Duplicate UUID (%s) found while registering "
            "guild '%s' from module '%s'."  %  (
            guild.uuid, guild.name, guild.module) )
        sys.exit(1)
    else:
        GUILD[guild.uuid] = guild    
