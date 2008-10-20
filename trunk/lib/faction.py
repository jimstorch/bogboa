##-----------------------------------------------------------------------------
##  File:       lib/faction.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.shared import FACTION

#------------------------------------------------------------------------Gender

class Faction(object):

    def __init__(self):
    
        uuid = None
        name = None
        module = None

        associated = {}



#-------------------------------------------------------------------Adj Faction

def adj_faction(faction, amount, player):
    pass


#--------------------------------------------------------------Register Faction

def register_faction(faction):

    """
    Given a configured faction, register it with the shared FACTION dictionary.
    """

    if faction.uuid in FACTION:
        print ( "ERROR! Duplicate UUID (%s) found while registering "
            "faction '%s' from module '%s'."  %  (
            faction.uuid, faction.name, faction.module) )
        sys.exit(1)
    else:
        FACTION[faction.uuid] = faction


#------------------------------------------------------------Configured Faction

def configured_faction(cfg):

    """
    Given a configuration dictionary, create a faction and configure it.
    Returns the configured faction.
    """

    faction = Faction()

    if 'name' in cfg:
        faction.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in faction config."
        sys.exit(1)

    if 'uuid' in cfg:
        faction.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for faction '%s'." % faction.name
        sys.exit(1)

    if 'desc' in cfg:
        faction.desc = cfg.pop('desc')
    else:
        faction.desc = None

    if 'module' in cfg:
        faction.module = cfg.pop('module')
    else:
        faction.module = None



    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        print ( "WARNING! Unrecognized key(s) in config for faction '%s': %s" 
            % ( faction.name, cfg.keys()) ) 

    return faction

        
