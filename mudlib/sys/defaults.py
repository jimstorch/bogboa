# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/sys/defaults.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
These are the default settings for new characters and mobs.
"""

import copy
from mudlib.sys.config import LOBBY_UUID
from mudlib.sys.config import START_UUID

#---------------------------------------------------------------------Abilities

_ABILITIES = set([
    'north', 'south', 'east', 'west',
    'tell', 'reply', 'say', 'emote', 'ooc', 'shout',
    'help', 'commands', 'quit'
    'time', 'date', 'uptime',
    'ansi', 'stats', 'topics',
    'look',
    'take',
    'kick', 'shutdown',
    ])

def default_abilities():
    return copy.copy(_ABILITIES)


#-----------------------------------------------------------------------Account

_ACCOUNT = {
    'last_on':None,
    'last_ip':None,
    'play_count':1,
    'status':'ok',
    'email':'',
    }

def default_account():
    return copy.copy(_ACCOUNT)


#----------------------------------------------------------------------Bag Type

_BAG_ITEMS = {}

def default bag_items():
    return copy.copy(_BAG_ITEMS)


#---------------------------------------------------------------------Bag Items

_BAG_TYPE = {}

def default bag_type():
    return copy.copy(_BAG_TYPE)


#-------------------------------------------------------------------Preferences

_PREFERENCES = {
    'use_ansi':1,
    }

def default_preferences():
    return copy.copy(_PREFERENCES)


#-----------------------------------------------------------------------Profile

_PROFILE = {
    'race':'human',
    'gender':'male',
    'guild':'fighter',
    'level':1,
    'xp':0,
    'room':START_UUID
    }

def default_profile():
    return copy.copy(_PROFILE)


#---------------------------------------------------------------------Resources

_RESOURCES = {
    'life':1,
    'energy':1,
    }

def default_resources():
    return copy.copy(_RESOURCES)


#------------------------------------------------------------------------Skills

_SKILLS = {}

def default_skills():
    return copy.copy(_SKILLS)


#-------------------------------------------------------------------------Stats

_STATS = {}

def default_stats():
    return copy.copy(_STATS)


#----------------------------------------------------------------Wardrobe Slots

## TODO: replace with item UUIDs
_START_LEGS = None
_START_CHEST = None
_START_WEAPON = None

## keep this matched with mudblib.inventory._WEAR_SLOTS
_WARDROBE_SLOTS = {
    'head':None,
    'face':None,
    'ears':None,
    'neck':None,
    'shoulders':None,
    'back':None,
    'chest':START_CHEST,
    'arms':None,
    'wrists':None,
    'hands':None,
    'fingers':None,
    'primary':START_WEAPON,
    'secondary':None,
    'waist':None,
    'legs':START_LEGS,
    'feet':None,
    }

def default_wardrobe_slots():
    return copy.copy(_WARDROBE_SLOTS)
