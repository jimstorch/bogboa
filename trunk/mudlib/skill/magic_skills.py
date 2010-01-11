# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   mudlib/skill/magic_skills.py
#   Copyright 2010 Jim Storch
#   Distributed under the terms of the GNU General Public License
#   See docs/LICENSE.TXT or http://www.gnu.org/licenses/ for details
#------------------------------------------------------------------------------

"""
Rate magic-related skills.
"""

from mudlib.skill import skill_check

def detrimental_magic_rating(actor, tutor=True):
    """
    Rate Actor's detrimental magic skill.
    """
    if tutor:
        skillup_check(actor, 'detrimental_magic')
    base = actor.get_skill('detrimental_magic')
    bonus = stat_bonus(actor, 'precision')
    return base * bonus


def beneficial_magic_rating(actor, tutor=True):
    """
    Rate Actor's beneficial magic skill.
    """
    if tutor:
        skillup_check(actor, 'beneficial_magic')
    base = actor.get_skill('beneficial_magic')
    bonus = stat_bonus(actor, 'faith')
    return base * bonus


def magic_school_rating(actor, tutor=True):
    """
    Rate the Actor's current magic category.
    """
    school = actor.get_magic_school()
    if tutor:
        skillup_check(actor, school)
    base = actor.get_skill(school)
    bonus = stat_bonus(actor, 'knowledge')
    return base * bonus


def spell_hit_rating(actor):
    """
    Rate Actor's ability to score a detrimental spell.
    Uses the average of offense + magic category skill.
    """
    offense = offensive_melee_rating(actor)
    school = magic_school_rating(actor)
    return (offense + school) / 2
