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
dex - Dexterity
int - Intelligence
luc - Luck
sta - Stamina
str - Strength
wis - Wisdom

Each Skill has two relevant Stats -- Stats enhance an Ability 1% per 10 points.
Negative stats are ten times as detrimental, 1% loss per negative point.
Each Ability utilizes one Skill.
Each Guild has one Primary and two Secondary Stats, based on Abilities.
Primary + Secondary A affects combat/damaging magic.
Primary + Secondary B affects defense/support magic.

"""



#--------------------------------------------------------------------Stat Bonus

def stat_bonus(stat):

    ## Negative stat effects have 10x the power, 1% loss for every point
    if stat < 0:
        bonus = 1.0 + (float(stat) / 100.0)

    ## Otherwise, grant 1% for every 10 points
    else:
        bonus = 1.0 + (float(stat) / 1000.0)



