# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/model/mapping.py
#   Purpose:    Load and save object data to sqlite
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import datetime
import hashlib

from ruleset.dbm.dbconnect import THE_CURSOR
from server.log import THE_LOG


#---]----------------------------------------------------------------Check Name

def check_name(name):

    """Returns True if the specified character exists in the database."""

    handle = name.lower()

    sql = """
        SELECT handle FROM character WHERE handle = ?;
        """
    ## Have to do this funky because SQLite's rowcount does not work on SELECT
    result = THE_CURSOR.execute(sql,(handle,)).fetchone()

    if result:
        return True
        
    else:
        return False    


#--------------------------------------------------------------Check Suspension

def check_suspension(name):

    handle = name.lower()

    """Returns True if the specified character is under suspension."""

    sql = """
        SELECT suspended FROM character WHERE handle = ?;
        """

    result = THE_CURSOR.execute(sql,(handle,)).fetchone()

    if result:

        if result[0] == True:
            return True
        else:
            return False
            
    else:
        THE_LOG.add('Suspension check requested on non-existant user %s.' %
            name)
        return False      
        

#----------------------------------------------------------------Check Password

def check_password(name, password):
    
    handle = name.lower()
    ## We don't store passwords in cleartext
    hashed_password = hashlib.sha256(password).hexdigest()

    """Returns True if the specified password matches."""

    sql = """
        SELECT password FROM character WHERE handle = ?;
        """
    ## Have to do this funky because SQLite's rowcount does not work on SELECT

    result = THE_CURSOR.execute(sql,(handle,)).fetchone()

    if result:
        
        if hashed_password == result[0]:
            return True
        else:
            return False            

    else:
        THE_LOG.add('Password check requested on non-existant user %s.' %
            name)
        return False  


#--------------------------------------------------------------Insert Character

def insert_character(client):

    created = str(datetime.datetime.now()) 
    ## Again, we don't store passwords in cleartext
    hashed_password = hashlib.sha256(client.password).hexdigest()

    sql = """
    INSERT INTO character ( cid, handle, name, password, gender, race, role, 
        suspended, note, date_created, date_last_on, last_ip_address )
        VALUES ( NULL, ?, ?, ?, ?, ?, ?, 0, 'a note', ?, ?, ? ); 
        """    
    THE_CURSOR.execute(sql, ( client.name.lower(), client.name, 
        hashed_password, client.gender, client.race, client.role, created,
        created, client.conn.addr ))
    THE_LOG.add("Character '%s' created by user from %s." % (client.name,
        client.conn.addrport()))    


#----------------------------------------------------------------Load Character

def load_character(name, client):

    handle = name.lower()
    
    sql = """
    SELECT name, gender, race, role FROM character where handle = ?;
        """    
    result = THE_CURSOR.execute(sql,(handle,)).fetchone()
    client.handle = handle
    client.name = result[0]
    client.gender = result[1]
    client.race = result[2]
    client.role = result[3]
#    print 'load_character', client.handle
    THE_LOG.add("%s logged in using %s client from %s." % (client.handle,
            client.conn.terminal_type, client.conn.addrport())) 


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





