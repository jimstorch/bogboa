# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/stat/stat_math.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Stat related computations.
"""

def bonus_calc(stat):
    """
    Calculate stat bonus or penalty.  
    10 points = 1% = 1.01.
    Negative stat values are ten times as detrimental.        
    """
    ## -100 and below = 0 multiplier
    if stat < -99.9:
        bonus = 0.0
    ## -99 to -1 = 1x penalty
    elif stat < 0.0:
        bonus = 1.0 + (stat / 100.0)
    ## Above 0 = .1x bonus
    else:
        bonus = 1.0 + (stat / 1000.0)
    return bonus    


def stat_bonus(actor, stat_name):
    """
    Given a stat name, return the bonus percentage relative to 1.
    """
    stat = actor.get_stat(stat_name)
    return bonus_calc(stat)


def greater_of_bonus(actor, stat1, stat2):
    """
    Given two stats, return that which gives a higher bonus.
    """
    s1 = actor.get_stat(stat1)
    s2 = actor.get_stat(stat2)
    stat = s1 if s1 > s2 else s2
    return bonus_calc(stat)
