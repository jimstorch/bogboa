# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/dbms/map.py
#   Purpose:    Load and save object data to sqlite
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import datetime
import hashlib

from driver.log import THE_LOG
from driver.dbms.dbconnect import THE_CURSOR


#--------------------------------------------------------------------Check Name

def check_name(name):

    """Return True if the specified character exists in the database."""

    sql = """
        SELECT COUNT(name_lower)
        FROM body
        WHERE name_lower = ?;
        """
    ## Have to do this funky because SQLite's rowcount does not work on SELECT
    result = THE_CURSOR.execute(sql, (name.lower() ,)).fetchone()[0]
    return bool(result)
  

#----------------------------------------------------------------Check Bad Name

def check_bad_name(name):
   
    """Return True is the given name is in the bad_name table."""

    sql = """
        SELECT COUNT(name_lower)
        FROM bad_name
        WHERE name_lower = ?;
        """
    result = THE_CURSOR.execute(sql,(name.lower(),)).fetchone()[0]
    return bool(result)
    

#--------------------------------------------------------------------Block Name

def block_name(name, gm='', comment=''):

    """Add the given name to the bad names list."""

    sql = """
        INSERT INTO bad_name
        VALUES (?,?,?,?);
        """

    now = datetime.datetime.now()
    THE_CURSOR.execute(sql, (name.lower(), now, gm, comment))


#----------------------------------------------------------------Suspended Days

def suspended_days(uuid):

    """Given an UUID, returns days remaining in a suspension or 0 for none."""

    sql = """
        SELECT date_added, duration
        FROM suspended WHERE uuid = ?
        ORDER BY date_added DESC
        LIMIT 1;
        """

    result = THE_CURSOR.execute(sql,(uuid,)).fetchone()

    if result:
        date_added = result['date_added']
        duration = result['duration']
        days_off = datetime.timedelta(duration)
        end_date = date_added + days_off
        now = datetime.datetime.now()
    
        ## if the suspension is still active return days remaining
        if end_date > now:
            left = end_date - now
            return left.days 

    ## Otherwise, return zero
    return 0 


#----------------------------------------------------------------Check Password

def check_password(name, password):
    
    """
    Returns True if the specified name and password match.
    Name is not case sensitive, but password is.    
    """

    sql = """
        SELECT COUNT(name_lower) 
        FROM body
        WHERE name_lower = ? and hashed_password = ?;
        """

    ## We don't store passwords in cleartext
    hashed_password = hashlib.sha256(password).hexdigest()

    result = THE_CURSOR.execute(sql, 
        (name.lower(), hashed_password)).fetchone()[0]

    return bool(result)

#---------------------------------------------------------------------Save Body

def save_body(body):

    sql = """
        """

#---------------------------------------------------------------------Load Body

def load_body(body, name):

    pass

#-------------------------------------------------------------------Update Body

def update_body(body):

    pass






