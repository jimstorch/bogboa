# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   driver/loader/from_yaml.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
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


#------------------------------------------------------------------Parse Markup

def parse_markup(markup):

    """Attempt to parse a YAML markup into a Python dictionary."""

    try:
        ## note the use of 'safe_load' to prevent arbitrary object creation
        cfg = yaml.safe_load(markup)

    except yaml.YAMLError, exc:
        cfg = None
        error = str(exc)

    else:
        if cfg == None:
            error = 'Source contains no data.'
        else:
            error = ''

    return (cfg, error)
