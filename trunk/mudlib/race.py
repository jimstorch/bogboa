# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/race.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from mudlib.shared import RACES
from driver.log import THE_LOG

#--------------------------------------------------------------------------Race

class Race(object):

    def __init__(self):
    
#        self.uuid = None
        self.name = None
        self.module = None

        self.stat = {}
        self.skill_adj = {}
        self.ability = {}
        

#----------------------------------------------------------------Configure race

def configure_race(cfg):

    """
    Given a configuration dictionary, create a race and configure it.
    Returns the configured race.
    """

    race = Race()

    if 'name' in cfg:
        race.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in race config."
        sys.exit(1)

#    if 'uuid' in cfg:
#        race.uuid = cfg.pop('uuid')
#    else:
#        print "ERROR! Missing UUID in config for race '%s'." % race.name
#        sys.exit(1)

    if 'desc' in cfg:
        race.desc = cfg.pop('desc')
    else:
        race.desc = None

    if 'module' in cfg:
        race.module = cfg.pop('module')
    else:
        race.module = None


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add( "WARNING! Unrecognized key(s) in config for race '%s': %s" 
            % ( race.name, cfg.keys()) ) 

    return race


#-----------------------------------------------------------------Register race

def register_race(race):

    """
    Given a configured race, register it with the shared race dictionary.
    """

    if race.name in RACES:
        print ( "ERROR! Duplicate name (%s) found while registering "
            "race '%s' from module '%s'."  %  (
            race.uuid, race.name, race.module) )
        sys.exit(1)
    else:
        RACES[race.name] = race    