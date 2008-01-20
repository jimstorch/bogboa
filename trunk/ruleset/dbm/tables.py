#------------------------------------------------------------------------------
#   File:       tables.py
#   Purpose:    Load and save object data to sqlite
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from ruleset.dbm.dbconnect import THE_CURSOR
from server.log import THE_LOG


#--[ Check Tables ]------------------------------------------------------------

def check_tables():

    """Returns True if all the application tables exist."""

    sql = """
        SELECT name 
            FROM sqlite_master
            WHERE type='table';
        """
    THE_CURSOR.execute(sql)
    table_names = [ table[0] for table in THE_CURSOR ] 
    
    result = True

    if 'character' not in table_names:
        result = False
        THE_LOG.add('Table CHARACTER not found.')
    if 'stat' not in table_names:
        result = False
        THE_LOG.add('Table STAT not found.')  
    if 'skill' not in table_names:
        result = False
        THE_LOG.add('Table SKILL not found.')      
    if 'ability' not in table_names:
        result = False
        THE_LOG.add('Table ABILITY not found.')   
    if 'inventory' not in table_names:
        result = False
        THE_LOG.add('Table INVENTORY not found.')   
    if 'flag' not in table_names:
        result = False
        THE_LOG.add('Table FLAG not found.')         
    if 'banned_ip' not in table_names:
        result = False
        THE_LOG.add('Table BANNED_IP not found.')  

    return result


#--[ Create Tables ]-----------------------------------------------------------

def create_tables():

    sql = """
        CREATE TABLE IF NOT EXISTS character 
            (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            handle TEXT UNIQUE,
            name TEXT UNIQUE,
            password TEXT,
            gender TEXT,
            race TEXT,
            role TEXT,
            suspended INTEGER,
            note TEXT,
            date_created TEXT,
            date_last_on TEXT,
            last_ip_address TEXT
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS stat 
            (
            cid INTEGER,
            name TEXT UNIQUE,
            value INTEGER
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS skill
            (
            cid INTEGER,
            name TEXT UNIQUE,
            value INTEGER
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS ability
            (
            cid INTEGER,
            name TEXT UNIQUE,
            value INTEGER
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS flag
            (
            cid INTEGER,
            name TEXT UNIQUE,
            value TEXT
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS inventory
            (
            cid INTEGER,
            name TEXT UNIQUE,
            value TEXT
            );
        """
    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS banned_ip
            (
            address TEXT,
            note TEXT
            );
        """
    THE_CURSOR.execute(sql)
            

