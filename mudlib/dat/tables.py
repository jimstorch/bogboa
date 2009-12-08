# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/dat/tables.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import datetime

from mudlib.sys.log import THE_LOG
from mudlib.dat.dbconnect import THE_CURSOR


#----------------------------------------------------------------Check Database

def check_database():

    """
    Verifies the existence of SQLite3 tables and creates any that are missing.
    """

    THE_LOG.add(">> Checking Database")

    ## Check/Set a user version for the database
    ## Might use this value for automatic table conversion in future releases
    user_version = THE_CURSOR.execute("PRAGMA user_version").fetchone()[0]
    if user_version == 0:
        THE_CURSOR.execute("PRAGMA user_version=1001;")
        THE_LOG.add("?? Using new database file.")
    else:
        THE_LOG.add(".. DB version is %d" % user_version)

    sql = """
        SELECT COUNT(*) FROM sqlite_master WHERE NAME = ?;
        """

    if not THE_CURSOR.execute(sql, ('account',)).fetchone()[0]:
        THE_LOG.add("?? Missing 'account' table in database, creating it.")
        create_account_table()

    if not THE_CURSOR.execute(sql, ('key_value',)).fetchone()[0]:
        THE_LOG.add("?? Missing 'key_value' table in database, creating it.")
        create_key_value_table()

    if not THE_CURSOR.execute(sql, ('reject_name',)).fetchone()[0]:
        THE_LOG.add("?? Missing 'reject_name' table in database, creating it.")
        create_reject_name_table()
        pre_reject_names()

    if not THE_CURSOR.execute(sql, ('banned_ip',)).fetchone()[0]:
        THE_LOG.add("?? Missing 'banned_ip' table in database, creating it.")
        create_banned_ip_table()

    if not THE_CURSOR.execute(sql, ('suspension',)).fetchone()[0]:
        THE_LOG.add("?? Missing 'suspension' table in database, creating it.")
        create_suspension_table()


    ## Lastly, vacuum the database
    sql = """VACUUM;"""

    THE_CURSOR.execute(sql)


#----------------------------------------------------------Create Account Table

def create_account_table():


    sql = """DROP TABLE IF EXISTS account;"""

    THE_CURSOR.execute(sql)

#    sql = """
#        CREATE TABLE IF NOT EXISTS account
#            (
#            name TEXT PRIMARY KEY,
#            uuid TEXT KEY,
#            hashed_password TEXT,
#            email TEXT,
#            race TEXT,
#            gender TEXT,
#            guild TEXT,
#            level INTEGER,
#            room_uuid TEXT,
#            bind_uuid TEXT,
#            bag_name TEXT,
#            bag_limit REAL,
#            bag_reduction REAL,
#            use_ansi BOOLEAN DEFAULT TRUE,
#            last_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#            last_ip TEXT,
#            play_count INTEGER
#            );
#        """

    sql = """
        CREATE TABLE IF NOT EXISTS account
            (
            name TEXT PRIMARY KEY,
            uuid TEXT KEY,
            hashed_password TEXT
            );
        """


    THE_CURSOR.execute(sql)


#--------------------------------------------------------Create Key-Value Table

def create_key_value_table():

    sql = """DROP TABLE IF EXISTS key_value;"""

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS key_value
            (
            uuid TEXT,
            category TEXT,
            key TEXT,
            value TEXT,
            PRIMARY KEY(uuid, category, key)
            );
        """

    THE_CURSOR.execute(sql)

#------------------------------------------------------Create Reject Name Table

def create_reject_name_table():

    sql = """DROP TABLE IF EXISTS reject_name;"""

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS reject_name
            (
            name_lower TEXT PRIMARY KEY,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            gm_name TEXT,
            gm_note TEXT
            );
        """

    THE_CURSOR.execute(sql)


#--------------------------------------------------------------Pre-Reject Names

def pre_reject_names():

    sql = """
        INSERT INTO reject_name
        VALUES (?, ?, ? , ?);
        """

    bad_names = ['bogboa', 'gm', 'admin', 'sysop', 'anonymous', 'anon',
        'test', 'nobody', 'noone',
        ]
    now = datetime.datetime.now()

    for name in bad_names:
        THE_CURSOR.execute(sql, (name.lower(), now,
            'tables.py', 'pre-rejected name'))


#--------------------------------------------------------Create Banned IP Table

def create_banned_ip_table():

    sql = """DROP TABLE IF EXISTS banned_ip;"""

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS banned_ip
            (
            ip TEXT PRIMARY KEY,
            active INT,
            gm_name TEXT,
            gm_note TEXT
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

    THE_CURSOR.execute(sql)


#--------------------------------------------------------Creat Suspension Table

def create_suspension_table():

    sql = """DROP TABLE IF EXISTS suspension;"""

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS suspension
            (
            uuid TEXT KEY,
            active INT,
            days INTEGER,
            gm_name TEXT,
            gm_note TEXT,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

    THE_CURSOR.execute(sql)
