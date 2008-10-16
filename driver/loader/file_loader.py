
##-----------------------------------------------------------------------------
##  File:       driver/loader/file_loader.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

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


##-------------------------------------------------------------------Parse File

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


##-------------------------------------------------------------------Items Iter

def item_iter(module_dir):

    """
    Loads all items from YAML scripts in the given module directory.
    """

    print "Loading items..."

    mask = os.path.join(module_dir, 'items/*.yaml')
    filenames = glob.glob(mask)
    
    print "%d found." % len(filenames)

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg


##--------------------------------------------------------------------Race Iter

def race_iter(module_dir):

    """
    Loads all races from YAML scripts in the given module directory.
    """

    print "Loading races..."

    mask = os.path.join(module_dir, 'races/*.yaml')
    filenames = glob.glob(mask)
    
    print "%d found." % len(filenames)

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg


##--------------------------------------------------------------------Sect Iter

def sect_iter(module_dir):

    """
    Loads all sects from YAML scripts in the given module directory.
    """

    print "Loading sects..."

    mask = os.path.join(module_dir, 'sects/*.yaml')
    filenames = glob.glob(mask)
    
    print "%d found." % len(filenames)

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg


##--------------------------------------------------------------------Room Iter

def room_iter(module_dir):

    """
    Loads all rooms from YAML scripts in the given module directory.
    """

    print "Loading rooms..."

    mask = os.path.join(module_dir, 'rooms/*.yaml')
    filenames = glob.glob(mask)
    
    print "%d found." % len(filenames)

    for filename in filenames:
        cfg = parse_file(filename)
        yield cfg
  
