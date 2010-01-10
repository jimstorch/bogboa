# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/defense.py
#   Copyright 2009 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Compute defensive skills.
"""

from mudlib.skill import stat_bonus
from mudlib.skill import skill_check


def armor_rating(actor):
    """
    Rate Actor on armor worn.
    """
    ## Note that armor is pre-scaled by Guild's armor type skills * level
    armor = actor.get_total_ac()
    bonus = stat_bonus(actor, 'precision')
    return armor * bonus


def defense_rating(actor, tutor=True):
    """
    Rate relative difficulty to strike Actor.
    Uses defense skill + armor.
    """
    if tutor:
        skillup_check(actor, 'defense')  
    base = actor.get_skill('defense')
    bonus = stat_bonus(actor, 'brawn')
    armor = armor_rating(actor)
    return base * bonus + armor


def dodge_rating(actor):
    """
    Actor rating to dodge a melee attack.
    """
    if tutor:
        skillup_check(actor, 'dodge')  
    base = actor.get_skill('dodge')
    bonus = stat_bonus(actor, 'cunning')
    return base * bonus    


def parry_rating(actor):
    """
    Actor rating to parry a melee attack.
    """
    if tutor:
        skillup_check(actor, 'parry')  
    base = actor.get_skill('parry')
    bonus = stat_bonus(actor, 'precision')
    return base * bonus    


