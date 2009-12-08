# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/dat/from_yaml.py
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

from mudlib.sys.error import BogYAMLError


#------------------------------------------------------------------Parse Markup

def parse_markup(markup):

    """Attempt to parse a YAML markup into a Python dictionary."""

    try:
        ## note the use of 'safe_load' to prevent arbitrary object creation
        cfg = yaml.safe_load(markup)

    except yaml.YAMLError, error:
        error = str(error)
        raise BogYAMLError('Error parsing YAML: %s' % error)

    if cfg == None:
        raise BogYAMLError('YAML Source contains no data.')

    return cfg
