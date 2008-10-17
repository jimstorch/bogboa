
##-----------------------------------------------------------------------------
##  File:       driver/loader/file_loader.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

"""
File Loader

Load configuration from YAML files in a module directory.
Eventually this will be replaced with DB Loader that pulls configuration
from a SQLite3 database.
"""

import os
import sys
import glob

from driver.loader.from_yaml import parse_script

##   Order of Precedence:

#       Prototypes
#           Items
#           Races
#           Genders
#           Sects
#           Bots
#
#       Reals
#           Rooms
#           Objects
#           NPCs
#           Players


#--------------------------------------------------------------------Parse File

def parse_file(filename):

    """
    Converts a YAML config file into a python dictionary of parameters.
    """

    try:
        script = open(filename, 'r').read()

    except IOError:
        print "Error opening file '%s'" % filename
        sys.exit(1)

    cfg, error = parse_script(script)

    if error:
        print "Error parsing YAML from file '%s':" % filename
        print error
        sys.exit(1)

    return cfg


#----------------------------------------------------------------------Cfg Iter

def cfg_iter(mask):

    """
    Shared YAML text files to configuration iterator.
    """

    filenames = glob.glob(mask)
    print "%d found." % len(filenames)

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg

#-----------------------------------------------------------------Item Cfg Iter

def item_cfg_iter(module_dir):

    print "Loading items..."

    mask = os.path.join(module_dir, 'item/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#-----------------------------------------------------------------Race Cfg Iter

def race_cfg_iter(module_dir):

    print "Loading races..."

    mask = os.path.join(module_dir, 'race/*.yaml')
    filenames = glob.glob(mask)
    for cfg in cfg_iter(mask):
        yield(cfg)


#---------------------------------------------------------------Gender Cfg Iter

def gender_cfg_iter(module_dir):

    print "Loading genders..."

    mask = os.path.join(module_dir, 'gender/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#-----------------------------------------------------------------Sect Cfg Iter

def sect_cfg_iter(module_dir):

    print "Loading sects..."

    mask = os.path.join(module_dir, 'sect/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)


#-----------------------------------------------------------------Room Cfg Iter

def room_cfg_iter(module_dir):

    print "Loading rooms..."

    mask = os.path.join(module_dir, 'room/*.yaml')
    for cfg in cfg_iter(mask):
        yield(cfg)
  
