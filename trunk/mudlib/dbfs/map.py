# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/dbfs/map.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

import datetime
import hashlib
import sys

from mudlib.log import THE_LOG
from mudlib.dbfs.dbconnect import THE_CURSOR
from mudlib import shared


#------------------------------------------------------------------------Ban IP

def ban_ip(ip, gm, note):

    """Given an IP address, add it to the banned_ip table."""

    sql = """
        INSERT INTO banned_ip
        VALUES (?, ?, ?, ?);
    """
    now = datetime.datetime.now()
    THE_CURSOR.execute(sql, (ip, now, gm, note))

    THE_LOG.add("?? Banned IP %s by '%s' for '%s'" % (ip, gm, note))


#----------------------------------------------------------------------Unban IP

def unban_ip(ip):

    """Given an IP address, remove it from the banned_ip table."""

    sql = """
        DELETE from banned_ip
        WHERE ip = ?;
    """

    THE_CURSOR.execute(sql, (ip,))

#---------------------------------------------------------------Check Banned IP

def check_banned_ip(ip):

    """Test the given IP address against the ban table."""

    sql = """
        SELECT count(ip)
        FROM banned_ip
        where ip = ?;
        """

    result = THE_CURSOR.execute(sql,(ip,)).fetchone()[0]
    return bool(result)

#--------------------------------------------------------------------Check Name

def check_name(name):

    """
    Return True if the given name should be rejected.
    The name may have been banned, reserved, or already be taken.
    """

    sql = """
        SELECT COUNT(name_lower)
        FROM reject_name
        WHERE name_lower = ?;
        """
    result = THE_CURSOR.execute(sql, (name.lower() ,)).fetchone()[0]
    return bool(result)


#--------------------------------------------------------------------Block Name

def block_name(name, gm='', comment=''):

    """Add the given name to the bad names list."""

    sql = """
        INSERT INTO reject_name
        VALUES (?, ?, ?, ?);
        """
    now = datetime.datetime.now()
    THE_CURSOR.execute(sql, (name.lower(), now, gm, comment))


#--------------------------------------------------------------Check Suspension

def check_suspension(uuid):

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


#-------------------------------------------------------------------Check Login

def check_login(name, password):

    """
    Returns True if the specified name and password match.
    Both name and password are case sensitive.
    """

    sql = """
        SELECT COUNT(name)
        FROM account
        WHERE name = ? and hashed_password = ?;
        """

    ## We don't store passwords in cleartext
    hashed_password = hashlib.sha256(password).hexdigest()

    result = THE_CURSOR.execute(sql, (name, hashed_password)).fetchone()[0]
    return bool(result)


#------------------------------------------------------------------Record Visit

def record_visit(uuid, ip):

        """Notes a returning player's IP and timestamp."""

        now = datetime.datetime.now()
        pass


#----------------------------------------------------------------------Set ANSI

#def set_ansi(name, setting):

#    """Record's a player's ANSI preference."""

#    ## Don't try to set for Lobby schmucks, no row
#    if name == 'Anonymous':
#        return

#    sql = """
#        UPDATE body
#        SET use_ansi = ?
#        WHERE name = ?;
#        """

#    THE_CURSOR.execute(sql, (setting, name))


#-----------------------------------------------------------------------Last On

#def last_on(name):

#    sql = """
#        SELECT last_on FROM body
#        WHERE name = ?;
#        """

#    result = THE_CURSOR.execute(sql, (name,)).fetchone()

#    if result:
#        last_on = result['last_on']
#        return last_on.strftime('%B %d, %Y %I:%M %p')

#    else:
#        return "not found."


#-----------------------------------------------------------------Save New Body

#def save_new_body(body):

#    sql = """
#        INSERT INTO body
#            (
#            name,
#            uuid,
#            hashed_password,
#            race,
#            gender,
#            guild,
#            level,
#            last_on,
#            last_ip,
#            use_ansi,
#            play_count
#            )
#        VALUES (?,?,?,?,?,?,?,?,?,?,?);
#        """

#    hashed_password = hashlib.sha256(body.password).hexdigest()
#    last_ip = body.mind.conn.addr
#    now = datetime.datetime.now()
#    use_ansi = body.mind.conn.use_ansi
#    tup = (body.name, body.uuid, hashed_password, body.race,
#        body.gender, body.guild, body.level, now, last_ip, use_ansi, 1)
#    THE_CURSOR.execute(sql, tup)

#    THE_LOG.add('++ New Character created; %s the %s %s by %s' %
#        (body.name, body.race, body.guild,body.mind.origin()))
#    ## Add the name to the reject table so no one else can use it
#    block_name(body.name, 'map.py', 'Taken by player')


#---------------------------------------------------------------------Load Body

#def load_body(body, name):

#    sql = """
#        SELECT name, uuid, race, gender, guild, level, room_uuid, bind_uuid,
#            use_ansi
#        FROM body
#        WHERE name = ?;
#        """

#    result = THE_CURSOR.execute(sql,(name,)).fetchone()

#    if result:
#        body.name = result['name']
#        body.alias = body.name
#        body.uuid = result['uuid']
#        body.race = result['race']
#        body.gender = result['gender']
#        body.guild = result['guild']
#        body.level = result['level']
#        body.room = shared.find_room(result['room_uuid'])
#        body.bind = shared.find_room(result['bind_uuid'])
#        body.mind.conn.use_ansi = result['use_ansi']

#        THE_LOG.add('== Loaded %s the %s %s from %s' % (body.name, body.race,
#            body.guild, body.mind.origin()))

#    else:
#        THE_LOG.add("!! Database Error: Body not found for '%s'" % name)
#        sys.exit(1)


#-------------------------------------------------------------------Update Body

def update_body(body):
    pass


#---------------------------------------------------------------------Add Skill

def add_skill(uuid, skill, value):
    pass


#------------------------------------------------------------------Update Skill

def update_skill(uuid, skill, value):
    pass
