# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       mud/calendar.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

from mud.shared import THE_TIME


"""
Game Calendar:

* Time runs at approximately 12x normal, i.e. 1 game day = 2 real hours.
* Stopping the server does not halt the progression of time.
* There are 360 days in the game year.
* There are no leap days/years because the game calendar is aligned to the
  Earth's solar year.
* We're going to forgo having months because they are too short to worry about
  and named months can look out of place in an RPG.  Instead, the day of the
  year is expressed as a Julian number (1 - 360).
* Game years roughly correspond to real months.
* The years cycle through twelve names similar to the Chinese Calendar.
"""


## Houses are the names for each annum in the 12 year cycle.
## They roughly correspond to real-time months (each are ~30 days long).

HOUSES = [   
    'War God', 'Rain God', 'Emerald Witch', 
    'Gold Scarab', 'Fire Kings', 'Stone Emperor',
    'Sapphire Goddess', 'Restless Dead', 'Long Shadows',
    'Frost Lords', 'Wolf', 'River Dragon',
    ]     

## UNIX_ADJ is used to align the start of game time with Jan 1, 2009 00:00 GMT.
UNIX_ADJ = 1230768000.0

## Change this value to adjust what century the game displays.
CENTURY_OFFSET = 0  
             
## Basing time of a SOLAR_YEAR let's us forget about leap days.
SOLAR_YEAR = 31556925.215999998     

## GAME_CYCLE describes the relation twelve game years to one real year.
## If you want to speed up or slow down time change the divisor.
GAME_CYCLE = SOLAR_YEAR / 1.0       

## Shouldn't need to change these.
GAME_YEAR = GAME_CYCLE / 12.0
GAME_MONTH = GAME_YEAR / 12.0
GAME_DAY = GAME_MONTH / 30.0
GAME_JULIAN = GAME_YEAR / 360.0
GAME_HOUR = GAME_DAY / 24.0
GAME_MINUTE = GAME_HOUR / 60.0
GAME_SECOND = GAME_MINUTE / 60.0
                

#-------------------------------------------------------------------------Notes

#    minute = int((tstamp % GAME_HOUR) / GAME_MINUTE)
#    hour = int((tstamp % GAME_DAY) / GAME_HOUR) 
#    day = int((tstamp % GAME_MONTH) / GAME_DAY)
#    julian = int((tstamp % GAME_YEAR) / GAME_JULIAN) + 1
#    month = int((tstamp % GAME_YEAR) / GAME_MONTH)
#    year = int(tstamp / GAME_YEAR) + CENTURY_OFFSET
#    phase = self.year % 12
#    house = HOUSES[self.phase]

#----------------------------------------------------------------------Date Msg


def date_msg(self):
    """
    Return the julian date and the current house.
    """
    tstamp = THE_TIME - UNIX_ADJ
    julian = int((tstamp % GAME_YEAR) / GAME_JULIAN) + 1
    phase = self.year % 12
    return ('day %d of the Year of the %s' %
        (julian, HOUSES[phase]))


#----------------------------------------------------------------------Time Msg

def time_msg(self):
    """
    Return HH:MM and the period of day.
    """
    tstamp = THE_TIME - UNIX_ADJ
    hour = int((tstamp % GAME_DAY) / GAME_HOUR) 
    minute = int((tstamp % GAME_HOUR) / GAME_MINUTE)

    if hour < 1:
        clock = '12:%.2d' % minute
    elif hour >= 1 and hour < 13:     
        clock = '%d:%.2d' % (hour, minute)
    else:
        clock = '%d:%.2d' % (hour - 12, minute)

    if hour < 12:
        retval = '%s in the morning' % clock
    elif hour >= 12 and hour < 17:
        retval = '%s in the afternoon' % clock
    elif hour >= 17 and hour < 21:
        retval = '%s in the evening' % clock
    else:
        retval = '%s at night' % clock

    return retval


#------------------------------------------------------------------Datetime Msg

def datetime_msg(self):
    """
    Return the HH:MM, period of day, julian date, and house.
    """
    return '%s, %s' % (time_msg(), date_msg())


#----------------------------------------------------------------------Sunlight

def sunlight(self):

    """
    Calculate the current sunlight level.
    Return an integer value in the range of 0 (Midnight) to 12 (Noon).
    """
    tstamp = THE_TIME - UNIX_ADJ
    hour = int((tstamp % GAME_DAY) / GAME_HOUR)
    return int(12 - abs(12 - hour))
        

