#------------------------------------------------------------------------------
#   File:       mapping.py
#   Purpose:    Load and save object data to sqlite
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import datetime

from ruleset.dbm.dbconnect import THE_CURSOR
from server.log import THE_LOG


def check_name(name):
    
    """Returns True if the specified character exists in the database."""

    sql = """
        SELECT name FROM character WHERE name = ?;
        """
    ## Have to do this funky because SQLite's rowcount does not work on SELECT
    result = THE_CURSOR.execute(sql,(name,)).fetchone()
    if result:
        return True
    else:
        return False    
        

def check_password(name, password):

    """Returns True if the specified password matches."""

    sql = """
        SELECT name, password FROM character WHERE name = ?;
        """
    ## Have to do this funky because SQLite's rowcount does not work on SELECT
    result = THE_CURSOR.execute(sql,(name,)).fetchone()
    if result:
        
       
       
    else:
        return False  


#--[ Insert Character ]--------------------------------------------------------

def insert_character(client):

    created = str(datetime.datetime.now()) 
    sql = """
    INSERT INTO character ( cid, name, password, gender, race, role, suspended,
        note, date_created, date_last_on, last_ip_address )
        VALUES ( NULL, ?, ?, ?, ?, ?, 0, 'a note', ?, ?, ? ); 
        """    
    THE_CURSOR.execute(sql, ( client.name, client.password, client.gender,
        client.race, client.role, created, created, client.conn.addr ))
    THE_LOG.add("Character '%s' created by user from %s." % (client.name,
        client.conn.addrport()))    


def load_character(client):
    pass

def save_character(client):
    pass
    
def get_attribute(client, tag):
    pass

def check_flag(client, tag):
    pass

def set_flag(client, tag):
    pass

def remove_flag(client, tag):
    pass





