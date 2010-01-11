# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/ranged_skills.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Rate ranged weapon skills.
"""

from mudlib.skill import skill_check


def ranged_combat_rating(actor, tutor=True):
    """
    Rate Actor's general combat prowess.
    """
    if tutor:
        skillup_check(actor, 'ranged_combat')
    base = actor.get_skill('ranged_combat')
    bonus = stat_bonus(actor, 'brawn')
    return base * bonus


def ranged_weapon_rating(actor):
    """
    Rate Actor's ability to use his selected ranged weapon.
    """
    weapon_type = actor.get_ranged_type()
    if tutor:
        skillup_check(actor, weapon_type)
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'precision')
    return base * bonus


def ranged_hit_rating(actor):
    """
    Rate Actor's ranged weapon skill + combat prowess.
    Uses the average of offense + weapon skill.
    """
    offense = offense_rating(actor)
    weapon = ranged_rating(actor)
    return (offense + weapon) / 2


def ranged_crit_rating(actor):
    """
    Return the Actor's rating for ranged critical strikes.
    """
    weapon_type = actor.get_ranged_type()
    base = actor.get_skill(weapon_type)
    bonus = stat_bonus(actor, 'cunning')
    return base * bonus


def ranged_max_dmg(actor):
    """
    Return the maximum damage for the Actor's ranged weapon.
    """
    dmg = actor.get_primary_dmg()
    bonus = stat_bonus(actor, 'precision')
    return dmg * bonus
