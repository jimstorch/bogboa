# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/dat/__init__.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Interface with YAML and SQLite data sources.
"""

from mudlib.dat.file_loader import load_module
from mudlib.dat.tables import check_database
from mudlib.dat.kv import *
from mudlib.dat.map import *

