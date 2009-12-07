# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/loader/file_loader.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
File Loader

Load configuration from YAML files in a module directory.
"""

import os
import sys
import glob

from mudlib import shared
from driver.log import THE_LOG
from driver.error import BogYAMLError
from driver.loader.from_yaml import parse_markup


##  Order of Precedence:
##  Races, Guilds, Items, Spawns, Rooms, Helps 

#-------------------------------------------------------------------Load Module

def load_module(module):

    THE_LOG.add(">> Loading Module: '%s'"  % module)

    ## Load Races
    from mudlib.race import configure_race, register_race
    for cfg in race_directory(module):
        race = configure_race(cfg)
        register_race(race)

    ## Load Guilds
    from mudlib.guild import configure_guild, register_guild
    for cfg in guild_directory(module):
        guild = configure_guild(cfg)
        register_guild(guild)

    ## Load Items    
    from mudlib.item import configure_item, register_item
    for cfg in item_directory(module):
        item = configure_item(cfg)
        register_item(item)

    ## Load Spawns    
#    from mudlib.item import configure_spawn, register_spawn
#    for cfg in spawn_directory(module):
#        spawn = configure_spawn(cfg)
#        register_spawn(spawn)

    ## Load Rooms    
    from mudlib.room import configure_room, register_room
    for cfg in room_directory(module):
        room = configure_room(cfg)
        register_room(room)

    ## Load Help
    from mudlib.help import configure_help, register_help
    for cfg in help_directory(module):
        help = configure_help(cfg)
        register_help(help)

#----------------------------------------------------------------Race Directory

def race_directory(module_dir):

    """Generator function to read module's Race directory."""

    THE_LOG.add(".. Loading Races")
    mask = os.path.join(module_dir, 'race/*.yml')
    filenames = glob.glob(mask)
    for cfg in parse_directory(mask):
        yield(cfg)

#---------------------------------------------------------------Guild Directory

def guild_directory(module_dir):

    """Generator function to read module's Guild directory."""

    THE_LOG.add(".. Loading Guilds")
    mask = os.path.join(module_dir, 'guild/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

#----------------------------------------------------------------Item Directory

def item_directory(module_dir):

    """Generator function to read module's Item directory."""

    THE_LOG.add(".. Loading Items")
    mask = os.path.join(module_dir, 'item/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

#---------------------------------------------------------------Spawn Directory

#def spawn_directory(module_dir):

#    """Generator function to read module's Spawn directory."""

#    THE_LOG.add(".. Loading Spawns")
#    mask = os.path.join(module_dir, 'spawn/*.yml')
#    for cfg in parse_directory(mask):
#        yield(cfg)

#----------------------------------------------------------------Room Directory

def room_directory(module_dir):

    """Generator function to read module's Room directory."""

    THE_LOG.add(".. Loading Rooms")
    mask = os.path.join(module_dir, 'room/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

#----------------------------------------------------------------Help Directory

def help_directory(module_dir):

    """
    Generator function to read module's Help, Guild, and Race directory.

    This second parsing of Guild and Race is used to create Help topics for
    each.
    """

    THE_LOG.add(".. Loading Help Pages")

    mask = os.path.join(module_dir, 'help/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

    ## Also load guilds as help files
    mask = os.path.join(module_dir, 'guild/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

    ## and races...
    mask = os.path.join(module_dir, 'race/*.yml')
    for cfg in parse_directory(mask):
        yield(cfg)

#---------------------------------------------------------------Parse Directory

def parse_directory(mask):

    """
    Generator function to convert a directory of configuration files
    into Python dictionaries.
    """

    filenames = glob.glob(mask)
    #THE_LOG.add(".. %d found" % len(filenames))

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg

#--------------------------------------------------------------------Parse File

def parse_file(filename):

    """
    Converts a YAML config file into a Python dictionary of parameters.
    """

    try:
        fp = open(filename, 'r')
        markup = fp.read()
        fp.close()

    except IOError:
        THE_LOG.add("Error opening file '%s'" % filename)
        sys.exit(1)

    try:
        cfg = parse_markup(markup)

    except BogYAMLError, error:
        THE_LOG.add("Error parsing YAML from file '%s':" % filename)
        THE_LOG.add(error)
        sys.exit(1)

    ## Add the filename to the cfg dictionary
    cfg['filename'] = filename
    return cfg


