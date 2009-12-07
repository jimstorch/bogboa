#------------------------------------------------------------------------------
#   driver/dbms/kv.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Functions to support key-value storage and retrieval from SQLite3.

The key_value table's primary index is the tuple (uuid, category, key) so
the combination of these three values MUST always be unique.  This allows us
to take advantage of SQLite's 'INSERT OR REPLACE' mechanism where we don't
have to worry if the row already exists before inserting or updating.
"""

from driver.dbms.dbconnect import THE_CURSOR


#----------------------------------------------------------------------Fetch KV

def fetch_kv(uuid, category, key):
    """
    Given a UUID, category, and key, retrieves the value from the database.
    """
    sql = """
        SELECT value
        FROM key_value
        WHERE uuid = ? AND category = ? AND key = ?;
        """
    THE_CURSOR.execute(sql, (uuid, category, key))
    return THE_CURSOR.fetchone()[0]


#----------------------------------------------------------------------Store KV

def store_kv(uuid, category, key, value):
    """
    Given a UUID, category, and dictionary, write them to the database.
    """
    sql = """
        INSERT OR REPLACE INTO key_value (uuid, category, key, value)
        VALUES (?, ?, ?, ?');
        """
    THE_CURSOR.execute(sql,(uuid, category, key, value))


#-----------------------------------------------------------------Fetch KV Dict

def fetch_kv_dict(uuid, category):
    """
    Given a UUID and category, select matching rows and convert them to a
    dictionary.
    """
    sql = """
        SELECT key, value
        FROM key_value
        WHERE uuid = ? AND category = ?;
        """
    dct = {}
    THE_CURSOR.execute(sql, (uuid, category))
    for row in THE_CURSOR:
        dct[row[0]] = row[1]
    return dct


#-----------------------------------------------------------Fetch KV Dict Float

def fetch_kv_dict_float(uuid, category):
     """
    Given a UUID and category, select matching rows and convert them to a
    dictionary of floating point values.
    """
    sql = """
        SELECT key, value
        FROM key_value
        WHERE uuid = ? AND category = ?;
        """
    dct = {}
    THE_CURSOR.execute(sql, (uuid, category))
    for row in THE_CURSOR:
        dct[row[0]] = float(row[1])
    return dct


#-----------------------------------------------------------------Store KV Dict

def store_kv_dict(uuid, category, dct):
    """
    Given a UUID, category, and dictionary, write them to the database.
    """
    sql = """
        INSERT OR REPLACE INTO key_value (uuid, category, key, value)
        VALUES (?, ?, ?, ?');
        """
    ## build a list comprehension of arguments for executemany()
    rows = [ uuid, set_name, k, v) for k, v in dct.items() ]
    THE_CURSOR.executemany(sql, rows)


#------------------------------------------------------------------Fetch KV Set

def fetch_kv_set(uuid, category):
    """
    Given a UUID and category, select matching row keys and convert them to a
    set.
    """
    sql = """
        SELECT key
        FROM key_value
        WHERE uuid = ? AND category = ?;
        """
    THE_CURSOR.execute(sql, (uuid, category))
    return set( [ row[0] for row in THE_CURSOR ] )


#------------------------------------------------------------------Store KV Set

def store_kv_set(uuid, category, st):
    """
    Given a UUID, category, and set, write them to the database.
    """
    sql = """
        INSERT OR REPLACE INTO key_value (uuid, category, key, value)
        VALUES (?, ?, ?, '1');
        """
    ## build a list comprehension of arguments for executemany()
    rows = [ (uuid, category, k) for k in st ]
    THE_CURSOR.executemany(sql, rows)