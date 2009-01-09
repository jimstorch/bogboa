# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   File:       driver/calendar.py
#   Author:     Jim Storch
#------------------------------------------------------------------------------

import time

#from lib.shared import THE_TIME

## Houses repeat like the Chinese Calendar.
## They roughly correspond to the months of the year.

HOUSES = [   
    'War God', 'Rain God', 'Emerald Witch', 
    'Gold Scarab', 'Fire Kings', 'Stone Emperor',
    'Sapphire Goddess', 'Restless Dead', 'Long Shadows',
    'Frost Lords', 'Wolf', 'River Dragon',
    ]     

UNIX_ADJ = 1230768000.0             ## Jan 1, 2009 00:00:00am GMT
SOLAR_YEAR = 31556925.215999998     ## Number of seconds in a Solar Year
GAME_CYCLE = SOLAR_YEAR / 1.0       ## Tweak the relative years here
GAME_YEAR = GAME_CYCLE / 12.0
GAME_MONTH = GAME_YEAR / 12.0
GAME_DAY = GAME_MONTH / 30.0
GAME_JULIAN = GAME_YEAR / 360.0
GAME_HOUR = GAME_DAY / 24.0
GAME_MINUTE = GAME_HOUR / 60.0


class MUD_Time(object):
    
    def __init__(self, tstamp=None):
        if tstamp == None:
            tstamp = time.time() - UNIX_ADJ
        self.minute = int((tstamp % GAME_HOUR) / GAME_MINUTE)
        self.hour = int((tstamp % GAME_DAY) / GAME_HOUR) + 1
        self.day = int((tstamp % GAME_MONTH) / GAME_DAY)
        self.julian = int((tstamp % GAME_YEAR) / GAME_JULIAN)
        self.month = int((tstamp % GAME_YEAR) / GAME_MONTH)
        self.year = int(tstamp / GAME_YEAR)
        self.phase = self.year % 12
        self.house = HOUSES[self.phase]


    def date_msg(self):
        """
        Return the julian date and the current house.
        """
        tstamp = time.time() - UNIX_ADJ
        julian = int((tstamp % GAME_YEAR) / GAME_JULIAN) + 1
        phase = self.year % 12
        return ('day %d of the Year of the %s' %
            (julian, HOUSES[phase]))

    def time_msg(self):
        """
        Return HH:MM and the period of day.
        """
        tstamp = time.time() - UNIX_ADJ
        hour = int((tstamp % GAME_DAY) / GAME_HOUR) + 1
        minute = int((tstamp % GAME_HOUR) / GAME_MINUTE)

        if hour < 13:
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

    def datetime_msg(self):
        """
        Return the HH:MM, period of day, julian date, and house.
        """
        return '%s, %s' % (self.time_msg(), self.date_msg())

    def sunlight(self):

        """
        Calculate the current sunlight level.
        Returns 10 for noon, -1 for midnight
        """
        
        tstamp = time.time() - UNIX_ADJ
        hour = int((tstamp % GAME_DAY) / GAME_HOUR) + 1
        return int(10.5 - abs(12.5 - hour))
        



if __name__ == '__main__':

    mt = MUD_Time()

    print("Day %d of the Year of the %s, at %.2d:%.2d" %
        (mt.julian, mt.house, mt.hour, mt.minute))

    print ("%.2d/%.2d/%.4d" % (mt.month, mt.day, mt.year))
    print mt.time_msg()
    print mt.date_msg()
    print mt.datetime_msg()
    print 'Relative sunlight = %d' % mt.sunlight()
