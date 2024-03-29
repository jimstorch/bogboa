# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/faction.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib import gvar
from mudlib.sys import THE_LOG

#------------------------------------------------------------------------Gender

class Faction(object):

    def __init__(self):

        self.uuid = None
        self.name = None
        self.filename = None

        self.related = {}


#---------------------------------------------------------------Cascade Faction

def cascade_faction(faction, amount, body):

    """
    Process a faction event that modifys the faction and all related factions.
    """

    pass

#-------------------------------------------------------------------Adj Faction

def adj_faction(faction, amount, body):

    """
    Modify a single faction, ingnoring related ones.
    """

    pass


#-------------------------------------------------------------Configure Faction

def configure_faction(cfg):

    """
    Given a configuration dictionary, create a faction and configure it.
    Returns the configured faction.
    """

    faction = Faction()

    faction.filename = cfg.pop('filename')

    if 'name' in cfg:
        faction.name = cfg.pop('name')
    else:
        THE_LOG.add("!! Missing name in faction config.")
        sys.exit(1)

    if 'uuid' in cfg:
        faction.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("!! Missing UUID in config for faction '%s'." %
            faction.name)
        sys.exit(1)

    if 'desc' in cfg:
        faction.desc = cfg.pop('desc')
    else:
        faction.desc = None

#    if 'module' in cfg:
#        faction.module = cfg.pop('module')
#    else:
#        faction.module = None

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("!! Unrecognized key(s) in config for faction"
            " '%s': %s" % ( faction.name, cfg.keys()) )

    return faction


#--------------------------------------------------------------Register Faction

def register_faction(faction):

    """
    Given a configured faction, register it with the shared FACTION dictionary.
    """

    if faction.uuid in gvar.FACTIONS:
        THE_LOG.add("!! Duplicate UUID (%s) found while registering "
            "faction '%s' from module '%s'."  %  (
            faction.uuid, faction.name, faction.module) )
        sys.exit(1)
    else:
        gvar.FACTIONS[faction.uuid] = faction
