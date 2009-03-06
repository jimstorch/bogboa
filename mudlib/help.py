# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mudlib/help.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

from mudlib.shared import HELPS
from driver.log import THE_LOG


#--------------------------------------------------------------------------Help

class Help(object):

    def __init__(self):

        self.uuid = None
        self.module = None
        self.name = None
        self.aliases = None
        self.text = None

    def on_read(self, client):
        """Send the contents of the help text to the player."""
        client.inform(self.text)


#----------------------------------------------------------------Configure Help

def configure_help(cfg):

    """
    Given a configuration dictionary, create a help object and configure it.
    Returns the configured help.
    """

    help = Help()

    if 'name' in cfg:
        help.name = cfg.pop('name')
    else:
        THE_LOG.add("ERROR! Missing name in help config.")
        sys.exit(1)

    if 'aliases' in cfg:
        help.aliases = cfg.pop('aliases')

    if 'uuid' in cfg:
        help.uuid = cfg.pop('uuid')
    else:
        THE_LOG.add("ERROR! Missing UUID in config for help '%s'." % help.name)
        sys.exit(1)

    if 'text' in cfg:
        help.text = cfg.pop('text')
    else:
        THE_LOG.add("ERROR! Missing text in config for help '%s'." % help.name)
        sys.exit(1)


    if 'module' in cfg:
        help.module = cfg.pop('module')
    else:
        help.module = None
        THE_LOG.add("WARNING: Missing 'module' value for help '%s'." 
            % help.name)       


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("WARNING! Unrecognized key(s) in config for help '%s': %s" 
            % ( help.name, cfg.keys()) ) 

    return help    


#-----------------------------------------------------------------Register Help

def register_help(help):

    """
    Given a configured help, register it with the shared HELP dictionary.
    """

    if help.name in HELPS:
        THE_LOG.add("ERROR! Duplicate name found while registering "
            "help text '%s' in module '%s'."  %  (help.name, help.module))
        sys.exit(1)
    else:
        HELPS[help.name] = help

    ## Also map any aliases for this text
    if help.aliases:
        for alias in help.aliases:
            if alias in HELPS:
                THE_LOG.add("ERROR! Duplicate alias found while registering "
                    "help text '%s' in module '%s'."  %  
                    (help.name, help.module))
                sys.exit(1)        
            else:
                HELPS[alias] = help

