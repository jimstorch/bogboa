# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/dat/dbconnect.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import sys

try:
    ## Do we have the built-int Python 2.5 version?
    import sqlite3 as sqlite
except ImportError:
    try:
        ## No, so let's try for the site package
        from pysqlite2 import dbapi2 as sqlite
    except:
        print "Please install pysqlite2 or upgrade to Python >= 2.5."
        sys.exit(1)

## Open the database with autocommit on and auto-convert dates and timestamps
DBCONN = sqlite.connect('data/mud.sqlite', isolation_level=None,
    detect_types=sqlite.PARSE_DECLTYPES)

## Assign a row factory so we can access columns by name
#DBCONN.row_factory = sqlite.Row


#--[ Global Instance ]---------------------------------------------------------

THE_CURSOR = DBCONN.cursor()

#------------------------------------------------------------------------------
