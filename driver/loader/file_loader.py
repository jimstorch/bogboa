# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/loader/file_loader.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

"""
File Loader

Load configuration from YAML files in a module directory.
Eventually this will be replaced with DB Loader that pulls configuration
from a SQLite3 database.
"""

import os
import sys
import glob

from lib import shared
from driver.log import THE_LOG
from driver.loader.from_yaml import parse_script


##   Order of Precedence:

#       Prototypes
#           Items
#           Races
#           Genders
#           Guilds
#           Bots
#
#       Reals
#           Rooms
#           Objects
#           NPCs
#           Players


#-------------------------------------------------------------------Load Module

def load_module(module):

    THE_LOG.add(">> Loading Module: '%s'"  % module)

    ## Load Rooms    
    from obj.room import configure_room, register_room
    for cfg in room_cfg_iter(module):
        room = configure_room(cfg)
        register_room(room)

    ## Load Guilds
    from obj.guild import configure_guild, register_guild
    for cfg in guild_cfg_iter(module):
        guild = configure_guild(cfg)
        register_guild(guild)

    ## Load Help
    from obj.help import configure_help, register_help
    for cfg in help_cfg_iter(module):
        help = configure_help(cfg)
        register_help(help)


#--------------------------------------------------------------------Parse File

def parse_file(filename):

    """
    Converts a YAML config file into a python dictionary of parameters.
    """

    try:
        fp = open(filename, 'r')
        script = fp.read()
        fp.close()

    except IOError:
        THE_LOG.add("Error opening file '%s'" % filename)
        sys.exit(1)

    cfg, error = parse_script(script)

    if error:
        THE_LOG.add("Error parsing YAML from file '%s':" % filename)
        THE_LOG.add(error)
        sys.exit(1)

    return cfg


#----------------------------------------------------------------------Cfg Iter

def cfg_iter(mask):

    """
    Shared YAML text files to configuration iterator.
    """

    filenames = glob.glob(mask)
    THE_LOG.add(">> %d found." % len(filenames))

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg

#-----------------------------------------------------------------Item Cfg Iter

def item_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Items")

    mask = os.path.join(module_dir, 'item/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#-----------------------------------------------------------------Race Cfg Iter

def race_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Races")

    mask = os.path.join(module_dir, 'race/*.yaml')
    filenames = glob.glob(mask)
    for cfg in cfg_iter(mask):
        yield(cfg)


#---------------------------------------------------------------Gender Cfg Iter

def gender_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Genders")

    mask = os.path.join(module_dir, 'gender/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#----------------------------------------------------------------Guild Cfg Iter

def guild_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Guilds")

    mask = os.path.join(module_dir, 'guild/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#-----------------------------------------------------------------Room Cfg Iter

def room_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Rooms")

    mask = os.path.join(module_dir, 'room/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)
  

#-----------------------------------------------------------------Help Cfg Iter

def help_cfg_iter(module_dir):

    THE_LOG.add(">> Loading Help Pages")

    mask = os.path.join(module_dir, 'help/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


