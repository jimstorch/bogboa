# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/stat.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
agi - Agility
chr - Charisma
dex - dexterity
int - Intelligence
luc - Luck
sta - stamina
str - strength
wis - Wisdom

"""



#--------------------------------------------------------------------Stat Bonus

def stat_bonus(stat):

    ## Negative stat effects have 10x the power, 1% loss for every point
    if stat < 0:
        bonus = 1.0 + (float(stat) / 100.0)

    ## Otherwise, grant 1% for every 10 points
    else:
        bonus = 1.0 + (float(stat) / 1000.0)



