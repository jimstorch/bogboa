# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/world/stat.py
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


class MobStat(object):

    def __init__(self):

        self.stats = {}

    def get_stat(self, stat_name):

        """
        Given a stat name, return the current value or 0 if not found.
        """

        scale = self.get_level() * 2.0   ## Method from Profile class
        return self.stats.get(stat_name, 0.0) + scale



class UsrStat(MobStat):

    def __init__(self):

        MobStat.__init__(self)



    def stat_bonus(self, stat_name):

        """
        Given a stat name, return a bonus percentage relative to 1.
        10 points = 1% = 1.01.
        Negative stat values are ten times as detrimental.
        """

        stat = self.get_stat(stat_name)

        ## -100 and below = 0 multiplier
        if stat < -99.0:
            bonus = 0.0

        ## -99 to -1 = 1x penalty
        elif stat < 0.0:
            bonus = 1.0 + (stat / 100.0)

        ## Above 0 = .1x bonus
        else:
            bonus = 1.0 + (stat / 1000.0)

        return bonus
