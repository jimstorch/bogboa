##-----------------------------------------------------------------------------
##  File:       lib/sect/sect_creator.py
##  Author:     Jim Storch
##-----------------------------------------------------------------------------

import sys

from lib.sect.sect import Sect
from lib.shared import SECT

#-----------------------------------------------------------------Register sect

def register_sect(sect):

    """
    Given a configured sect, register it with the shared sect dictionary.
    """

    if sect.uuid in SECT:
        print ( "ERROR! Duplicate UUID (%s) found while registering "
            "sect '%s' from module '%s'."  %  (
            sect.uuid, sect.name, sect.module) )
        sys.exit(1)
    else:
        SECT[sect.uuid] = sect


#----------------------------------------------------------------Configure sect

def configured_sect(cfg):

    """
    Given a configuration dictionary, create a sect and configure it.
    Returns the configured sect.
    """

    sect = Sect()

    if 'name' in cfg:
        sect.name = cfg.pop('name')
    else:
        print "ERROR! Missing name in sect config."
        sys.exit(1)

    if 'uuid' in cfg:
        sect.uuid = cfg.pop('uuid')
    else:
        print "ERROR! Missing UUID in config for sect '%s'." % name
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
        print ( "WARNING! Unrecognized key(s) in config for sect '%s': %s" 
            % ( sect.name, cfg.keys()) ) 

    return sect    
