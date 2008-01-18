#------------------------------------------------------------------------------
#   File:       dbconnect.py
#   Purpose:    Establish a connection to an SQLite data file
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import sys

try:
    # Do we have the built-int Python 2.5 version?
    import sqlite3 as sqlite
except ImportError:
    try:
        # No, so let's try for the site package
        from pysqlite2 import dbapi2 as sqlite
    except:
        print "Please install pysqlite2 or upgrade to Python >= 2.5."
        sys.exit(1)

# Open the database with autocommit on
DBCONN = sqlite.connect('data/sqlite_files/sqlite.db', isolation_level=None)


#--[ Shared Database Cursor ]--------------------------------------------------

THE_CURSOR = DBCONN.cursor()
