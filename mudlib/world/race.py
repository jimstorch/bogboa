# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/race.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib import gvar
from mudlib.sys import THE_LOG


class Race(object):

    def __init__(self):

        self.name = None
        self.filename = None
        self.stats = {}
        self.abilities = set()

    def get_stats(self):
        """
        Return a copy of the race stats.
        """
        return self.stats[:]


def configure_race(cfg):
    """
    Given a configuration dictionary, create a race and configure it.
    Returns the configured race.
    """
    race = Race()

    race.filename = cfg.pop('filename')

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

    if 'module' in cfg:
        race.module = cfg.pop('module')
    else:
        race.module = None

    if 'stats' in cfg:
        race.stats = cfg.pop('stats')

    ## Used by Help
    if 'text' in cfg:
        cfg.pop('text')

    ## Used by Help
    if 'keywords' in cfg:
        cfg.pop('keywords')

    ## For future use
    if 'version' in cfg:
        cfg.pop('version')

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add( "!! Unrecognized key(s) in config for race '%s': %s"
            % ( race.name, cfg.keys()) )

    return race


def register_race(race):
    """
    Given a configured race, register it with the shared race dictionary.
    """
    if race.name in gvar.RACES:
        print ( "!! Duplicate name (%s) found while registering "
            "race '%s' from module '%s'."  %  (
            race.uuid, race.name, race.module) )
        sys.exit(1)
    else:
        gvar.RACES[race.name] = race
