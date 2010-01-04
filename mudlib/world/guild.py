# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/guild.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib import gvar
from mudlib.sys import THE_LOG


class Guild(object):

    def __init__(self):
        self.name = None
        self.filename = None
        self.skill_mods = {}    # Dictionary of Skill modifiers
        self.ability = {}       # List of guild abilities by name

    def get_skill_mod(self, skill_name):
        """
        Return the guild skill modifier or zero if skill not found.
        """
        return self.skill_mods(skill_name, 0.0)

    def has_ability(self, ability_name):
        return ability_name in self.ability


def configure_guild(cfg):
    """
    Given a configuration dictionary, create a guild and configure it.
    Returns the configured guild.
    """
    guild = Guild()

    guild.filename = cfg.pop('filename')

    if 'name' in cfg:
        guild.name = cfg.pop('name')
    else:
        THE_LOG.add("!! Missing name in guild config.")
        sys.exit(1)

#    if 'uuid' in cfg:
#        guild.uuid = cfg.pop('uuid')
#    else:
#        THE_LOG.add("ERROR! Missing UUID in config for guild '%s'."
#            % guild.name)
#        sys.exit(1)

    ## Used by Help
    if 'text' in cfg:
        cfg.pop('text')

    ## Used by Help
    if 'keywords' in cfg:
        cfg.pop('keywords')

    if 'module' in cfg:
        guild.module = cfg.pop('module')
    else:
        guild.module = None

    if 'skills' in cfg:
        guild.skill_mods = cfg.pop('skills')

    ## For future use
    if 'version' in cfg:
        cfg.pop('version')

    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("!! Unrecognized key(s) in config for guild '%s': %s"
            % ( guild.name, cfg.keys()) )

    return guild


def register_guild(guild):
    """
    Given a configured guild, register it with the shared guild dictionary.
    """
    if guild.name in gvar.GUILDS:
        THE_LOG.add("!! Duplicate name (%s) found while registering "
            "guild '%s' from module '%s'."  %  (
            guild.uuid, guild.name, guild.module) )
        sys.exit(1)
    else:
        gvar.GUILDS[guild.name] = guild
