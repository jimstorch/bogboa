# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/model/tables.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import datetime

from driver.log import THE_LOG
from driver.dbms.dbconnect import THE_CURSOR


#-------------------------------------------------------------------Table Check

def check_tables():
    
    """
    Verifies the existence of SQLite3 tables and creates any that are missing.
    """
    
    sql = """
        SELECT COUNT(*) FROM sqlite_master WHERE NAME = ?;
        """

    if not THE_CURSOR.execute(sql, ('body',)).fetchone()[0]:
        THE_LOG.add("Missing 'body' table in database, creating it.")
        create_body_table()

    if not THE_CURSOR.execute(sql, ('flag',)).fetchone()[0]:
        THE_LOG.add("Missing 'flag' table in database, creating it.")
        create_flag_table()
            
    if not THE_CURSOR.execute(sql, ('bad_name',)).fetchone()[0]:
        THE_LOG.add("Missing 'bad_name' table in database, creating it.")    
        create_bad_name_table()
        populate_bad_name_table()

    if not THE_CURSOR.execute(sql, ('banned_ip',)).fetchone()[0]:
        THE_LOG.add("Missing 'banned_ip' table in database, creating it.")
        create_banned_ip_table()

    if not THE_CURSOR.execute(sql, ('suspension',)).fetchone()[0]:
        THE_LOG.add("Missing 'suspension' table in database, creating it.")
        create_suspension_table()


#-------------------------------------------------------------Create Body Table


def create_body_table():

    sql = """DROP TABLE IF EXISTS body;"""

    THE_CURSOR.execute(sql)    

    sql = """
        CREATE TABLE IF NOT EXISTS body 
            (
            name TEXT PRIMARY KEY,
            name_lower TEXT KEY,
            hashed_password TEXT,
            body_uuid TEXT,
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


#--------------------------------------------------------Create Bad Names Table

def create_bad_name_table():

    sql = """DROP TABLE IF EXISTS bad_name;"""

    THE_CURSOR.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS bad_name
            (
            name_lower TEXT PRIMARY KEY,
            date_added TIMESTAMP,
            gm_name TEXT,
            gm_note TEXT
            );
        """

    THE_CURSOR.execute(sql)                


#-------------------------------------------------------Populate Bad Name Table

def populate_bad_name_table():

    sql = """
        INSERT INTO bad_name
        VALUES (?, ?, '', 'Predefined rejected name');
        """

    bad_names = ['bogboa', 'gm', 'admin', 'sysop']
    now = datetime.datetime.now()

    for name in bad_names:
        THE_CURSOR.execute(sql, (name.lower(), now))    

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

    slq = """
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



