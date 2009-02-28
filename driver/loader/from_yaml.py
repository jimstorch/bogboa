# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/loader/from_yaml.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

try:
    import yaml
except ImportError:
    print ( "Please install the PyYAML library for Python. "
            "See www.pyyaml.org" )
    sys.exit(1)

## Single point of conversion in the event we move away from YAML
## Also, having it external like this lets me call it from an OLC-style tool 


#------------------------------------------------------------------Parse Script

def parse_script(script):

    """Attempt to parse a YAML script into a Python dictionary."""

    try:
        ## note the use of 'safe_load' to prevent arbitrary object creation
        cfg = yaml.safe_load(script)

    except yaml.YAMLError, exc:
        cfg = None
        error = str(exc)

    else:
        if cfg == None:
            error = 'Source contains no data.'
        else:
            error = ''

    return (cfg, error)
