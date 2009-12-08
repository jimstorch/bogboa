# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/usr/help.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

from mudlib.sys import shared
from mudlib.sys.log import THE_LOG


#--------------------------------------------------------------------------Help

class Help(object):

    def __init__(self):

#        self.uuid = None
        self.module = None
        self.name = None
        self.keywords = None
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

    help.filename = cfg.pop('filename')

    if 'name' in cfg:
        help.name = cfg.pop('name')
    else:
        THE_LOG.add("!! Missing name in help config.")
        sys.exit(1)

    if 'keywords' in cfg:
        help.aliases = cfg.pop('keywords')

#    if 'uuid' in cfg:
#        help.uuid = cfg.pop('uuid')
#    else:
#        THE_LOG.add("ERROR! Missing UUID in config for help '%s'." % help.name)
#        sys.exit(1)

    if 'text' in cfg:
        help.text = cfg.pop('text')
    else:
        THE_LOG.add("!! Missing text in config for help '%s'." % help.name)
        sys.exit(1)


#    if 'module' in cfg:
#        help.module = cfg.pop('module')
#    else:
#        help.module = None
#        THE_LOG.add("WARNING: Missing 'module' value for help '%s'."
#            % help.name)

    ## Ignore from Guild files
    if 'skills' in cfg:
        cfg.pop('skills')

    ## Ignore from Race files
    if 'stats' in cfg:
        cfg.pop('stats')

    ## Unused at this time
    if 'version' in cfg:
        cfg.pop('version')


    ## Complain if there are leftover keys -- probably a typo in the YAML
    if cfg:
        THE_LOG.add("!! Unrecognized key(s) in config for help '%s': %s"
            % ( help.name, cfg.keys()) )

    return help


#-----------------------------------------------------------------Register Help

def register_help(help):

    """
    Given a configured help, register it with the shared HELP dictionary.
    """

    if help.name in shared.HELPS:
        THE_LOG.add("!! Duplicate name found while registering "
            "help text '%s' in module '%s'."  %  (help.name, help.module))
        sys.exit(1)
    else:
        shared.HELPS[help.name] = help

    ## Also map any aliases for this text
    if help.keywords:
        for keyword in help.keywords:
            if keyword in shared.HELPS:
                THE_LOG.add("!! Duplicate keyword found while registering "
                    "help text '%s' in module '%s'."  %
                    (help.name, help.module))
                sys.exit(1)
            else:
                shared.HELPS[keyword] = help
