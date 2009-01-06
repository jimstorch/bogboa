# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       lib/sect.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from lib.shared import SECT
from driver.log import THE_LOG

#--------------------------------------------------------------------------Sect

class Sect(object):

    def __init__(self):
   
        self.uuid = None
        self.name = None
        self.module = None

        self.skill_mod = {}     # Dictionary of Skill modifiers
        self.ability = {}       # List of sect abilities by name

    #-------------------------------------------------------------Get Skill Mod        

    def get_skill_mod(self, skill_name):
        """
        Return the sect skill modifier or zero if skill not found.
        """
        return self.skill_mod(skill_name, 0.0)

    #---------------------------------------------------------------Has Ability

    def has_ability(self, ability_name):
        return ability_name in self.ability


#----------------------------------------------------------------Configure Sect

def configure_sect(cfg):

    """
    Given a configuration dictionary, create a sect and configure it.
    Returns the configured sect.
    """

    sect = Sect()

    if 'name' in cfg:
        sect.name = cfg.pop('name')
    else:
        THE_LOG.add("ERROR! Missing name in sect config.")
        sys.exit(1)

    if 'uuid' in cfg:
        sect.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("ERROR! Missing UUID in config for sect '%s'." % sect.name)
        sys.exit(1)

    if 'desc' in cfg:
        sect.desc = cfg.pop('desc')
    else:
        sect.desc = None

    if 'module' in cfg:
        sect.module = cfg.pop('module')
    else:
        sect.module = None


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("WARNING! Unrecognized key(s) in config for sect '%s': %s" 
            % ( sect.name, cfg.keys()) ) 

    return sect    


#-----------------------------------------------------------------Register Sect

def register_sect(sect):

    """
    Given a configured sect, register it with the shared sect dictionary.
    """

    if sect.uuid in SECT:
        THE_LOG.add("ERROR! Duplicate UUID (%s) found while registering "
            "sect '%s' from module '%s'."  %  (
            sect.uuid, sect.name, sect.module) )
        sys.exit(1)
    else:
        SECT[sect.uuid] = sect    
