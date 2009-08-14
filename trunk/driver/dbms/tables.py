# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/model/tables.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import datetime

from driver.log import THE_LOG
from driver.dbms.dbconnect import THE_CURSOR


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
        THE_CURSOR.execute("PRAGMA user_version=10001;")
        THE_LOG.add("-> Using new database file.")
    else:
        THE_LOG.add("-> DB version is %d." % user_version)    

    sql = """
        SELECT COUNT(*) FROM sqlite_master WHERE NAME = ?;
        """

    if not THE_CURSOR.execute(sql, ('body',)).fetchone()[0]:
        THE_LOG.add("Missing 'body' table in database, creating it.")
        create_body_table()

    if not THE_CURSOR.execute(sql, ('ability',)).fetchone()[0]:
        THE_LOG.add("Missing 'ability' table in database, creating it.")
        create_ability_table()

    if not THE_CURSOR.execute(sql, ('skill',)).fetchone()[0]:
        THE_LOG.add("Missing 'skill' table in database, creating it.")
        create_skill_table()

    if not THE_CURSOR.execute(sql, ('flag',)).fetchone()[0]:
        THE_LOG.add("Missing 'flag' table in database, creating it.")
        create_flag_table()

    if not THE_CURSOR.execute(sql, ('inventory',)).fetchone()[0]:
        THE_LOG.add("Missing 'inventory' table in database, creating it.")
        create_inventory_table()
            
    if not THE_CURSOR.execute(sql, ('reject_name',)).fetchone()[0]:
        THE_LOG.add("Missing 'reject_name' table in database, creating it.")    
        create_reject_name_table()
        pre_reject_names()

    if not THE_CURSOR.execute(sql, ('banned_ip',)).fetchone()[0]:
        THE_LOG.add("Missing 'banned_ip' table in database, creating it.")
        create_banned_ip_table()

    if not THE_CURSOR.execute(sql, ('suspension',)).fetchone()[0]:
        THE_LOG.add("Missing 'suspension' table in database, creating it.")
        create_suspension_table()


    ## Lastly, vacuum the database
    sql = """VACUUM;"""
    THE_CURSOR.execute(sql)


#-------------------------------------------------------------Create Body Table


def create_body_table():

    sql = """DROP TABLE IF EXISTS body;"""

    THE_CURSOR.execute(sql)    

    sql = """
        CREATE TABLE IF NOT EXISTS body 
            (
            name TEXT PRIMARY KEY,
            uuid TEXT KEY,
            hashed_password TEXT,
            race TEXT,
            gender TEXT,
            guild TEXT,
            level INTEGER,            
            room_uuid TEXT,
            last_on TIMESTAMP,
            last_ip TEXT,
            play_count INTEGER
            );
        """

    THE_CURSOR.execute(sql)


#----------------------------------------------------------Create Ability Table


def create_ability_table():

    sql = """DROP TABLE IF EXISTS ability;"""

    THE_CURSOR.execute(sql)
    
    sql = """
        CREATE TABLE IF NOT EXISTS ability
            (
            body_uuid TEXT PRIMARY KEY,
            ability TEXT
            );
        """

    THE_CURSOR.execute(sql)


#------------------------------------------------------------Create Skill Table

def create_skill_table():

    sql = """DROP TABLE IF EXISTS skill;"""

    THE_CURSOR.execute(sql)
    
    sql = """
        CREATE TABLE IF NOT EXISTS skill
            (
            body_uuid TEXT PRIMARY KEY,
            skill TEXT,
            value TEXT
            );
        """

    THE_CURSOR.execute(sql)


#-------------------------------------------------------------Create Flag Table

def create_flag_table():

    sql = """DROP TABLE IF EXISTS flag;"""

    THE_CURSOR.execute(sql)
    
    sql = """
        CREATE TABLE IF NOT EXISTS flag
            (
            body_uuid TEXT PRIMARY KEY,
            flag TEXT,
            value TEXT
            );
        """

    THE_CURSOR.execute(sql)


#--------------------------------------------------------Create Inventory Table

def create_inventory_table():
    
    sql = """DROP TABLE IF EXISTS inventory;"""

    THE_CURSOR.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS inventory
        (
        body_uuid TEXT PRIMARY KEY,
        slot TEXT,
        item_uuid TEXT,
        item_count INTEGER
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
            date_added TIMESTAMP,
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

    bad_names = ['bogboa', 'gm', 'admin', 'sysop']
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
            date_added TIMESTAMP,
            gm_name TEXT,
            gm_note TEXT
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
            uuid TEXT PRIMARY KEY,
            date_added TIMESTAMP,
            duration INTEGER,
            gm_name TEXT,
            gm_note TEXT
            );
        """

    THE_CURSOR.execute(sql)    


